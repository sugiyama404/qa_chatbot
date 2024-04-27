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
          uri                  = var.elb_uri
        }
      }
    }
  })

  name = "main"

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

