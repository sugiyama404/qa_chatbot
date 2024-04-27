resource "aws_api_gateway_vpc_link" "main" {
  name        = "main-vpc-link"
  description = "main description"
  target_arns = [aws_lb.main.arn]
}
