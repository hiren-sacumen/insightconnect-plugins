# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Define the SAST scan settings according to a project (preset and engine configuration)"


class Input:
    EMAILNOTIFICATIONS = "emailNotifications"
    ENGINECONFIGURATIONID = "engineConfigurationId"
    PRESETID = "presetId"
    PROJECTID = "projectId"
    

class Output:
    ID = "id"
    LINK = "link"
    

class DefineScanSettingsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "emailNotifications": {
      "$ref": "#/definitions/email_notifications",
      "title": "Email Notifications",
      "description": "Email notification details",
      "order": 4
    },
    "engineConfigurationId": {
      "type": "integer",
      "title": "Engine Configuration ID",
      "description": "Unique ID of the engine configuration",
      "order": 3
    },
    "presetId": {
      "type": "integer",
      "title": "Preset ID",
      "description": "Unique ID of the preset",
      "order": 2
    },
    "projectId": {
      "type": "integer",
      "title": "Project ID",
      "description": "Unique ID of the project",
      "order": 1
    }
  },
  "required": [
    "engineConfigurationId",
    "presetId",
    "projectId"
  ],
  "definitions": {
    "email_notifications": {
      "type": "object",
      "title": "email_notifications",
      "properties": {
        "afterScans": {
          "type": "string",
          "title": "Failed Scans",
          "description": "Specifies the email to send the post-scan message",
          "order": 3
        },
        "beforeScan": {
          "type": "string",
          "title": "Before Scan",
          "description": "Specifies the email to send the pre-scan message",
          "order": 1
        },
        "failedScans": {
          "type": "string",
          "title": "Failed Scans",
          "description": "Specifies the email to send the scan failure message",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DefineScanSettingsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "ID of the created scan settings",
      "order": 1
    },
    "link": {
      "$ref": "#/definitions/link",
      "title": "Link",
      "description": "Metadata about the scan settings",
      "order": 2
    }
  },
  "definitions": {
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Relation of the link",
          "order": 1
        },
        "uri": {
          "type": "string",
          "title": "URI",
          "description": "Relative URL of the project",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
