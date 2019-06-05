# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    
    ASSIGNEE = "assignee"
    COMPONENT = "component"
    KIND = "kind"
    MILESTONE = "milestone"
    POLL = "poll"
    PRIORITY = "priority"
    REPOSITORY = "repository"
    STATE = "state"
    VERSION = "version"
    

class Output:
    
    ISSUES = "issues"
    

class IssueInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "assignee": {
      "type": "string",
      "title": "Assignee",
      "description": "Assignee username",
      "order": 6
    },
    "component": {
      "type": "string",
      "title": "Component",
      "description": "Component name",
      "order": 5
    },
    "kind": {
      "type": "string",
      "title": "Kind",
      "description": "Kind e.g. bug, proposal, etc",
      "enum": [
        "None",
        "Bug",
        "Enhancement",
        "Proposal",
        "Task"
      ],
      "order": 3
    },
    "milestone": {
      "type": "string",
      "title": "Milestone",
      "description": "Milestone name",
      "order": 8
    },
    "poll": {
      "type": "integer",
      "title": "Poll Interval",
      "description": "Poll interval in seconds",
      "order": 9
    },
    "priority": {
      "type": "string",
      "title": "Priority",
      "description": "Priority e.g. major, critical, etc",
      "enum": [
        "None",
        "Trivial",
        "Minor",
        "Major",
        "Critical",
        "Blocker"
      ],
      "order": 2
    },
    "repository": {
      "type": "string",
      "title": "Repository",
      "description": "Return issues of a specific repository",
      "order": 1
    },
    "state": {
      "type": "string",
      "title": "State",
      "description": "State e.g. open, resolved, etc",
      "enum": [
        "None",
        "New",
        "Open",
        "Resolved",
        "On hold",
        "Invalid",
        "Duplicate",
        "Wontfix",
        "Closed"
      ],
      "order": 4
    },
    "version": {
      "type": "string",
      "title": "Version",
      "description": "Version name",
      "order": 7
    }
  },
  "required": [
    "repository"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class IssueOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "issues": {
      "type": "array",
      "title": "Issues",
      "description": "Issues",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
