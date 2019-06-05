# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    XPATH = "xpath"
    

class Output:
    RESPONSE = "response"
    

class ShowInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "xpath": {
      "type": "string",
      "title": "Xpath",
      "description": "Xpath targeting the requested portion of the configuration",
      "order": 1
    }
  },
  "required": [
    "xpath"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ShowOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/config",
      "title": "Response",
      "description": "Response from PAN-OS",
      "order": 1
    }
  },
  "definitions": {
    "config": {
      "type": "object",
      "title": "config",
      "properties": {
        "data": {
          "type": "object",
          "title": "Data",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
