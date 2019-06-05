# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    pass

class Output:
    RESPONSE = "response"
    

class UsageInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UsageOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/USAGE_Output",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "required": [
    "response"
  ],
  "definitions": {
    "USAGE_Output": {
      "type": "object",
      "title": "USAGE_Output",
      "properties": {
        "DnsMax": {
          "type": "integer",
          "title": "DnsMax",
          "order": 3
        },
        "DnsRequests": {
          "type": "integer",
          "title": "DnsRequests",
          "order": 1
        },
        "NetworkMax": {
          "type": "integer",
          "title": "NetworkMax",
          "order": 2
        },
        "NetworkRequests": {
          "type": "integer",
          "title": "NetworkRequests",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
