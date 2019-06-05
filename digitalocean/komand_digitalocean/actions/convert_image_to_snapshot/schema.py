# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    IMAGE_ID = "image_id"
    

class Output:
    SUCCESS = "success"
    

class ConvertImageToSnapshotInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "image_id": {
      "type": "string",
      "title": "Image ID",
      "description": "ID of image to convert to snapshot",
      "order": 1
    }
  },
  "required": [
    "image_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ConvertImageToSnapshotOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Successful",
      "description": "Conversion status. True if successful, false otherwise",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
