resource "aws_ecs_cluster" "MainCluster" {
  name = "${var.app_name}-cluster"
}

resource "aws_ecs_cluster_capacity_providers" "newworld_capacity_providers" {
  cluster_name       = "${var.app_name}-cluster"
  capacity_providers = ["FARGATE"]

  default_capacity_provider_strategy {
    base              = 1
    weight            = 100
    capacity_provider = "FARGATE"
  }
}
