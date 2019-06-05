# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ASSET_ID = "asset_id"
    TAG_ID = "tag_id"
    

class Output:
    LINKS = "links"
    

class RemoveAssetTagInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_id": {
      "type": "integer",
      "title": "Asset ID",
      "description": "Asset ID from which to remove the tag",
      "order": 1
    },
    "tag_id": {
      "type": "integer",
      "title": "Tag ID",
      "description": "Tag ID to remove from the asset",
      "order": 2
    }
  },
  "required": [
    "asset_id",
    "tag_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemoveAssetTagOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "links": {
      "type": "array",
      "title": "Links",
      "description": "Hypermedia links to corresponding or related resources",
      "items": {
        "$ref": "#/definitions/link"
      },
      "order": 1
    }
  },
  "required": [
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
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
