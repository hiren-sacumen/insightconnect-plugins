# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    FEATURES = "features"
    FILE_DIGEST = "file_digest"
    FILE_DIGEST_TYPE = "file_digest_type"
    FILE_NAME = "file_name"
    FILE_TYPE = "file_type"
    QUOTA = "quota"
    

class Output:
    FOUND = "found"
    QUERY_RESPONSE = "query_response"
    

class QueryReportInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "features": {
      "type": "string",
      "title": "Features",
      "description": "Features",
      "order": 5
    },
    "file_digest": {
      "type": "string",
      "title": "File Digest",
      "description": "Hash of the file",
      "order": 1
    },
    "file_digest_type": {
      "type": "string",
      "title": "File Digest Type",
      "description": "The type of hash used for the digest",
      "enum": [
        "md5",
        "sha1",
        "sha2"
      ],
      "order": 2
    },
    "file_name": {
      "type": "string",
      "title": "File Name",
      "description": "File name",
      "order": 4
    },
    "file_type": {
      "type": "string",
      "title": "File Type",
      "description": "The file extension",
      "order": 3
    },
    "quota": {
      "type": "boolean",
      "title": "Quota",
      "description": "Quota",
      "order": 6
    }
  },
  "required": [
    "file_digest",
    "file_digest_type"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QueryReportOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Returns true if file found",
      "order": 2
    },
    "query_response": {
      "type": "object",
      "title": "Query Response",
      "description": "Status of requested features",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
