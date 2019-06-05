# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    HOST = "host"
    USER = "user"
    

class Output:
    FOUND = "found"
    FULLNAME = "fullname"
    HOME = "home"
    HOMEPHONE = "homephone"
    LOGIN = "login"
    LOGINFROM = "loginfrom"
    LOGINSTATUS = "loginstatus"
    MAIL = "mail"
    MAILSTATUS = "mailstatus"
    PLAN = "plan"
    PROJECT = "project"
    PUBKEY = "pubkey"
    ROOM = "room"
    SHELL = "shell"
    STATUS = "status"
    WORKPHONE = "workphone"
    

class FingerInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Finger server host",
      "order": 2
    },
    "user": {
      "type": "string",
      "title": "User",
      "description": "User",
      "order": 1
    }
  },
  "required": [
    "user",
    "host"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class FingerOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "found": {
      "type": "boolean",
      "title": "Found Status",
      "description": "Found",
      "order": 1
    },
    "fullname": {
      "type": "string",
      "title": "Real Name",
      "description": "Full name",
      "order": 5
    },
    "home": {
      "type": "string",
      "title": "Home Directory",
      "description": "Home",
      "order": 6
    },
    "homephone": {
      "type": "string",
      "title": "Home Phone",
      "description": "Homephone",
      "order": 7
    },
    "login": {
      "type": "string",
      "title": "Login Name",
      "description": "Login",
      "order": 2
    },
    "loginfrom": {
      "type": "string",
      "title": "Login from",
      "description": "Login from",
      "order": 4
    },
    "loginstatus": {
      "type": "string",
      "title": "Login Status",
      "description": "Login Status",
      "order": 3
    },
    "mail": {
      "type": "string",
      "title": "Mail Forward Address",
      "description": "Mail",
      "order": 9
    },
    "mailstatus": {
      "type": "string",
      "title": "Mail Status",
      "description": "Mail status",
      "order": 10
    },
    "plan": {
      "type": "string",
      "title": "Plan",
      "description": "Plan",
      "order": 12
    },
    "project": {
      "type": "string",
      "title": "Project",
      "description": "Project",
      "order": 13
    },
    "pubkey": {
      "type": "string",
      "title": "Public Key File",
      "description": "Public key",
      "order": 11
    },
    "room": {
      "type": "string",
      "title": "Room",
      "description": "Room",
      "order": 14
    },
    "shell": {
      "type": "string",
      "title": "Shell",
      "description": "Shell",
      "order": 8
    },
    "status": {
      "type": "string",
      "title": "Plugin Status",
      "description": "Status",
      "order": 16
    },
    "workphone": {
      "type": "string",
      "title": "Work Phone",
      "description": "Workphone",
      "order": 15
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
