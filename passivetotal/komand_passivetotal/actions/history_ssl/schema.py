# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    QUERY = "query"
    

class Output:
    RESULTS = "results"
    

class HistorySslInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "IP Address or SHA-1 Hash",
      "order": 1
    }
  },
  "required": [
    "query"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class HistorySslOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "array",
      "title": "Results",
      "description": "Results as JSON",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
