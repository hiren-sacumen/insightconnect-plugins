# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    NAME = "name"
    

class Output:
    ROLES = "roles"
    

class GetRolesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Role name by which to filter, accepts regular expression patterns",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetRolesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "roles": {
      "type": "array",
      "title": "Roles",
      "description": "List of roles",
      "items": {
        "$ref": "#/definitions/role"
      },
      "order": 1
    }
  },
  "required": [
    "roles"
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
    "role": {
      "type": "object",
      "title": "role",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "The description of the role",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "Id",
          "description": "ID of the role, e.g 'global-admin'",
          "order": 2
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "List of hypermedia links to corresponding or related resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the role",
          "order": 4
        },
        "privileges": {
          "type": "array",
          "title": "Privileges",
          "description": "List of privileges assigned to the role",
          "items": {
            "type": "string"
          },
          "order": 5
        }
      },
      "required": [
        "links",
        "name",
        "privileges",
        "description",
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
