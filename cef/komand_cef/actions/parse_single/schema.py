# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CEF_STRING = "cef_string"
    

class Output:
    CEF = "cef"
    

class ParseSingleInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cef_string": {
      "type": "string",
      "title": "Cef String",
      "description": "CEF formatted string",
      "order": 1
    }
  },
  "required": [
    "cef_string"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ParseSingleOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cef": {
      "$ref": "#/definitions/cef",
      "title": "Cef",
      "description": "CEF object",
      "order": 1
    }
  },
  "definitions": {
    "cef": {
      "type": "object",
      "title": "cef",
      "properties": {
        "device_product": {
          "type": "string",
          "title": "Device Product",
          "description": "With vendor and version, uniquely identifies the type of sending device",
          "order": 3
        },
        "device_vendor": {
          "type": "string",
          "title": "Device Vendor",
          "description": "With product and version, uniquely identifies the type of sending device",
          "order": 2
        },
        "device_version": {
          "type": "string",
          "title": "Device Version",
          "description": "With vendor and product, uniquely identifies the type of sending device",
          "order": 4
        },
        "extension": {
          "type": "object",
          "title": "Extension",
          "description": "JSON object of key value pairs with keys and values as defined by the ArcSight Extension Dictionary",
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Represents a human-readable and understandable description of the event",
          "order": 6
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Reflects the importance of the event",
          "enum": [
            "Low",
            "Medium",
            "High",
            "Very-High",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10"
          ],
          "order": 7
        },
        "signature_id": {
          "type": "string",
          "title": "Signature Id",
          "description": "Unique identifier per event-type",
          "order": 5
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Identifies the version of the CEF format",
          "default": "0.1",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
