# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Add an email address or domain to a group"


class Input:
    DOMAIN = "domain"
    EMAIL_ADDRESS = "email_address"
    ID = "id"
    

class Output:
    EMAIL_ADDRESS = "email_address"
    FOLDER_ID = "folder_id"
    ID = "id"
    INTERNAL = "internal"
    

class AddGroupMemberInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "A domain to add to a group. Use either emailAddress or domain",
      "order": 3
    },
    "email_address": {
      "type": "string",
      "title": "Email Address",
      "description": "The email address of a user to add to a group. Use either emailAddress or domain",
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The Mimecast ID of the group to add to",
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


class AddGroupMemberOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "email_address": {
      "type": "string",
      "title": "Email Address",
      "description": "The email address of the user that was added to the group",
      "order": 2
    },
    "folder_id": {
      "type": "string",
      "title": "Folder ID",
      "description": "The Mimecast ID of the group that the user / domain was added to",
      "order": 1
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The Mimecast ID of the user / domain that was added to the group",
      "order": 3
    },
    "internal": {
      "type": "boolean",
      "title": "Internal",
      "description": "If the user / doamin is internal or not",
      "order": 4
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
