# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Extract text from PDF file"


class Input:
    CONTENTS = "contents"
    

class Output:
    OUTPUT = "output"
    

class ExtractTextInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "contents": {
      "type": "string",
      "title": "PDF File",
      "displayType": "bytes",
      "description": "PDF file to extract text from",
      "format": "bytes",
      "order": 1
    }
  },
  "required": [
    "contents"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ExtractTextOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "output": {
      "type": "string",
      "title": "PDF Text",
      "description": "Text extracted from PDF file",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
