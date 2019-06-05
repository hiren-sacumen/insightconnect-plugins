# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    FILE_PATH = "file_path"
    SHARE_NAME = "share_name"
    TIMEOUT = "timeout"
    

class Output:
    DELETED = "deleted"
    

class DeleteFileInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file_path": {
      "type": "string",
      "title": "File Path",
      "description": "Path of the file to delete",
      "order": 2
    },
    "share_name": {
      "type": "string",
      "title": "Share Name",
      "description": "Name of the SMB share",
      "order": 1
    },
    "timeout": {
      "type": "integer",
      "title": "Timeout",
      "description": "Request timeout of operation in seconds",
      "default": 30,
      "order": 3
    }
  },
  "required": [
    "share_name",
    "file_path"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteFileOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "deleted": {
      "type": "boolean",
      "title": "Deleted",
      "description": "Deletion success",
      "order": 1
    }
  },
  "required": [
    "deleted"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
