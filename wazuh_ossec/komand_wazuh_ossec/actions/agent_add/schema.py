# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    FORCE = "force"
    IP = "ip"
    NAME = "name"
    

class Output:
    ERROR = "error"
    ID = "id"
    

class AgentAddInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "force": {
      "type": "string",
      "title": "Force",
      "description": "Remove old agent with same IP if disconnected since force seconds",
      "order": 3
    },
    "ip": {
      "type": "string",
      "title": "IP Address",
      "description": "If you do not include this param, the API will get the IP automatically. If you are behind a proxy, you must set the option config.BehindProxyServer to yes at config.js",
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Agent name",
      "order": 1
    }
  },
  "required": [
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AgentAddOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "error": {
      "type": "integer",
      "title": "Error Code",
      "description": "Error code",
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "Agend ID",
      "description": "Agent ID",
      "order": 1
    }
  },
  "required": [
    "id",
    "error"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
