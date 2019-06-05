# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    API_KEY = "api_key"
    URL = "url"
    VERIFY_SSL = "verify_ssl"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "API token found in your Carbon Black profile",
      "order": 1
    },
    "url": {
      "type": "string",
      "title": "API URL",
      "description": "Carbon Black Server API URL",
      "default": "https://127.0.0.1/api/bit9platform/v1",
      "order": 2
    },
    "verify_ssl": {
      "type": "boolean",
      "title": "Verify SSL",
      "description": "SSL Certificate Verification",
      "default": true,
      "order": 3
    }
  },
  "required": [
    "url",
    "verify_ssl",
    "api_key"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
