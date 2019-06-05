# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    pass

class Output:
    QUEUESIZE = "queuesize"
    

class GetServerInfoInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetServerInfoOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "queuesize": {
      "type": "integer",
      "title": "Queue Size",
      "description": "Queue size",
      "order": 1
    }
  },
  "required": [
    "queuesize"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
