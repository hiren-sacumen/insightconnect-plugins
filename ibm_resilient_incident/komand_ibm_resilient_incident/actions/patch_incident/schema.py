# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    INCIDENT_ID = "incident_id"
    ORGANIZATION_ID = "organization_id"
    PATCH = "patch"
    

class Output:
    PATCH_STATUS = "patch_status"
    

class PatchIncidentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incident_id": {
      "type": "number",
      "title": "Incident ID",
      "description": "The incident ID",
      "order": 2
    },
    "organization_id": {
      "type": "number",
      "title": "Organization ID",
      "description": "The organization ID",
      "order": 1
    },
    "patch": {
      "type": "object",
      "title": "Patch",
      "description": "The incident properties to update, in JSON format. Please see the PatchDTO JSON reference in your Resilient API documentation",
      "order": 3
    }
  },
  "required": [
    "organization_id",
    "incident_id",
    "patch"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PatchIncidentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "patch_status": {
      "$ref": "#/definitions/PatchStatusDTO",
      "title": "Patch Status",
      "description": "Patch status",
      "order": 1
    }
  },
  "definitions": {
    "FieldPatchFailureDTO": {
      "type": "object",
      "title": "FieldPatchFailureDTO",
      "properties": {
        "actual_current_value": {
          "type": "object",
          "title": "Actual Current Value",
          "order": 3
        },
        "field": {
          "type": "object",
          "title": "Field",
          "order": 1
        },
        "your_original_value": {
          "type": "object",
          "title": "Your Original Value",
          "order": 2
        }
      }
    },
    "PatchStatusDTO": {
      "type": "object",
      "title": "PatchStatusDTO",
      "properties": {
        "field_failure": {
          "type": "array",
          "title": "Field Failure",
          "items": {
            "$ref": "#/definitions/FieldPatchFailureDTO"
          },
          "order": 1
        },
        "hints": {
          "type": "array",
          "title": "Hints",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "message": {
          "type": "string",
          "title": "Message",
          "order": 4
        },
        "success": {
          "type": "boolean",
          "title": "Success",
          "order": 2
        },
        "title": {
          "type": "string",
          "title": "Title",
          "order": 3
        }
      },
      "definitions": {
        "FieldPatchFailureDTO": {
          "type": "object",
          "title": "FieldPatchFailureDTO",
          "properties": {
            "actual_current_value": {
              "type": "object",
              "title": "Actual Current Value",
              "order": 3
            },
            "field": {
              "type": "object",
              "title": "Field",
              "order": 1
            },
            "your_original_value": {
              "type": "object",
              "title": "Your Original Value",
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
