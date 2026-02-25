provider "azurerm" {
  features {}
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.56.0"
    }
  }
}

resource "azurerm_resource_group" "rg" {
  name     = "cartly-rg"
  location = "West Europe"
}

resource "azurerm_app_service" "webapp" {
  name                = "cartly-webapp"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.appserviceplan.id
}

resource "azurerm_app_service" "backend_app" {
  name                = "cartly-backend-app"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.appserviceplan.id
}

resource "azurerm_app_service_plan" "appserviceplan" {
  name                = "cartly-appserviceplan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_frontdoor" "frontdoor" {
  name                = "cartly-frontdoor"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_function_app" "functionapp" {
  name                = "cartly-functions"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.appserviceplan.id
}

resource "azurerm_active_directory_b2c" "adb2c" {
  name     = "cartlyadb2c"
  location = azurerm_resource_group.rg.location
}
