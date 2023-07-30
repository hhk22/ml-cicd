resource "aws_vpc" "test-vpc" {
  assign_generated_ipv6_cidr_block = "false"
  cidr_block                       = "172.31.0.0/16"
  instance_tenancy                 = "default"

  tags = {
    Name = "test-vpc"
  }

  tags_all = {
    Name = "test-vpc"
  }
}