# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    COMMAND = "command"
    HOST = "host"
    

class Output:
    RESULTS = "results"
    

class ShowCommandsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "command": {
      "type": "string",
      "title": "Command",
      "description": "Show command to execute on network device",
      "order": 2
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Optional Host to run remote commands. If not provided, the connection host will be used",
      "order": 1
    }
  },
  "required": [
    "command"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ShowCommandsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "string",
      "title": "Output results",
      "description": "Results",
      "order": 1
    }
  },
  "required": [
    "results"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
