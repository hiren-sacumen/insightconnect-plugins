# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ID = "id"
    POLICY_ID = "policy_id"
    

class Output:
    MSG = "msg"
    

class DeleteDataTheftInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "Id",
      "description": "ID of a Data Theft Element",
      "order": 2
    },
    "policy_id": {
      "type": "string",
      "title": "Policy Id",
      "description": "ID of security policy",
      "order": 1
    }
  },
  "required": [
    "policy_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteDataTheftOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "msg": {
      "type": "string",
      "title": "Msg",
      "description": "Message of delete",
      "order": 1
    }
  },
  "required": [
    "msg"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
