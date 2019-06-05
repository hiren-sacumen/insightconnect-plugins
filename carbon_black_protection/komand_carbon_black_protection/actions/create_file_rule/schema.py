# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Creates a file rule, allowing for the creation and editing of file Approvals and Bans"


class Input:
    DESCRIPTION = "description"
    FILE_CATALOG_ID = "file_catalog_id"
    FILE_STATE = "file_state"
    FORCE_INSTALLER = "force_installer"
    FORCE_NOT_INSTALLER = "force_not_installer"
    HASH = "hash"
    NAME = "name"
    PLATFORM_FLAGS = "platform_flags"
    POLICY_IDS = "policy_ids"
    REPORT_ONLY = "report_only"
    REPUTATION_APPROVALS_ENABLED = "reputation_approvals_enabled"
    

class Output:
    FILE_RULE = "file_rule"
    

class CreateFileRuleInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Description of this rule",
      "order": 3
    },
    "file_catalog_id": {
      "type": "integer",
      "title": "File Catalog ID",
      "description": "ID of fileCatalog entry associated with this fileRule. Can be 0 if creating/modifying rule based on hash or file name",
      "order": 1
    },
    "file_state": {
      "type": "string",
      "title": "File State",
      "description": "File state for this rule. Can be one of 1=Unapproved, 2=Approved, 3=Banned",
      "default": 1,
      "enum": [
        "Unapproved",
        "Approved",
        "Banned"
      ],
      "order": 4
    },
    "force_installer": {
      "type": "boolean",
      "title": "Force Installer",
      "description": "True if this file is forced to act as installer, even if product detected it as ‘not installer’",
      "default": false,
      "order": 7
    },
    "force_not_installer": {
      "type": "boolean",
      "title": "Force Not Installer",
      "description": "True if this file is forced to act as ‘not installer’, even if product detected it as installer",
      "default": false,
      "order": 8
    },
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "Hash associated with this rule. This parameter is not required if fileCatalogId is supplied",
      "order": 9
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name of this rule",
      "order": 2
    },
    "platform_flags": {
      "type": "integer",
      "title": "Policy IDs",
      "description": "Comma separated list of platform flags where this file rule will be valid. combination of 1 = Windows, 2 = Mac, 4 = Linux",
      "default": 124,
      "order": 11
    },
    "policy_ids": {
      "type": "string",
      "title": "Policy IDs",
      "description": "Comma separated list of IDs of policies where this rule applies. 0 if this is a global rule",
      "default": "0",
      "order": 10
    },
    "report_only": {
      "type": "boolean",
      "title": "Report Only",
      "description": "Set to true to create a report-only ban. Note - fileState has to be set to 1 (unapproved) before this flag can be set",
      "default": false,
      "order": 5
    },
    "reputation_approvals_enabled": {
      "type": "boolean",
      "title": "Reputation Approvals Enabled",
      "description": "True if reputation approvals are enabled for this file",
      "default": false,
      "order": 6
    }
  },
  "required": [
    "description",
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateFileRuleOutput(komand.Output):
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
