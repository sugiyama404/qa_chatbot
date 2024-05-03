resource "aws_ecs_cluster" "MainCluster" {
  name = "${var.app_name}-cluster"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }

  tags = {
    Name = "${var.app_name}-cluster"
  }
}

resource "aws_ecs_cluster_capacity_providers" "newworld_capacity_providers" {
  cluster_name       = "${var.app_name}-cluster"
  capacity_providers = ["FARGATE"]

}
