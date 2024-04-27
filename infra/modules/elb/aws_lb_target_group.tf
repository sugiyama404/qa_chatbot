# LbTargetGroup for api
resource "aws_lb_target_group" "api" {
  name        = "${var.app_name}-tg"
  port        = var.api_port
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = var.main_vpc_id

  health_check {
    interval            = 300
    path                = "/"
    port                = var.api_port
    protocol            = "HTTP"
    timeout             = 120
    unhealthy_threshold = 10
    matcher             = "200-299"
  }

  tags = {
    Name = "${var.app_name}-tg"
  }
}
