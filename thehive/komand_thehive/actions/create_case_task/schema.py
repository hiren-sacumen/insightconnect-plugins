# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a new case task"


class Input:
    ID = "id"
    TASK = "task"
    

class Output:
    CASE = "case"
    

class CreateCaseTaskInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "Case ID",
      "description": "Case ID e.g. AV_ajI_oYMfcbXhqb9tS",
      "order": 1
    },
    "task": {
      "$ref": "#/definitions/itask",
      "title": "Task",
      "description": "Task name",
      "order": 2
    }
  },
  "required": [
    "id",
    "task"
  ],
  "definitions": {
    "itask": {
      "type": "object",
      "title": "itask",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Task description",
          "order": 4
        },
        "flag": {
          "type": "boolean",
          "title": "Flag",
          "description": "Task flag, default is false",
          "default": false,
          "order": 3
        },
        "owner": {
          "type": "string",
          "title": "Owner",
          "description": "Task owner",
          "order": 5
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Task status",
          "default": "Waiting",
          "enum": [
            "Waiting",
            "InProgress",
            "Completed",
            "Cancel"
          ],
          "order": 2
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Task title",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateCaseTaskOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "case": {
      "$ref": "#/definitions/task",
      "title": "Case",
      "description": "Create case task output",
      "order": 1
    }
  },
  "definitions": {
    "task": {
      "type": "object",
      "title": "task",
      "properties": {
        "_type": {
          "type": "string",
          "title": "Type",
          "description": "Task type",
          "order": 3
        },
        "createdAt": {
          "type": "integer",
          "title": "Created At",
          "description": "Task created at",
          "order": 12
        },
        "createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "Task created by",
          "order": 9
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Task description",
          "order": 4
        },
        "flag": {
          "type": "boolean",
          "title": "Flag",
          "description": "Task flag",
          "order": 7
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Task ID",
          "order": 6
        },
        "order": {
          "type": "integer",
          "title": "Order",
          "description": "Task order",
          "order": 11
        },
        "owner": {
          "type": "string",
          "title": "Owner",
          "description": "Task owner",
          "order": 10
        },
        "startDate": {
          "type": "integer",
          "title": "Start Date",
          "description": "Task start date",
          "order": 2
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Task status",
          "enum": [
            "Waiting",
            "InProgress",
            "Completed",
            "Cancel"
          ],
          "order": 1
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Task title",
          "order": 5
        },
        "user": {
          "type": "string",
          "title": "User",
          "description": "Task user",
          "order": 8
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
