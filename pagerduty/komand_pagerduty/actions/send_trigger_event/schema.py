# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CLIENT = "client"
    CLIENT_URL = "client_url"
    CONTEXTS = "contexts"
    DESCRIPTION = "description"
    DETAILS = "details"
    SERVICE_KEY = "service_key"
    

class Output:
    INCIDENT_KEY = "incident_key"
    MESSAGE = "message"
    STATUS = "status"
    

class SendTriggerEventInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "client": {
      "type": "string",
      "title": "Client",
      "description": "The name of the monitoring client that is triggering this event",
      "order": 4
    },
    "client_url": {
      "type": "string",
      "title": "Client URL",
      "description": "The URL of the monitoring client that is triggering this event",
      "order": 5
    },
    "contexts": {
      "type": "array",
      "title": "Contexts",
      "description": "Additional context objects",
      "items": {
        "type": "object"
      },
      "order": 6
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Text that will appear in the incident's log associated with this event",
      "order": 2
    },
    "details": {
      "type": "object",
      "title": "Details",
      "description": "An arbitrary JSON object containing any data you'd like included in the incident log",
      "order": 3
    },
    "service_key": {
      "type": "string",
      "title": "Service Key",
      "description": "Service Key (aka Integration Key)",
      "order": 1
    }
  },
  "required": [
    "description"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SendTriggerEventOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incident_key": {
      "type": "string",
      "title": "Incident Key",
      "description": "Incident Key",
      "order": 3
    },
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message",
      "order": 2
    },
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
