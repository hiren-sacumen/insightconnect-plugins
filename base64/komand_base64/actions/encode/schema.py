# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Encode data to Base64"


class Input:
    CONTENT = "content"
    

class Output:
    DATA = "data"
    

class EncodeInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "content": {
      "type": "string",
      "title": "Content",
      "description": "Data to encode",
      "order": 1
    }
  },
  "required": [
    "content"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EncodeOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "string",
      "title": "Encoded Data",
      "displayType": "bytes",
      "description": "Encoded data result",
      "format": "bytes",
      "order": 1
    }
  },
  "required": [
    "data"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
