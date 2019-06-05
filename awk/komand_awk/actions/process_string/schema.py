# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    EXPRESSION = "expression"
    TEXT = "text"
    

class Output:
    OUT = "out"
    

class ProcessStringInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "expression": {
      "type": "string",
      "title": "Expression",
      "description": "Awk expression e.g. [pattern] { action }",
      "order": 1
    },
    "text": {
      "type": "string",
      "title": "Text",
      "description": "String to process",
      "order": 2
    }
  },
  "required": [
    "expression",
    "text"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ProcessStringOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "out": {
      "type": "string",
      "title": "Out",
      "description": "Processed string",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
