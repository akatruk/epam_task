### Variables for RDS and VPC ###

variable "access_key" {}
variable "secret_key" {}
variable "region" {}
variable "vpc_name" {}
variable "cidr" {}
variable "private_subnets" {}
variable "public_subnets" {}
variable "rds_port" {}
variable "rds_name" {}
variable "rds_username" {}
variable "rds_password" {}

### Variables for EKS ###

variable "cluster_name" {}
variable "instance_type" {}
variable "vpc_id" {}
variable "k8s_nodes_count" {}
