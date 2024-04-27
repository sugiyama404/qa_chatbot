resource "aws_api_gateway_method" "MyMethod" {
  rest_api_id   = aws_api_gateway_rest_api.main.id
  resource_id   = aws_api_gateway_rest_api.main.root_resource_id
  http_method   = "POST"
  authorization = "NONE"

  depends_on = [aws_api_gateway_rest_api.main]
}

resource "aws_api_gateway_method" "MyMethods3" {
  rest_api_id   = aws_api_gateway_rest_api.main.id
  resource_id   = aws_api_gateway_rest_api.main.root_resource_id
  http_method   = "GET"
  authorization = "NONE"

  depends_on = [aws_api_gateway_rest_api.main]
}
