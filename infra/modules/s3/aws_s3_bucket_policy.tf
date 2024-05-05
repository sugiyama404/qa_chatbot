resource "aws_s3_bucket_policy" "allow_access" {
  bucket = aws_s3_bucket.main.id
  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::${aws_s3_bucket.main.bucket}/*"
            ]
        }
    ]
}
POLICY

  depends_on = [aws_s3_bucket_public_access_block.main]
}
