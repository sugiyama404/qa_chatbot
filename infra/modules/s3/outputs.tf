output "s3_url" {
  value = "http://${aws_s3_bucket.main.bucket}.s3-website.${var.region}.amazonaws.com/index.html"
}

output "s3_uri" {
  value = "s3://${aws_s3_bucket.main.bucket}"
}
