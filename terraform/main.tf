resource "aws_key_pair" "deployer" {
  key_name   = "${var.name}-key"
  public_key = file(pathexpand(var.public_key_path))

  tags = {
    Name        = "${var.name}-key"
    description = "Public key for SSH access to the EC2 instance"
  }
}

module "ec2_instance" {
  source        = "./modules/ec2"
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = aws_key_pair.deployer.key_name
  name          = var.name
}
