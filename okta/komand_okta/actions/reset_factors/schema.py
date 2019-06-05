# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    EMAIL = "email"
    

class Output:
    EMAIL = "email"
    SUCCESS = "success"
    USER_ID = "user_id"
    

class ResetFactorsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "email": {
      "type": "string",
      "title": "Okta User Email",
      "description": "The email of the employee to reset factors",
      "order": 1
    }
  },
  "required": [
    "email"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ResetFactorsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "email": {
      "type": "string",
      "title": "Okta User Email",
      "description": "The email of the Okta user",
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether the reset was successful",
      "order": 1
    },
    "user_id": {
      "type": "string",
      "title": "Okta User ID",
      "description": "The user ID of the Okta user",
      "order": 3
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
