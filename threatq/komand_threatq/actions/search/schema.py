# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    LIMIT = "limit"
    QUERY = "query"
    

class Output:
    RESULTS = "results"
    

class SearchInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Maximum number of records to retrieve",
      "order": 1
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Search query",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "array",
      "title": "Results",
      "description": "Data entries matching query",
      "items": {
        "$ref": "#/definitions/search_result"
      },
      "order": 1
    }
  },
  "definitions": {
    "search_result": {
      "type": "object",
      "title": "search_result",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Object ID",
          "order": 1
        },
        "object": {
          "type": "string",
          "title": "Type of result",
          "description": "Type of object returned",
          "order": 2
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Property of the result that matches the query string",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
