resource "aws_cloudfront_origin_access_control" "s3" {
  name                              = "s3_access_control"
  description                       = "S3 Access Control Policy"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "never"
  signing_protocol                  = "sigv4"
}

