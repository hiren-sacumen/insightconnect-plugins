# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DOC = "doc"
    

class Output:
    MARKDOWN_CONTENTS = "markdown_contents"
    MARKDOWN_FILE = "markdown_file"
    

class MarkdownInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "doc": {
      "type": "string",
      "title": "Document",
      "description": "Document to transform",
      "order": 1
    }
  },
  "required": [
    "doc"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MarkdownOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "markdown_contents": {
      "type": "string",
      "title": "Contents",
      "description": "Markdown Contents",
      "order": 1
    },
    "markdown_file": {
      "type": "string",
      "title": "File",
      "displayType": "bytes",
      "description": "Markdown File",
      "format": "bytes",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
