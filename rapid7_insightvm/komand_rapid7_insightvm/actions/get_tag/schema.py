# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ID = "id"
    

class Output:
    TAG = "tag"
    

class GetTagInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "Tag ID, e.g. 1",
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


class GetTagOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "tag": {
      "$ref": "#/definitions/tag",
      "title": "Tag",
      "description": "Tag Details",
      "order": 1
    }
  },
  "required": [
    "tag"
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
    "tag": {
      "type": "object",
      "title": "tag",
      "properties": {
        "color": {
          "type": "string",
          "title": "Color",
          "description": "Tag color",
          "order": 1
        },
        "created": {
          "type": "string",
          "title": "Created",
          "displayType": "date",
          "description": "Tag creation date",
          "format": "date-time",
          "order": 2
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Tag ID",
          "order": 3
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Hypermedia links to corresponding or related resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Tag name",
          "order": 5
        },
        "riskModifier": {
          "type": "string",
          "title": "Risk Modifier",
          "description": "Tag risk score modifier",
          "order": 6
        },
        "searchCriteria": {
          "type": "object",
          "title": "Search Criteria",
          "description": "Tag search criteria",
          "order": 7
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Tag source",
          "order": 8
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Tag type",
          "order": 9
        }
      },
      "required": [
        "type",
        "name",
        "id"
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
