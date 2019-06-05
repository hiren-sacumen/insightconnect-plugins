# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    pass

class Output:
    NEW_ELEMENTS = "new_elements"
    

class NewInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class NewOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "new_elements": {
      "type": "array",
      "title": "New elements",
      "description": "All elements listed as Hippocampe/new",
      "items": {
        "$ref": "#/definitions/new_element"
      },
      "order": 1
    }
  },
  "required": [
    "new_elements"
  ],
  "definitions": {
    "new_element": {
      "type": "object",
      "title": "new_element",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "toSearch": {
          "type": "string",
          "title": "To Search",
          "description": "Search resource",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
