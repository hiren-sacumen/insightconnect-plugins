# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    FIELD_NAME = "field_name"
    OBJECT_NAME = "object_name"
    RECORD_ID = "record_id"
    

class Output:
    DATA = "data"
    

class GetBlobDataInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "field_name": {
      "type": "string",
      "title": "Field Name",
      "description": "Blob field name",
      "default": "body",
      "order": 3
    },
    "object_name": {
      "type": "string",
      "title": "Object Name",
      "description": "The name of the object (e.g. 'Account')",
      "default": "Attachment",
      "order": 2
    },
    "record_id": {
      "type": "string",
      "title": "Record ID",
      "description": "The ID of an existing record",
      "order": 1
    }
  },
  "required": [
    "record_id",
    "object_name",
    "field_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetBlobDataOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "string",
      "title": "Data",
      "displayType": "bytes",
      "description": "The value of the selected blob field",
      "format": "bytes",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
