# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Assign specific user to task"


class Input:
    ID = "id"
    USER = "user"
    

class Output:
    MESSAGE = "message"
    

class AssignInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Task ID",
      "order": 1
    },
    "user": {
      "type": "string",
      "title": "User",
      "description": "User assign to task",
      "order": 2
    }
  },
  "required": [
    "id",
    "user"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AssignOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "When user is assigned message is: User assigned",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
