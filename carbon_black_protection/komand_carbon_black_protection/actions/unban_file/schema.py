# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Unban file globally or by policy"


class Input:
    HASH = "hash"
    METHOD = "method"
    NEW_STATE = "new_state"
    POLICY_IDS = "policy_ids"
    

class Output:
    FILE_RULE = "file_rule"
    

class UnbanFileInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "Hash for file to unban",
      "order": 2
    },
    "method": {
      "type": "string",
      "title": "Method",
      "description": "Unban globally or by policy",
      "default": "Globally",
      "enum": [
        "Globally",
        "Policy"
      ],
      "order": 4
    },
    "new_state": {
      "type": "string",
      "title": "New State",
      "description": "New state of the file. Either approved or unapproved",
      "default": "Approved",
      "enum": [
        "Approved",
        "Unapproved"
      ],
      "order": 1
    },
    "policy_ids": {
      "type": "array",
      "title": "Policy IDs",
      "description": "List of policy IDs. Only fill in this field if unban is by policy",
      "items": {
        "type": "integer"
      },
      "order": 3
    }
  },
  "required": [
    "hash",
    "method",
    "new_state"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UnbanFileOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file_rule": {
      "$ref": "#/definitions/fileRule",
      "title": "File Rule",
      "description": "Updated file rule",
      "order": 1
    }
  },
  "definitions": {
    "fileRule": {
      "type": "object",
      "title": "fileRule",
      "properties": {
        "clVersion": {
          "type": "integer",
          "title": "CL Version",
          "order": 19
        },
        "createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "User that Created Rule",
          "order": 16
        },
        "dateCreated": {
          "type": "string",
          "title": "Date Created",
          "displayType": "date",
          "description": "Datetime when Rule Created (UTC)",
          "format": "date-time",
          "order": 15
        },
        "dateModified": {
          "type": "string",
          "title": "Date Modified",
          "displayType": "date",
          "description": "Datetime when Rule Last Modified (UTC)",
          "format": "date-time",
          "order": 17
        },
        "description": {
          "type": "string",
          "title": "Description",
          "order": 4
        },
        "fileCatalogId": {
          "type": "integer",
          "title": "File Catlog ID",
          "order": 2
        },
        "fileState": {
          "type": "integer",
          "title": "File State",
          "description": "1=unapproved,2=approved,3=banned",
          "order": 5
        },
        "forceInstaller": {
          "type": "boolean",
          "title": "Force Installer",
          "description": "True if File is Forced to Act as Installer, Even if Product Detected as Not Installer",
          "order": 10
        },
        "forceNotInstaller": {
          "type": "boolean",
          "title": "Force Not Installer",
          "description": "True if File is Forced to Act as Not Installer, Even if Product Detected as Installer",
          "order": 11
        },
        "hash": {
          "type": "string",
          "title": "Hash",
          "description": "Hash Only Available If Rule Created Through MD5 or SHA-1",
          "order": 13
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "order": 1
        },
        "modifiedBy": {
          "type": "string",
          "title": "Modified By",
          "description": "User that Last Modified Rule",
          "order": 18
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 3
        },
        "platformFlags": {
          "type": "integer",
          "title": "Platform Flags",
          "description": "1=Windows,2=Mac,3=Linux",
          "order": 14
        },
        "policyIds": {
          "type": "string",
          "title": "Policy IDs",
          "description": "List of IDs of Policies where Rule Applies, 0 if Global",
          "order": 12
        },
        "reportOnly": {
          "type": "boolean",
          "title": "Report Only",
          "description": "True if this Has a Report-Only Ban",
          "order": 8
        },
        "reputationApprovalsEnabled": {
          "type": "boolean",
          "title": "Reputation Approvals Enabled",
          "description": "True if Reputation Approvals Are Enabled",
          "order": 9
        },
        "sourceId": {
          "type": "integer",
          "title": "Source ID",
          "description": "Can Be Event Rule ID or Trusted Directory ID",
          "order": 7
        },
        "sourceType": {
          "type": "integer",
          "title": "Source Type",
          "description": "Mechanism that Created Rule",
          "order": 6
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
