# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Pass the given JSON to the jq command, using the given flags and filter"


class Input:
    FILTER = "filter"
    FLAGS = "flags"
    JSON_IN = "json_in"
    TIMEOUT = "timeout"
    

class Output:
    JSON_OUT = "json_out"
    

class RunJqInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filter": {
      "type": "string",
      "title": "Filter",
      "description": "Filter expression to be used by the jq command not in surrounding quotes",
      "order": 3
    },
    "flags": {
      "type": "array",
      "title": "Flags",
      "description": "Flags with which to invoke the jq command (e.g. -c)",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "json_in": {
      "type": "object",
      "title": "JSON Input",
      "description": "Data in JSON format to be passed to jq",
      "order": 1
    },
    "timeout": {
      "type": "integer",
      "title": "Timeout",
      "description": "Timeout in seconds during which the jq command runs",
      "default": 15,
      "order": 4
    }
  },
  "required": [
    "filter",
    "json_in"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RunJqOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "json_out": {
      "type": "string",
      "title": "JSON Out",
      "description": "The output JSON",
      "order": 1
    }
  },
  "required": [
    "json_out"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
