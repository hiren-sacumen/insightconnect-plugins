# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    IMAGE_ID = "image_id"
    

class Output:
    SUCCESS = "success"
    

class DeleteSnapshotInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "image_id": {
      "type": "string",
      "title": "Snapshot ID",
      "description": "ID of snapshot to delete",
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


class DeleteSnapshotOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Successful",
      "description": "Deletion status. True if successful, false otherwise",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
