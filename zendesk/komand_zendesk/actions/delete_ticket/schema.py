# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    TICKET_ID = "ticket_id"
    

class Output:
    STATUS = "status"
    

class DeleteTicketInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ticket_id": {
      "type": "string",
      "title": "Delete Ticket",
      "description": "Delete ticket",
      "order": 1
    }
  },
  "required": [
    "ticket_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteTicketOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "boolean",
      "title": "Status",
      "description": "Success or failure",
      "order": 1
    }
  },
  "required": [
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
