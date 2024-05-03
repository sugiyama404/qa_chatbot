resource "aws_ecs_task_definition" "MainDefinition" {
  family                   = "${var.app_name}-definition"
  requires_compatibilities = ["FARGATE"]
  cpu                      = 512
  memory                   = 1024
  execution_role_arn       = var.aws_iam_role
  task_role_arn            = var.aws_iam_role
  network_mode             = "awsvpc"
  container_definitions = jsonencode([
    {
      name      = "${var.app_name}"
      image     = "${var.api_repository_url}:latest"
      cpu       = 512
      memory    = 1024
      essential = true
      portMappings = [
        {
          containerPort = var.api_port
          hostPort      = var.api_port
        }
      ]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-region        = "ap-northeast-1"
          awslogs-stream-prefix = "${var.app_name}"
          awslogs-create-group  = "true"
          awslogs-group         = "/fargate/${var.app_name}/dev"
        }
      }
    }
  ])
  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "X86_64"
  }

  tags = {
    Name = "${var.app_name}-template"
  }
}
