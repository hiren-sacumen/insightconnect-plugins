# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    EXCLUDED_TARGETS = "excluded_targets"
    ID = "id"
    OVERWRITE = "overwrite"
    

class Output:
    ID = "id"
    LINKS = "links"
    

class UpdateSiteExcludedTargetsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "excluded_targets": {
      "type": "array",
      "title": "Excluded Targets",
      "description": "List of addresses that represent either a hostname, IPv4 address, IPv4 address range, IPv6 address, or CIDR notation",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "id": {
      "type": "integer",
      "title": "Site ID",
      "description": "The identifier of the site",
      "order": 1
    },
    "overwrite": {
      "type": "boolean",
      "title": "Overwrite",
      "description": "Whether to overwrite the excluded targets to the current site or append to the previous list of excluded targets",
      "default": true,
      "order": 3
    }
  },
  "required": [
    "id",
    "overwrite"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateSiteExcludedTargetsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "The identifier of the updated site",
      "order": 1
    },
    "links": {
      "type": "array",
      "title": "Links",
      "description": "Hypermedia links to corresponding or related resources",
      "items": {
        "$ref": "#/definitions/link"
      },
      "order": 2
    }
  },
  "required": [
    "links",
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
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
