# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    _REF = "_ref"
    

class Output:
    _REF = "_ref"
    

class DeleteHostInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "_ref": {
      "type": "string",
      "title": "Ref",
      "description": "Object Reference of the host to remove",
      "order": 1
    }
  },
  "required": [
    "_ref"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteHostOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "_ref": {
      "type": "string",
      "title": "Ref",
      "description": "Object Reference of the removed host",
      "order": 1
    }
  },
  "required": [
    "_ref"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
