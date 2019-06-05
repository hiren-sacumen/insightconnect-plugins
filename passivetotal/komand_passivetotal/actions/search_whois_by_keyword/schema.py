# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    QUERY = "query"
    

class Output:
    COUNT = "count"
    RESULTS = "results"
    

class SearchWhoisByKeywordInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Input query, e.g. email@passivetotal.org",
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


class SearchWhoisByKeywordOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "count": {
      "type": "integer",
      "title": "Count",
      "description": "Number of results returned",
      "order": 1
    },
    "results": {
      "type": "array",
      "title": "Results",
      "description": "WHOIS Keyword Results",
      "items": {
        "$ref": "#/definitions/whois_keyword_result"
      },
      "order": 2
    }
  },
  "definitions": {
    "whois_keyword_result": {
      "type": "object",
      "title": "whois_keyword_result",
      "properties": {
        "fieldMatch": {
          "type": "string",
          "title": "FieldMatch",
          "order": 3
        },
        "focusPoint": {
          "type": "string",
          "title": "FocusPoint",
          "order": 1
        },
        "matchType": {
          "type": "string",
          "title": "MatchType",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
