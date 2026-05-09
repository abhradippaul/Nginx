resource "aws_security_group" "this" {
  name        = "${var.name}-sg"
  description = "Security group for Nginx and related services"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  dynamic "ingress" {
    for_each = [80, 443, 3000, 3001, 3002, 3003, 8080, 9090, 9113, 24224]
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "${var.name}-sg"
    description = "Security group for Nginx and related services"
  }
}

# resource "aws_instance" "this" {
#   ami                    = var.ami
#   instance_type          = var.instance_type
#   key_name               = var.key_name
#   subnet_id              = var.subnet_id
#   vpc_security_group_ids = [aws_security_group.this.id]

#   user_data = file("${path.module}/scripts/install_docker.sh")

#   tags = {
#     Name        = var.name
#     description = "EC2 instance running Nginx and Docker services"
#   }
# }
