resource "aws_ecs_service" "MainService" {
  name            = "nginx-service"
  cluster         = aws_ecs_cluster.MainCluster.id
  task_definition = aws_ecs_task_definition.MainDefinition.arn
  desired_count   = 1

  load_balancer {
    target_group_arn = var.lb_target_group_api_arn
    container_name   = var.app_name
    container_port   = var.api_port
  }

  network_configuration {
    security_groups  = [var.sg_ecs_id]
    subnets          = ["${var.subnet_private_subnet_1a_id}"]
    assign_public_ip = true
  }

  lifecycle {
    ignore_changes = [desired_count]
  }
}
