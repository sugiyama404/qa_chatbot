resource "aws_api_gateway_rest_api" "main" {
  body = jsonencode({
    openapi = "3.0.1"
    info = {
      title   = "api"
      version = "1.0"
    }
    paths = {
      # get = {
      #   x-amazon-apigateway-integration = {
      #     payloadFormatVersion = "1.0"
      #     type                 = "HTTP_PROXY"
      #     uri                  = "${var.s3_url}"
      #   }
      # }
      post = {
        x-amazon-apigateway-integration = {
          payloadFormatVersion = "1.0"
          type                 = "HTTP"
          connection_type      = "VPC_LINK"
          connection_id        = "${var.api_gateway_vpc_link_id}"
        }
      }
    }
  })

  name = "main"

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

