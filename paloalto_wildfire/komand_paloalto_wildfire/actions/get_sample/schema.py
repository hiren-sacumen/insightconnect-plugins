# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    HASH = "hash"
    

class Output:
    FILE = "file"
    

class GetSampleInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "The MD5 or SHA‐256 hash value of the sample",
      "order": 1
    }
  },
  "required": [
    "hash"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetSampleOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file": {
      "type": "string",
      "title": "File",
      "displayType": "bytes",
      "description": "File",
      "format": "bytes",
      "order": 1
    }
  },
  "required": [
    "file"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
