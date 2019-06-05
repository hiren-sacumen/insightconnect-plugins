# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    SCAN_ID = "scan_id"
    

class Output:
    MESSAGE = "message"
    REPORT = "report"
    SUCCESS = "success"
    

class GetReportHtmlInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_id": {
      "type": "string",
      "title": "Scan ID",
      "description": "Scan ID E.g. 9a849831-23a0-48ba-8e8f-a3deeaa45f7e",
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


class GetReportHtmlOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message",
      "order": 3
    },
    "report": {
      "type": "string",
      "title": "Report",
      "description": "HTML output of report",
      "order": 1
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
