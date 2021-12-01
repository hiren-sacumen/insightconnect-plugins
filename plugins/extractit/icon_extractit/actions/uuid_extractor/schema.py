# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Extracts all UUIDs from a string or file"


class Input:
    FILE = "file"
    STR = "str"
    

class Output:
    UUIDS = "uuids"
    

class UuidExtractorInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file": {
      "type": "string",
      "title": "File",
      "displayType": "bytes",
      "description": "Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS",
      "format": "bytes",
      "order": 2
    },
    "str": {
      "type": "string",
      "title": "String",
      "description": "Input string",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UuidExtractorOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "uuids": {
      "type": "array",
      "title": "UUIDs",
      "description": "List of extracted UUIDs",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
