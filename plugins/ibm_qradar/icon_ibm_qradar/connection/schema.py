# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    CREDENTIALS = "credentials"
    HOST_URL = "host_url"
    VERIFY_SSL = "verify_ssl"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        """
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Credentials",
      "description": "Auth object consisting of username of type string and password of type password",
      "order": 2
    },
    "host_url": {
      "type": "string",
      "title": "Host URL",
      "description": "Host URL of the QRadar instance.",
      "order": 1
    },
    "verify_ssl": {
      "type": "boolean",
      "title": "Verify SSL",
      "description": "Whether to verify the SSL for QRadar connection",
      "order": 3
    }
  },
  "required": [
    "credentials",
    "host_url"
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
          "format": "password",
          "order": 2
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with",
          "order": 1
        }
      },
      "required": [
        "username",
        "password"
      ]
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
