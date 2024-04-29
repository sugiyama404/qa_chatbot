resource "aws_lb" "main" {
  name                       = "main-alb"
  internal                   = true
  load_balancer_type         = "network"
  enable_deletion_protection = false
  security_groups            = [var.sg_alb_id]
  subnets                    = [var.subnet_public_subnet_1a_id]

  tags = {
    "key" = "main-vpc"
  }
}
