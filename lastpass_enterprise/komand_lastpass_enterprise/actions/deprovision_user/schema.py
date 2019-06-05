# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Remove, delete, or deactivate a user"


class Input:
    DELETE_ACTION = "delete_action"
    USER_NAME = "user_name"
    

class Output:
    STATUS = "status"
    

class DeprovisionUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "delete_action": {
      "type": "string",
      "title": "Delete Action",
      "description": "Delete action",
      "enum": [
        "deactivate",
        "remove",
        "delete"
      ],
      "order": 2
    },
    "user_name": {
      "type": "string",
      "title": "User Name",
      "description": "User name to delete",
      "order": 1
    }
  },
  "required": [
    "delete_action",
    "user_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeprovisionUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
