# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DISTINGUISHED_NAME = "distinguished_name"
    

class Output:
    SUCCESS = "success"
    

class DisableUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "distinguished_name": {
      "type": "string",
      "title": "Distinguished Name",
      "description": "The distinguished name of the user to disable e.g. CN=user,OU=domain_users,DC=mydomain,DC=com",
      "order": 1
    }
  },
  "required": [
    "distinguished_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DisableUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Operation status",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
