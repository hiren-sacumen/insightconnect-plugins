# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
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
    

class Output:
    CLIENTOPERATIONID = "clientOperationId"
    DESCRIPTION = "description"
    ENDTIME = "endTime"
    ERROR = "error"
    HTTPERRORMESSAGE = "httpErrorMessage"
    HTTPERRORSTATUSCODE = "httpErrorStatusCode"
    ID = "id"
    INSERTTIME = "insertTime"
    KIND = "kind"
    NAME = "name"
    OPERATIONTYPE = "operationType"
    PROGRESS = "progress"
    REGION = "region"
    SELFLINK = "selfLink"
    STARTTIME = "startTime"
    STATUS = "status"
    STATUSMESSAGE = "statusMessage"
    TARGETID = "targetId"
    TARGETLINK = "targetLink"
    USER = "user"
    WARNINGS = "warnings"
    ZONE = "zone"
    

class InsertFirewallInput(komand.Input):
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
      "order": 2
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
      "order": 6
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The unique identifier for the resource. This identifier is defined by the server",
      "order": 3
    },
    "kind": {
      "type": "string",
      "title": "Kind",
      "description": "Type of the resource. Always compute#firewall for firewall rules",
      "order": 4
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name of the resource, provided by the client when the resource is created",
      "order": 1
    },
    "network": {
      "type": "string",
      "title": "Network",
      "description": "URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default",
      "order": 7
    },
    "selfLink": {
      "type": "string",
      "title": "Self Link",
      "description": "Server-defined url for the resource",
      "order": 5
    },
    "sourceRanges": {
      "type": "array",
      "title": "Source Ranges",
      "description": "If source ranges are specified, the firewall will apply only to traffic that has source ip address in these ranges",
      "items": {
        "type": "string"
      },
      "order": 9
    },
    "sourceTags": {
      "type": "array",
      "title": "Source Tags",
      "description": "If source tags are specified, the firewall will apply only to traffic with source ip that belongs to a tag listed in source tags",
      "items": {
        "type": "string"
      },
      "order": 8
    },
    "targetTags": {
      "type": "array",
      "title": "Target Tags",
      "description": "A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[]",
      "items": {
        "type": "string"
      },
      "order": 10
    }
  },
  "required": [
    "name",
    "allowed"
  ],
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


class InsertFirewallOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "clientOperationId": {
      "type": "string",
      "title": "Client OperationId",
      "description": "Reserved for future use",
      "order": 14
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "A textual description of the operation, which is set when the operation is created",
      "order": 4
    },
    "endTime": {
      "type": "string",
      "title": "End Time",
      "description": "The time that this operation was completed",
      "order": 22
    },
    "error": {
      "$ref": "#/definitions/error",
      "title": "Error",
      "description": "If errors are generated during processing of the operation, this field will be populated",
      "order": 21
    },
    "httpErrorMessage": {
      "type": "string",
      "title": "Http Error Message",
      "description": "If the operation fails, this field contains the http error message that was returned",
      "order": 15
    },
    "httpErrorStatusCode": {
      "type": "integer",
      "title": "Http Error Status Code",
      "description": "If the operation fails, this field contains the http error status code that was returned",
      "order": 16
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The unique identifier for the resource. This identifier is defined by the server",
      "order": 1
    },
    "insertTime": {
      "type": "string",
      "title": "Insert Time",
      "description": "The time that this operation was requested",
      "order": 5
    },
    "kind": {
      "type": "string",
      "title": "Kind",
      "description": "Type of the resource. Always compute#operation for operation resources",
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name of the resource",
      "order": 3
    },
    "operationType": {
      "type": "string",
      "title": "Operation Type",
      "description": "The type of operation, such as insert, update, or delete, and so on",
      "order": 17
    },
    "progress": {
      "type": "integer",
      "title": "Progress",
      "description": "An optional progress indicator that ranges from 0 to 100",
      "order": 6
    },
    "region": {
      "type": "string",
      "title": "Region",
      "description": "The url of the region where the operation resides",
      "order": 20
    },
    "selfLink": {
      "type": "string",
      "title": "Self Link",
      "description": "Server-defined url for the resource",
      "order": 9
    },
    "startTime": {
      "type": "string",
      "title": "Start Time",
      "description": "The time that this operation was started by the server",
      "order": 19
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "The status of the operation, which can be one of the following: pending, running, or done",
      "order": 12
    },
    "statusMessage": {
      "type": "string",
      "title": "Status Message",
      "description": "An optional textual description of the current status of the operation",
      "order": 13
    },
    "targetId": {
      "type": "string",
      "title": "TargetID",
      "description": "The unique targetID, which identifies a specific incarnation of the target resource",
      "order": 8
    },
    "targetLink": {
      "type": "string",
      "title": "Target Link",
      "description": "The url of the resource that the operation modifies",
      "order": 7
    },
    "user": {
      "type": "string",
      "title": "User",
      "description": "User who requested the operation",
      "order": 10
    },
    "warnings": {
      "type": "array",
      "title": "Warnings",
      "description": "Warning messages",
      "items": {
        "$ref": "#/definitions/warnings"
      },
      "order": 18
    },
    "zone": {
      "type": "string",
      "title": "Zone",
      "description": "The url of the zone where the operation resides. Only available when performing per-zone operations",
      "order": 11
    }
  },
  "definitions": {
    "data": {
      "type": "object",
      "title": "data",
      "properties": {
        "key": {
          "type": "string",
          "title": "Key",
          "order": 1
        },
        "value": {
          "type": "string",
          "title": "Value",
          "order": 2
        }
      }
    },
    "error": {
      "type": "object",
      "title": "error",
      "properties": {
        "errors": {
          "type": "array",
          "title": "Errors",
          "items": {
            "$ref": "#/definitions/errors"
          },
          "order": 1
        }
      },
      "definitions": {
        "errors": {
          "type": "object",
          "title": "errors",
          "properties": {
            "code": {
              "type": "string",
              "title": "Code",
              "order": 1
            },
            "location": {
              "type": "string",
              "title": "Location",
              "order": 2
            },
            "message": {
              "type": "string",
              "title": "Message",
              "order": 3
            }
          }
        }
      }
    },
    "errors": {
      "type": "object",
      "title": "errors",
      "properties": {
        "code": {
          "type": "string",
          "title": "Code",
          "order": 1
        },
        "location": {
          "type": "string",
          "title": "Location",
          "order": 2
        },
        "message": {
          "type": "string",
          "title": "Message",
          "order": 3
        }
      }
    },
    "warnings": {
      "type": "object",
      "title": "warnings",
      "properties": {
        "code": {
          "type": "string",
          "title": "Code",
          "order": 1
        },
        "data": {
          "type": "array",
          "title": "Data",
          "items": {
            "$ref": "#/definitions/data"
          },
          "order": 2
        },
        "message": {
          "type": "string",
          "title": "Message",
          "order": 3
        }
      },
      "definitions": {
        "data": {
          "type": "object",
          "title": "data",
          "properties": {
            "key": {
              "type": "string",
              "title": "Key",
              "order": 1
            },
            "value": {
              "type": "string",
              "title": "Value",
              "order": 2
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
