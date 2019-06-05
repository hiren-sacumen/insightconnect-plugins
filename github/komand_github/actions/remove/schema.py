# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Remove user"


class Input:
    ORGANIZATION = "organization"
    REPOSITORY = "repository"
    USERNAME = "username"
    

class Output:
    STATUS = "status"
    

class RemoveInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "organization": {
      "type": "string",
      "title": "Organization",
      "description": "Remove from organization",
      "order": 2
    },
    "repository": {
      "type": "string",
      "title": "Repository",
      "description": "Remove from repository",
      "order": 3
    },
    "username": {
      "type": "string",
      "title": "Username",
      "description": "Username to remove",
      "order": 1
    }
  },
  "required": [
    "username"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemoveOutput(komand.Output):
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
