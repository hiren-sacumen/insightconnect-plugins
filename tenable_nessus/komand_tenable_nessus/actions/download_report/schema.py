# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    REPORT_FORMAT = "report_format"
    SCAN_NAME = "scan_name"
    

class Output:
    REPORT = "report"
    

class DownloadReportInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "report_format": {
      "type": "string",
      "title": "Report Format",
      "description": "File format of the downloaded report",
      "enum": [
        "nessus",
        "csv",
        "html"
      ],
      "order": 2
    },
    "scan_name": {
      "type": "string",
      "title": "Scan Name",
      "description": "Name of the specified scan",
      "order": 1
    }
  },
  "required": [
    "scan_name",
    "report_format"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DownloadReportOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "report": {
      "type": "string",
      "title": "Report",
      "description": "Text of the returned file",
      "order": 1
    }
  },
  "required": [
    "report"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
