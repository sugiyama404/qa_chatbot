output "lb_target_group_api_arn" {
  value = aws_lb_target_group.api.arn
}

output "api_gateway_vpc_link_id" {
  value = aws_api_gateway_vpc_link.main.id
}

output "elb_uri" {
  value = "http://${aws_lb.main.dns_name}"
}
