# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DESCRIPTION = "description"
    HAS_ISSUES = "has_issues"
    HAS_WIKI = "has_wiki"
    IS_PRIVATE = "is_private"
    TITLE = "title"
    TYPE = "type"
    

class Output:
    REPOSITORY = "repository"
    

class CreateRepoInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Description of repository",
      "order": 2
    },
    "has_issues": {
      "type": "boolean",
      "title": "Has Issues",
      "description": "Add issue tracker",
      "default": true,
      "order": 3
    },
    "has_wiki": {
      "type": "boolean",
      "title": "Has Wiki",
      "description": "Has wiki",
      "default": false,
      "order": 6
    },
    "is_private": {
      "type": "boolean",
      "title": "Is Private",
      "description": "Repository is private",
      "default": false,
      "order": 4
    },
    "title": {
      "type": "string",
      "title": "Title",
      "description": "Title of repository",
      "order": 1
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Repo type e.g. Git, Mercurial, etc",
      "default": "Git",
      "enum": [
        "Hg",
        "Git"
      ],
      "order": 5
    }
  },
  "required": [
    "title"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateRepoOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "repository": {
      "type": "object",
      "title": "Repository",
      "description": "Repository",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
