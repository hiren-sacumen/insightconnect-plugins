# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    AVAILABILITYSET = "availabilitySet"
    RESOURCEGROUP = "resourceGroup"
    SUBSCRIPTIONID = "subscriptionId"
    

class Output:
    VALUE = "value"
    

class AvailabilitySetVmInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "availabilitySet": {
      "type": "string",
      "title": "Availability Set",
      "description": "The availability set that contains the virtual machine",
      "order": 3
    },
    "resourceGroup": {
      "type": "string",
      "title": "Resource Group",
      "description": "The resource group that will contain the virtual machine",
      "order": 2
    },
    "subscriptionId": {
      "type": "string",
      "title": "Subscription ID",
      "description": "The identifier of your subscription",
      "order": 1
    }
  },
  "required": [
    "subscriptionId",
    "resourceGroup",
    "availabilitySet"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AvailabilitySetVmOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "value": {
      "type": "array",
      "title": "Value",
      "description": "List sizes in availability set",
      "items": {
        "$ref": "#/definitions/value_size_vm"
      },
      "order": 1
    }
  },
  "definitions": {
    "value_size_vm": {
      "type": "object",
      "title": "value_size_vm",
      "properties": {
        "maxDataDiskCount": {
          "type": "integer",
          "title": "Max Data Disk Count",
          "description": "Specifies the maximum number of data disks that can be attached to the vm size",
          "order": 1
        },
        "memoryInMB": {
          "type": "integer",
          "title": "Memory In MB",
          "description": "Specifies the available ram in mb",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Specifies the name of the virtual machine size",
          "order": 3
        },
        "numberOfCores": {
          "type": "integer",
          "title": "Number Of Cores",
          "description": "Specifies the number of available cpu cores",
          "order": 4
        },
        "osDiskSizeInMB": {
          "type": "integer",
          "title": "OS Disk Size In MB",
          "description": "Specifies the size in mb of the operating system disk",
          "order": 5
        },
        "resourceDiskSizeInMB": {
          "type": "integer",
          "title": "Resource Disk Size In MB",
          "description": "Specifies the size in mb of the temporary or resource disk",
          "order": 6
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
