output "s3_url" {
  value = "http://${aws_s3_bucket.main.bucket}.s3-website.${var.region}.amazonaws.com/index.html"
}

output "s3_uri" {
  value = "s3://${aws_s3_bucket.main.bucket}"
}

output "s3_domain_name" {
  value = aws_s3_bucket.main.bucket_regional_domain_name
}

output "s3_origin_id" {
  value = aws_s3_bucket.main.id
}
