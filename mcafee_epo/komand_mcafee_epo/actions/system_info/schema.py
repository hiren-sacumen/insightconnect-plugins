# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "List system information"


class Input:
    QUERY = "query"
    

class Output:
    PROPERTIES = "properties"
    

class SystemInfoInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "System search query e.g Device-1",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SystemInfoOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "properties": {
      "type": "array",
      "title": "Properties",
      "description": "Computer Properties",
      "items": {
        "$ref": "#/definitions/computer_properties"
      },
      "order": 1
    }
  },
  "required": [
    "properties"
  ],
  "definitions": {
    "computer_properties": {
      "type": "object",
      "title": "computer_properties",
      "properties": {
        "EPOBranchNode.AutoID": {
          "type": "integer",
          "title": "Auto ID",
          "order": 10
        },
        "EPOComputerProperties.CPUSerialNum": {
          "type": "string",
          "title": "CPU Serial Number",
          "order": 30
        },
        "EPOComputerProperties.CPUSpeed": {
          "type": "integer",
          "title": "CPU Speed",
          "order": 1
        },
        "EPOComputerProperties.CPUType": {
          "type": "string",
          "title": "CPU Type",
          "order": 15
        },
        "EPOComputerProperties.ComputerName": {
          "type": "string",
          "title": "Computer Name",
          "order": 3
        },
        "EPOComputerProperties.DefaultLangID": {
          "type": "string",
          "title": "Default Lang ID",
          "order": 11
        },
        "EPOComputerProperties.Description": {
          "type": "string",
          "title": "Description",
          "order": 9
        },
        "EPOComputerProperties.DomainName": {
          "type": "string",
          "title": "Domain Name",
          "order": 18
        },
        "EPOComputerProperties.FreeDiskSpace": {
          "type": "integer",
          "title": "Free Disk Space",
          "order": 41
        },
        "EPOComputerProperties.FreeMemory": {
          "type": "integer",
          "title": "Free Memory",
          "order": 8
        },
        "EPOComputerProperties.IPAddress": {
          "type": "string",
          "title": "IP Address",
          "order": 17
        },
        "EPOComputerProperties.IPHostName": {
          "type": "string",
          "title": "IP Host Name",
          "order": 19
        },
        "EPOComputerProperties.IPSubnet": {
          "type": "string",
          "title": "IP Subnet",
          "order": 21
        },
        "EPOComputerProperties.IPSubnetMask": {
          "type": "string",
          "title": "IP Subnet Mask",
          "order": 32
        },
        "EPOComputerProperties.IPV4x": {
          "type": "integer",
          "title": "IPv4",
          "order": 12
        },
        "EPOComputerProperties.IPV6": {
          "type": "string",
          "title": "IPv6",
          "order": 20
        },
        "EPOComputerProperties.IPXAddress": {
          "type": "string",
          "title": "EPOComputerProperties IPXAddress",
          "order": 22
        },
        "EPOComputerProperties.IsPortable": {
          "type": "integer",
          "title": "Is Portable",
          "order": 6
        },
        "EPOComputerProperties.LastAgentHandler": {
          "type": "integer",
          "title": "Last Agent Handler",
          "order": 49
        },
        "EPOComputerProperties.NetAddress": {
          "type": "string",
          "title": "Net Address",
          "order": 35
        },
        "EPOComputerProperties.NumOfCPU": {
          "type": "integer",
          "title": "Number of CPU's",
          "order": 44
        },
        "EPOComputerProperties.OSBitMode": {
          "type": "integer",
          "title": "OS Bit Mode",
          "order": 34
        },
        "EPOComputerProperties.OSBuildNum": {
          "type": "integer",
          "title": "OS Build Number",
          "order": 4
        },
        "EPOComputerProperties.OSOEMID": {
          "type": "string",
          "title": "OS OEM ID",
          "order": 16
        },
        "EPOComputerProperties.OSPlatform": {
          "type": "string",
          "title": "OS Platform",
          "order": 2
        },
        "EPOComputerProperties.OSServicePackVer": {
          "type": "string",
          "title": "OS Service Pack Version",
          "order": 29
        },
        "EPOComputerProperties.OSType": {
          "type": "string",
          "title": "OS Type",
          "order": 36
        },
        "EPOComputerProperties.OSVersion": {
          "type": "string",
          "title": "OS Version",
          "order": 31
        },
        "EPOComputerProperties.ParentID": {
          "type": "integer",
          "title": "Parent ID",
          "order": 47
        },
        "EPOComputerProperties.SubnetAddress": {
          "type": "string",
          "title": "Subnet Address",
          "order": 43
        },
        "EPOComputerProperties.SubnetMask": {
          "type": "string",
          "title": "Subnet Mask",
          "order": 28
        },
        "EPOComputerProperties.SystemDescription": {
          "type": "string",
          "title": "System Description",
          "order": 42
        },
        "EPOComputerProperties.SysvolFreeSpace": {
          "type": "integer",
          "title": "System Volume Free Space",
          "order": 14
        },
        "EPOComputerProperties.SysvolTotalSpace": {
          "type": "integer",
          "title": "System Volume Total Space",
          "order": 23
        },
        "EPOComputerProperties.TimeZone": {
          "type": "string",
          "title": "Time Zone",
          "order": 33
        },
        "EPOComputerProperties.TotalDiskSpace": {
          "type": "integer",
          "title": "Total Disk Space",
          "order": 45
        },
        "EPOComputerProperties.TotalPhysicalMemory": {
          "type": "integer",
          "title": "Total Physical Memory",
          "order": 13
        },
        "EPOComputerProperties.UserName": {
          "type": "string",
          "title": "User Name",
          "order": 25
        },
        "EPOComputerProperties.UserProperty1": {
          "type": "string",
          "title": "User Property 1",
          "order": 38
        },
        "EPOComputerProperties.UserProperty2": {
          "type": "string",
          "title": "User Property 2",
          "order": 40
        },
        "EPOComputerProperties.UserProperty3": {
          "type": "string",
          "title": "User Property 3",
          "order": 39
        },
        "EPOComputerProperties.UserProperty4": {
          "type": "string",
          "title": "User Property",
          "order": 5
        },
        "EPOComputerProperties.Vdi": {
          "type": "integer",
          "title": "VDI",
          "order": 27
        },
        "EPOLeafNode.AgentGUID": {
          "type": "string",
          "title": "Agent GUID",
          "order": 26
        },
        "EPOLeafNode.AgentVersion": {
          "type": "string",
          "title": "Agent Version",
          "order": 37
        },
        "EPOLeafNode.ExcludedTags": {
          "type": "string",
          "title": "Excluded Tags",
          "order": 48
        },
        "EPOLeafNode.LastUpdate": {
          "type": "string",
          "title": "Last Update",
          "order": 24
        },
        "EPOLeafNode.ManagedState": {
          "type": "integer",
          "title": "Managed State",
          "order": 7
        },
        "EPOLeafNode.Tags": {
          "type": "string",
          "title": "Tags",
          "order": 46
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
