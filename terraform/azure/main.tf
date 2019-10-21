provider "azurerm" {
	version = "~> 1.35"
}

resource "azurerm_resource_group" "rg" {
        name = "packt-checker-resource-group"
        location = "westeurope"
}
