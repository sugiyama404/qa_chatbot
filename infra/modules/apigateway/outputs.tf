output "api_execution_arn" {
  value = aws_api_gateway_rest_api.main.execution_arn
}

output "api_gateway_origin_id" {
  value = aws_api_gateway_rest_api.main.id
}

output "api_gateway_domain_name" {
  value = "${aws_api_gateway_rest_api.main.id}.execute-api.ap-northeast-1.amazonaws.com"
}
