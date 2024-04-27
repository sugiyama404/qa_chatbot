variable "app_name" {
  description = "application name"
  type        = string
  default     = "qa_chatbot"
}

variable "region" {
  description = "AWS region to create resources in"
  type        = string
  default     = "ap-northeast-1"
}

variable "image_name" {
  description = "application name"
  type        = string
  default     = "transformer"
}

variable "api_port" {
  description = "api port"
  type        = number
  default     = 8000
}
