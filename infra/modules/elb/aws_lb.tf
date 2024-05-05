resource "aws_lb" "main" {
  name                       = "main-alb"
  internal                   = false
  enable_deletion_protection = false
  load_balancer_type         = "network"
  security_groups            = [var.sg_alb_id]
  subnets = [
    var.subnet_public_subnet_1a_id,
    var.subnet_public_subnet_1c_id
  ]

  tags = {
    "key" = "main-vpc"
  }
}
