terraform {
  required_version = "=1.0.6"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = var.region
}

# IAM
module "iam" {
  source   = "./modules/iam"
  app_name = var.app_name
}

# ECR
module "ecr" {
  source     = "./modules/ecr"
  image_name = var.image_name
  app_name   = var.app_name
}

# Null Resource
module "after_ecr" {
  source     = "./modules/bash"
  region     = var.region
  image_name = var.image_name
}

# network
module "network" {
  source   = "./modules/network"
  app_name = var.app_name
  api_port = var.api_port
}

# ELB
module "elb" {
  source                  = "./modules/elb"
  app_name                = var.app_name
  api_port                = var.api_port
  main_vpc_id             = module.network.main_vpc_id
  subnet_public_subnet_1a = module.network.subnet_public_subnet_1a_id
  sg_alb_id               = module.network.sg_alb_id
}

# ECS
module "ecs" {
  source                      = "./modules/ecs"
  app_name                    = var.app_name
  sg_ecs_id                   = module.network.sg_ecs_id
  subnet_private_subnet_1a_id = module.network.subnet_private_subnet_1a_id
  aws_iam_role                = module.iam.aws_iam_role
  api_repository_url          = module.ecr.api_repository_url
  lb_target_group_api_arn     = module.elb.lb_target_group_api_arn
  api_port                    = var.api_port
}


# # s3
# module "s3" {
#   source   = "./modules/s3"
#   app_name = var.app_name
#   region   = var.region
# }

# apigateway
module "apigateway" {
  source                  = "./modules/apigateway"
  app_name                = var.app_name
  region                  = var.region
  api_gateway_vpc_link_id = module.elb.api_gateway_vpc_link_id
  elb_uri                 = module.elb.elb_uri

  # s3_uri            = module.s3.s3_uri
  # s3_url            = module.s3.s3_url

}