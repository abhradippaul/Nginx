import requests
import threading
import time
import urllib3
import statistics
import math
import os

# Suppress insecure request warnings for self-signed certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration from Environment Variables
TARGET_URL = os.getenv("TARGET_URL", "https://localhost/api")
MAX_USERS = int(os.getenv("MAX_USERS", "20"))
DURATION_SECONDS = int(os.getenv("DURATION", "300")) # Default 5 mins for better visualization
CYCLE_SECONDS = int(os.getenv("CYCLE", "60"))      # Time for one full wave

# Shared stats
stats = {
    "total": 0,
    "success": 0,
    "failure": 0,
    "latencies": []
}
stats_lock = threading.Lock()
stop_event = threading.Event()

def get_target_concurrency(elapsed):
    """Calculates target concurrency based on a sine wave."""
    # Oscillates between 1 and MAX_USERS over CYCLE_SECONDS
    wave = (math.sin(elapsed * 2 * math.pi / CYCLE_SECONDS - (math.pi / 2)) + 1) / 2
    return int(wave * (MAX_USERS - 1) + 1)

def worker_node(user_id):
    """A worker that only performs requests when the wave allows it."""
    while not stop_event.is_set():
        elapsed = time.time() - start_time
        target = get_target_concurrency(elapsed)
        
        # If this worker's ID is higher than current target, it 'sleeps' until needed
        if user_id < target:
            req_start = time.time()
            try:
                response = requests.get(TARGET_URL, verify=False, timeout=5)
                latency = time.time() - req_start
                with stats_lock:
                    stats["total"] += 1
                    if response.status_code == 200:
                        stats["success"] += 1
                    else:
                        stats["failure"] += 1
                    stats["latencies"].append(latency)
            except Exception:
                with stats_lock:
                    stats["total"] += 1
                    stats["failure"] += 1
            
            # Pacing
            time.sleep(0.1)
        else:
            # Not active in the current wave, wait a bit and check again
            time.sleep(0.5)

if __name__ == "__main__":
    print(f"🌊 Starting Dynamic Load Test (Sine Wave Profile)")
    print(f"Target:      {TARGET_URL}")
    print(f"Max Users:   {MAX_USERS}")
    print(f"Cycle:       {CYCLE_SECONDS}s")
    print(f"Duration:    {DURATION_SECONDS}s")
    print("-" * 35)

    start_time = time.time()
    threads = []
    
    # Pre-spawn all potential workers
    for i in range(MAX_USERS):
        t = threading.Thread(target=worker_node, args=(i,))
        t.start()
        threads.append(t)

    try:
        while time.time() - start_time < DURATION_SECONDS:
            elapsed = time.time() - start_time
            current_target = get_target_concurrency(elapsed)
            # Print a simple progress bar
            bar = "█" * current_target + "░" * (MAX_USERS - current_target)
            print(f"\r[{bar}] Users: {current_target:3} | Elapsed: {int(elapsed):3}s", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping...")

    stop_event.set()
    for t in threads:
        t.join()

    # Calculate Results
    print("\n\n✅ Load Test Complete")
    print("-" * 35)
    print(f"Total Requests: {stats['total']}")
    print(f"Successes:      {stats['success']}")
    print(f"Failures:       {stats['failure']}")
    
    if stats["latencies"]:
        avg_lat = sum(stats["latencies"]) / len(stats["latencies"])
        p95_lat = statistics.quantiles(stats["latencies"], n=20)[18] if len(stats["latencies"]) > 1 else avg_lat
        print(f"Avg Latency:    {avg_lat:.4f}s")
        print(f"P95 Latency:    {p95_lat:.4f}s")
        print(f"Requests/sec:   {stats['total'] / (time.time() - start_time):.2f}")
