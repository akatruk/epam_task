provider "aws" {
    access_key = var.access_key
    secret_key = var.secret_key
    region     = var.region
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = var.vpc_name
  cidr = var.cidr

  azs             = ["eu-west-3a", "eu-west-3b", "eu-west-3c"]
  private_subnets = var.private_subnets
  public_subnets  = var.public_subnets
  enable_dns_hostnames = true
  enable_dns_support   = true
  enable_nat_gateway = true
  enable_vpn_gateway = true

  tags = {
    Terraform = "true"
    Environment = "prd"
  }
}

resource "aws_security_group" "allow_rds" {
  name        = "allow_rds"
  description = "Allow ssh inbound traffic"
  vpc_id      = module.vpc.vpc_id

  dynamic "ingress" {
    for_each = ["5432"]
    content {
    description = "ssh from VPC"
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
    Name = "allow_postgres"
    Owner = "Andrey Katruk"
  }
}

module "db" {
  source  = "terraform-aws-modules/rds/aws"
  version = "~> 3.0"
  identifier = var.rds_name
  engine            = "postgres"
  engine_version    = "11.12"
  instance_class    = "db.t2.micro"
  allocated_storage = 5
  publicly_accessible = true
  name     = var.rds_name
  username = var.rds_username
  password = var.rds_password
  port     = var.rds_port
  iam_database_authentication_enabled = true
  vpc_security_group_ids = [aws_security_group.allow_rds.id]
  maintenance_window = "Mon:00:00-Mon:03:00"
  backup_window      = "03:00-06:00"
  tags = {
    Owner       = "akatruk"
    Environment = "prod"
  }
  subnet_ids = module.vpc.public_subnets
  family = "postgres11"
  deletion_protection = false
}