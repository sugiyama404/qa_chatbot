resource "null_resource" "default" {
  provisioner "local-exec" {
    command = "aws ecr get-login-password --region ${var.region} | docker login --username AWS --password-stdin ${data.aws_caller_identity.self.account_id}.dkr.ecr.ap-northeast-1.amazonaws.com"
  }

  provisioner "local-exec" {
    command = "docker push ${data.aws_caller_identity.self.account_id}.dkr.ecr.ap-northeast-1.amazonaws.com/${var.image_name}:latest"
  }
}
