terraform {
  backend "s3" {
    bucket       = "abhradip-terraform-state-bucket"
    key          = "nginx-server-monitoring/terraform.tfstate"
    region       = "ap-south-1"
    encrypt      = true
    use_lockfile = true
  }
}
