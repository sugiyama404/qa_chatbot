output "lb_target_group_api_arn" {
  value = aws_lb_target_group.api.arn
}

output "http_arn" {
  value = aws_lb_listener.http.arn
}

output "elb_uri" {
  value = "http://${aws_lb.main.dns_name}"
}

output "alb_arn" {
  value = aws_lb.main.arn
}
