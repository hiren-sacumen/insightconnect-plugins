# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    USER_ID = "user_id"
    

class Output:
    MEMBERSHIPS = "memberships"
    

class ShowMembershipsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_id": {
      "type": "string",
      "title": "User ID",
      "description": "ID of user to show E.g. 20444826487",
      "order": 1
    }
  },
  "required": [
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ShowMembershipsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "memberships": {
      "type": "array",
      "title": "Memberships",
      "description": "Members data",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  },
  "required": [
    "memberships"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
