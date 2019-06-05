# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    HTML_CONTENTS = "html_contents"
    

class Output:
    VALIDATED = "validated"
    

class ValidateInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "html_contents": {
      "type": "string",
      "title": "Contents",
      "description": "HTML Contents",
      "order": 1
    }
  },
  "required": [
    "html_contents"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ValidateOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "validated": {
      "type": "boolean",
      "title": "Is Validated",
      "description": "HTML Syntax Validation Status",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
