# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DAYS_BACK = "days_back"
    PAGE = "page"
    QUERY = "query"
    

class Output:
    RESPONSE = "response"
    

class IpMonitorInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "days_back": {
      "type": "integer",
      "title": "Days Back",
      "description": "Use this parameter when you need to search domain changes up to six days prior to the current date",
      "default": 0,
      "enum": [
        0,
        1,
        2,
        3,
        4,
        5,
        6
      ],
      "order": 2
    },
    "page": {
      "type": "integer",
      "title": "Page",
      "description": "If the result set is larger than 1000 records for a given day, request additional pages with this parameter",
      "default": 1,
      "order": 3
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "The IP Address you wish to query (i.e. 65.55.53.233)",
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


class IpMonitorOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/ip_monitor_response",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "definitions": {
    "ip_monitor_response": {
      "type": "object",
      "title": "ip_monitor_response",
      "properties": {
        "alerts": {
          "type": "array",
          "title": "Alerts",
          "items": {
            "type": "object"
          },
          "order": 1
        },
        "date": {
          "type": "string",
          "title": "Date",
          "order": 2
        },
        "ip_address": {
          "type": "string",
          "title": "Ip Address",
          "order": 3
        },
        "limit": {
          "type": "integer",
          "title": "Limit",
          "order": 4
        },
        "page": {
          "type": "integer",
          "title": "Page",
          "order": 5
        },
        "page_count": {
          "type": "integer",
          "title": "Page Count",
          "order": 6
        },
        "total": {
          "type": "string",
          "title": "Total",
          "order": 7
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
