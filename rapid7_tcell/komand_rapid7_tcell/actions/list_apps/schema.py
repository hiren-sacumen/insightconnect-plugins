# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    pass

class Output:
    APPS = "apps"
    TOTAL = "total"
    

class ListAppsInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListAppsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "apps": {
      "type": "array",
      "title": "Apps",
      "description": "A list of apps",
      "items": {
        "$ref": "#/definitions/app"
      },
      "order": 1
    },
    "total": {
      "type": "integer",
      "title": "Total",
      "description": "The number of items returned",
      "order": 2
    }
  },
  "definitions": {
    "app": {
      "type": "object",
      "title": "app",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The app ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the app",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
