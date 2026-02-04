// Counter logic
let count = 0;
const countEl = document.getElementById("count");

function increment() {
    count++;
    updateCount();
}

function decrement() {
    count--;
    updateCount();
}

function reset() {
    count = 0;
    updateCount();
}

function updateCount() {
    countEl.textContent = count;
}

// Dark mode toggle
const themeToggle = document.getElementById("themeToggle");

themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    themeToggle.textContent =
        document.body.classList.contains("dark")
            ? "☀️ Light Mode"
            : "🌙 Dark Mode";
});

// Live text preview
const input = document.getElementById("textInput");
const preview = document.getElementById("previewText");

input.addEventListener("input", (e) => {
    preview.textContent = e.target.value || "Your text will appear here";
});
