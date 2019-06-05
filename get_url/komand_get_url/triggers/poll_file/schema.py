# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    
    IS_VERIFY = "is_verify"
    POLL = "poll"
    URL = "url"
    

class Output:
    
    BYTES = "bytes"
    STATUS_CODE = "status_code"
    

class PollFileInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "is_verify": {
      "type": "boolean",
      "title": "Is Verify",
      "description": "Validate certificate",
      "default": true,
      "order": 3
    },
    "poll": {
      "type": "integer",
      "title": "Poll",
      "description": "Poll in seconds",
      "default": 60,
      "order": 2
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL to Download",
      "order": 1
    }
  },
  "required": [
    "url",
    "is_verify"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PollFileOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "bytes": {
      "type": "string",
      "title": "Base64 Encoded File",
      "displayType": "bytes",
      "description": "Bytes",
      "format": "bytes",
      "order": 1
    },
    "status_code": {
      "type": "integer",
      "title": "Status Codes",
      "description": "Status code",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
