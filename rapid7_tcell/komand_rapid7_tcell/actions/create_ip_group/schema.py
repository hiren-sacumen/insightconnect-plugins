# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    GROUP = "group"
    

class Output:
    ID = "id"
    

class CreateIpGroupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "group": {
      "type": "object",
      "title": "Group",
      "description": "IP group definition, containing a name and a list of items, in JSON format",
      "order": 1
    }
  },
  "required": [
    "group"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateIpGroupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "ID of a new IP group",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
