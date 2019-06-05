# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    APPLICATIONID = "applicationId"
    APPUSER = "appuser"
    

class Output:
    RESULT = "result"
    

class AssignUserToAppSsoInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "applicationId": {
      "type": "string",
      "title": "Application ID",
      "description": "Application ID",
      "order": 1
    },
    "appuser": {
      "type": "object",
      "title": "Application User Model",
      "description": "Application user model as JSON object, see https://developer.okta.com/docs/api/resources/apps#application-user-model",
      "order": 2
    }
  },
  "required": [
    "applicationId"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AssignUserToAppSsoOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "type": "object",
      "title": "Result",
      "description": "Result",
      "order": 1
    }
  },
  "required": [
    "result"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
