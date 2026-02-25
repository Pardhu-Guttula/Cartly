provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "cartly-rg"
  location = "East US"
}

resource "azurerm_app_service_plan" "asp" {
  name                = "cartly-app-service-plan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "web_app" {
  name                = "cartly-web-app"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.asp.id
  site_config {
    dotnet_framework_version = "v4.0"
    scm_type                 = "LocalGit"
  }
}

resource "azurerm_cdn_profile" "cdn" {
  name                = "cartly-cdn-profile"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Standard_Microsoft"
}

resource "azurerm_cdn_endpoint" "cdn_endpoint" {
  name                = "cartly-cdn-endpoint"
  profile_name        = azurerm_cdn_profile.cdn.name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  origin_host_header  = azurerm_app_service.web_app.default_host_name
  origins {
    name      = "cartly-origin"
    host_name = azurerm_app_service.web_app.default_host_name
  }
}