# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    FIREWALL = "firewall"
    

class Output:
    ALLOWED = "allowed"
    CREATIONTIMESTAMP = "creationTimestamp"
    DESCRIPTION = "description"
    ID = "id"
    KIND = "kind"
    NAME = "name"
    NETWORK = "network"
    SELFLINK = "selfLink"
    SOURCERANGES = "sourceRanges"
    SOURCETAGS = "sourceTags"
    TARGETTAGS = "targetTags"
    

class GetFirewallInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "firewall": {
      "type": "string",
      "title": "Firewall Name",
      "description": "Name of the firewall rule to return",
      "order": 1
    }
  },
  "required": [
    "firewall"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetFirewallOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "allowed": {
      "type": "array",
      "title": "Allowed",
      "description": "The list of allow rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection",
      "items": {
        "$ref": "#/definitions/allowed"
      },
      "order": 10
    },
    "creationTimestamp": {
      "type": "string",
      "title": "Creation Timestamp",
      "description": "Creation timestamp",
      "order": 11
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "A textual description of the operation, which is set when the operation is created",
      "order": 5
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The unique identifier for the resource. This identifier is defined by the server",
      "order": 1
    },
    "kind": {
      "type": "string",
      "title": "Kind",
      "description": "Type of the resource. Always compute#firewall for firewall rules",
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name of the resource, provided by the client when the resource is created",
      "order": 3
    },
    "network": {
      "type": "string",
      "title": "Network",
      "description": "URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default",
      "order": 6
    },
    "selfLink": {
      "type": "string",
      "title": "Self Link",
      "description": "Server-defined url for the resource",
      "order": 4
    },
    "sourceRanges": {
      "type": "array",
      "title": "Source Ranges",
      "description": "If source ranges are specified, the firewall will apply only to traffic that has source ip address in these ranges",
      "items": {
        "type": "string"
      },
      "order": 8
    },
    "sourceTags": {
      "type": "array",
      "title": "Source Tags",
      "description": "If source tags are specified, the firewall will apply only to traffic with source ip that belongs to a tag listed in source tags",
      "items": {
        "type": "string"
      },
      "order": 7
    },
    "targetTags": {
      "type": "array",
      "title": "Target Tags",
      "description": "A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[]",
      "items": {
        "type": "string"
      },
      "order": 9
    }
  },
  "definitions": {
    "allowed": {
      "type": "object",
      "title": "allowed",
      "properties": {
        "IPProtocol": {
          "type": "string",
          "title": "IPProtocol",
          "order": 1
        },
        "ports": {
          "type": "array",
          "title": "Ports",
          "items": {
            "type": "string"
          },
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
