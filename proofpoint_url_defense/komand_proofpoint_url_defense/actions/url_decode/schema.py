# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ENCODED_URL = "encoded_url"
    

class Output:
    DECODED_URL = "decoded_url"
    

class UrlDecodeInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "encoded_url": {
      "type": "string",
      "title": "Encoded URL",
      "description": "Proofpoint encoded URL or URL parameters e.g http-3A__www.example.org_url\\u0026d=BwdwBAg\\u0026c=TIwfCwdwWnrHy3gMA_uzZorHPsT2wfwvKrwfU",
      "order": 1
    }
  },
  "required": [
    "encoded_url"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UrlDecodeOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "decoded_url": {
      "type": "string",
      "title": "Decoded Proofpoint URL",
      "description": "Decoded Proofpoint URL",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
