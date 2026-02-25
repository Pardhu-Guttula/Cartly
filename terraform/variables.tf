variable "resource_group_name" {
  description = "The name of the resource group."
  type        = string
  default     = "cartly-rg"
}

variable "location" {
  description = "The Azure location where resources should be created."
  type        = string
  default     = "East US"
}

variable "app_service_plan_name" {
  description = "The name of the App Service plan."
  type        = string
  default     = "cartly-app-service-plan"
}

variable "web_app_name" {
  description = "The name of the Web App."
  type        = string
  default     = "cartly-web-app"
}

variable "cdn_profile_name" {
  description = "The name of the CDN profile."
  type        = string
  default     = "cartly-cdn-profile"
}

variable "cdn_endpoint_name" {
  description = "The name of the CDN endpoint."
  type        = string
  default     = "cartly-cdn-endpoint"
}