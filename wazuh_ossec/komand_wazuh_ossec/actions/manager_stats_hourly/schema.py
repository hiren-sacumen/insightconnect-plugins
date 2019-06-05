# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    pass

class Output:
    AVERAGES = "averages"
    ERROR = "error"
    INTERACTIONS = "interactions"
    

class ManagerStatsHourlyInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ManagerStatsHourlyOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "averages": {
      "type": "array",
      "title": "Averages",
      "description": "Averages",
      "items": {
        "type": "integer"
      },
      "order": 2
    },
    "error": {
      "type": "integer",
      "title": "Error Code",
      "description": "Error code",
      "order": 3
    },
    "interactions": {
      "type": "integer",
      "title": "Interactions",
      "description": "Interactions",
      "order": 1
    }
  },
  "required": [
    "interactions",
    "averages",
    "error"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
