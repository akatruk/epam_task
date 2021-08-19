output "instance_ips" {
  value = module.vpc.public_subnets
}

output "vpc" {
  value = module.vpc.vpc_id
}