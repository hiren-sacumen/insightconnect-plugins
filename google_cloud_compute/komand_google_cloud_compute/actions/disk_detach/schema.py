# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DEVICENAME = "deviceName"
    INSTANCE = "instance"
    ZONE = "zone"
    

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
    

class DiskDetachInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "deviceName": {
      "type": "string",
      "title": "Disk Name",
      "description": "Disk device name to detach",
      "order": 3
    },
    "instance": {
      "type": "string",
      "title": "Name Instance",
      "description": "Name of the instance resource to stop",
      "order": 2
    },
    "zone": {
      "type": "string",
      "title": "Zone",
      "description": "The name of the zone for this request",
      "order": 1
    }
  },
  "required": [
    "zone",
    "instance",
    "deviceName"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DiskDetachOutput(komand.Output):
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
