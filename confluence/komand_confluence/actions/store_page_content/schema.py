# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CONTENT = "content"
    PAGE = "page"
    SPACE = "space"
    

class Output:
    PAGE = "page"
    

class StorePageContentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "content": {
      "type": "string",
      "title": "Content",
      "description": "Content To Store",
      "order": 3
    },
    "page": {
      "type": "string",
      "title": "Page",
      "description": "Page Name",
      "order": 1
    },
    "space": {
      "type": "string",
      "title": "Space",
      "description": "Space",
      "order": 2
    }
  },
  "required": [
    "content",
    "page",
    "space"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class StorePageContentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "page": {
      "$ref": "#/definitions/page",
      "title": "Page",
      "description": "Page Stored",
      "order": 1
    }
  },
  "definitions": {
    "page": {
      "type": "object",
      "title": "page",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "Page Content",
          "order": 5
        },
        "contentStatus": {
          "type": "string",
          "title": "ContentStatus",
          "description": "Content Status",
          "order": 14
        },
        "created": {
          "type": "string",
          "title": "Created",
          "displayType": "date",
          "description": "Created Date",
          "format": "date-time",
          "order": 4
        },
        "creator": {
          "type": "string",
          "title": "Creator",
          "description": "Creator User",
          "order": 8
        },
        "current": {
          "type": "boolean",
          "title": "Current",
          "description": "True if current verison",
          "order": 13
        },
        "homePage": {
          "type": "boolean",
          "title": "HomePage",
          "description": "Home Page",
          "order": 11
        },
        "id": {
          "type": "string",
          "title": "Id",
          "description": "Page ID",
          "order": 12
        },
        "modified": {
          "type": "string",
          "title": "Modified",
          "displayType": "date",
          "description": "Modified Date",
          "format": "date-time",
          "order": 15
        },
        "modifier": {
          "type": "string",
          "title": "Modifier",
          "description": "Modifier User",
          "order": 3
        },
        "parentId": {
          "type": "string",
          "title": "ParentId",
          "description": "Parent Page ID",
          "order": 9
        },
        "permissions": {
          "type": "string",
          "title": "Permissions",
          "description": "Permissions",
          "order": 7
        },
        "space": {
          "type": "string",
          "title": "Space",
          "description": "Space",
          "order": 2
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Page Title",
          "order": 1
        },
        "url": {
          "type": "string",
          "title": "Url",
          "description": "URL",
          "order": 6
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Page Version",
          "order": 10
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
