# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Transmit a file for processing and incorporation into the database"


class Input:
    DONATE = "donate"
    FILE = "file"
    

class Output:
    OBSERVER = "observer"
    RESULTS = "results"
    WARNING = "warning"
    

class UploadFileInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "donate": {
      "type": "boolean",
      "title": "Donate",
      "description": "Allow commercial use of the file contents - 'on' to allow",
      "default": true,
      "order": 2
    },
    "file": {
      "$ref": "#/definitions/file",
      "title": "File",
      "description": "File to transmit",
      "order": 1
    }
  },
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UploadFileOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "observer": {
      "type": "string",
      "title": "Observer",
      "description": "Observer",
      "order": 1
    },
    "results": {
      "$ref": "#/definitions/file_upload_results",
      "title": "Results",
      "description": "Results",
      "order": 3
    },
    "warning": {
      "type": "string",
      "title": "Warning",
      "description": "Warning",
      "order": 2
    }
  },
  "required": [
    "results"
  ],
  "definitions": {
    "file_upload_results": {
      "type": "object",
      "title": "file_upload_results",
      "properties": {
        "filename": {
          "type": "string",
          "title": "File Name",
          "order": 3
        },
        "filesize": {
          "type": "integer",
          "title": "File Size",
          "order": 2
        },
        "timeTaken": {
          "type": "string",
          "title": "Time Taken",
          "order": 1
        },
        "transids": {
          "type": "array",
          "title": "Transaction ID",
          "items": {
            "$ref": "#/definitions/file_upload_transid"
          },
          "order": 4
        }
      },
      "required": [
        "filename",
        "filesize",
        "timeTaken",
        "transids"
      ],
      "definitions": {
        "file_upload_transid": {
          "type": "object",
          "title": "file_upload_transid",
          "properties": {
            "file": {
              "type": "string",
              "title": "File",
              "order": 1
            },
            "size": {
              "type": "integer",
              "title": "Size",
              "order": 2
            },
            "transId": {
              "type": "string",
              "title": "Transaction ID",
              "order": 3
            }
          },
          "required": [
            "file",
            "size",
            "transId"
          ]
        }
      }
    },
    "file_upload_transid": {
      "type": "object",
      "title": "file_upload_transid",
      "properties": {
        "file": {
          "type": "string",
          "title": "File",
          "order": 1
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "order": 2
        },
        "transId": {
          "type": "string",
          "title": "Transaction ID",
          "order": 3
        }
      },
      "required": [
        "file",
        "size",
        "transId"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
