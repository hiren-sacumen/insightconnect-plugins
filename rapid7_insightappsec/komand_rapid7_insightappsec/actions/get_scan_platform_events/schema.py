# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    SCAN_ID = "scan_id"
    

class Output:
    EVENTS = "events"
    

class GetScanPlatformEventsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_id": {
      "type": "string",
      "title": "Scan ID",
      "description": "Scan UUID",
      "order": 1
    }
  },
  "required": [
    "scan_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetScanPlatformEventsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "events": {
      "type": "array",
      "title": "Events",
      "description": "An array of event logs and their dates",
      "items": {
        "$ref": "#/definitions/event_log"
      },
      "order": 1
    }
  },
  "definitions": {
    "event_log": {
      "type": "object",
      "title": "event_log",
      "properties": {
        "event": {
          "type": "string",
          "title": "Event",
          "description": "The log event",
          "order": 2
        },
        "time": {
          "type": "string",
          "title": "Time",
          "displayType": "date",
          "description": "The time at which the log event occurred",
          "format": "date-time",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
