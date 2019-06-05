# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ID = "id"
    

class Output:
    SCAN_ENGINE_POOL = "scan_engine_pool"
    

class GetScanEnginePoolInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "Scan engine pool identifier",
      "order": 1
    }
  },
  "required": [
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetScanEnginePoolOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_engine_pool": {
      "$ref": "#/definitions/scan_engine_pool",
      "title": "Scan Engine Pool",
      "description": "Scan engine pool details",
      "order": 1
    }
  },
  "required": [
    "scan_engine_pool"
  ],
  "definitions": {
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "URL",
          "description": "A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Link relation type following RFC 5988",
          "order": 2
        }
      }
    },
    "scan_engine_pool": {
      "type": "object",
      "title": "scan_engine_pool",
      "properties": {
        "engines": {
          "type": "array",
          "title": "Engines",
          "description": "List of scan engine IDs associated with the scan engine pool",
          "items": {
            "type": "integer"
          },
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Scan engine pool identifier",
          "order": 2
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "List of hypermedia links to corresponding resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Scan engine pool name",
          "order": 1
        }
      },
      "required": [
        "name",
        "id",
        "engines",
        "links"
      ],
      "definitions": {
        "link": {
          "type": "object",
          "title": "link",
          "properties": {
            "href": {
              "type": "string",
              "title": "URL",
              "description": "A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)",
              "order": 1
            },
            "rel": {
              "type": "string",
              "title": "Rel",
              "description": "Link relation type following RFC 5988",
              "order": 2
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
