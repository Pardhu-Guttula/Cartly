variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "cartly-rg"
}

variable "location" {
  description = "Azure location"
  type        = string
  default     = "West Europe"
}

variable "webapp_name" {
  description = "Name of the Azure App Service web app"
  type        = string
  default     = "cartly-webapp"
}

variable "backend_app_name" {
  description = "Name of the Azure App Service API app"
  type        = string
  default     = "cartly-backend-app"
}

variable "appservice_plan_name" {
  description = "Name of the Azure App Service plan"
  type        = string
  default     = "cartly-appserviceplan"
}

variable "frontdoor_name" {
  description = "Name of the Azure Front Door"
  type        = string
  default     = "cartly-frontdoor"
}

variable "function_app_name" {
  description = "Name of the Azure Function App"
  type        = string
  default     = "cartly-functions"
}

variable "adb2c_name" {
  description = "Name of the Azure Active Directory B2C instance"
  type        = string
  default     = "cartlyadb2c"
}
