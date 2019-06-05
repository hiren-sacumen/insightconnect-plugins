# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    API_KEY = "api_key"
    SSL_VERIFY = "ssl_verify"
    URL = "url"
    USERNAME = "username"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "Anomali ThreatStream API key",
      "order": 3
    },
    "ssl_verify": {
      "type": "boolean",
      "title": "SSL Verify",
      "description": "Verify the server's SSL/TLS certificate",
      "default": true,
      "order": 4
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL for the ThreatStream instance e.g. https://ts.example.com",
      "order": 2
    },
    "username": {
      "type": "string",
      "title": "Username",
      "description": "Anomali ThreatStream username",
      "order": 1
    }
  },
  "required": [
    "username",
    "url",
    "api_key",
    "ssl_verify"
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
