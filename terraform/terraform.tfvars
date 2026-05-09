region          = "ap-south-1"
ami             = "ami-039c8bec2cb71e1ea" # Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type (example for ap-south-1)
instance_type   = "t4g.small"
name            = "nginx-server-monitoring"
public_key_path = "~/.ssh/id_ed25519_personal.pub"
