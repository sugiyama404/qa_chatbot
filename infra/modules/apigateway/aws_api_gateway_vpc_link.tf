# resource "aws_api_gateway_vpc_link" "main" {
#   name        = "main-vpc-link"
#   description = "main description"
#   target_arns = ["${var.alb_arn}"]

#   tags = {
#     Name = "${var.app_name}-template"
#   }
# }
