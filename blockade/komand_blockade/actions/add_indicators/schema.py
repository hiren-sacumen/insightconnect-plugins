# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    INDICATORS = "indicators"
    

class Output:
    MESSAGE = "message"
    SUCCESS = "success"
    WRITECOUNT = "writeCount"
    

class AddIndicatorsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "indicators": {
      "type": "array",
      "title": "Indicators",
      "description": "Indicators as array e.g. [ \\"c9867172dca8b07d06566c78c7265ff2\\", \\"8f55ea93778722e32403b0c961295aed\\" ]",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddIndicatorsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message",
      "order": 1
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
      "order": 2
    },
    "writeCount": {
      "type": "integer",
      "title": "WriteCount",
      "description": "Write count",
      "order": 3
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
