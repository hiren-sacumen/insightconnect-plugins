# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    HOST = "host"
    PORT = "port"
    USE_SSL = "use_ssl"
    USERNAME_PASSWORD = "username_password"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Server Host, e.g. ldap://192.5.5.5. Must use either ldap:// or ldaps:// for SSL prefix",
      "order": 1
    },
    "port": {
      "type": "integer",
      "title": "Port",
      "description": "Port, e.g. 389",
      "default": 389,
      "order": 2
    },
    "use_ssl": {
      "type": "boolean",
      "title": "Use SSL",
      "description": "Use SSL?",
      "order": 3
    },
    "username_password": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Username and Password",
      "description": "Username and password",
      "order": 4
    }
  },
  "required": [
    "use_ssl",
    "username_password",
    "host",
    "port"
  ],
  "definitions": {
    "credential_username_password": {
      "id": "credential_username_password",
      "type": "object",
      "title": "Credential: Username and Password",
      "description": "A username and password combination",
      "properties": {
        "password": {
          "type": "string",
          "title": "Password",
          "displayType": "password",
          "description": "The password",
          "format": "password"
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with"
        }
      },
      "required": [
        "username",
        "password"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
