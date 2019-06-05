# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ALERT_ID = "alert_id"
    

class Output:
    FILE_INFORMATION = "file_information"
    

class GetFileIdFromAlertIdInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert_id": {
      "type": "string",
      "title": "Alert ID",
      "description": "Alert ID to get files from",
      "order": 1
    }
  },
  "required": [
    "alert_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetFileIdFromAlertIdOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file_information": {
      "$ref": "#/definitions/file_information",
      "title": "File Information",
      "description": "The file ID related to the given alert ID",
      "order": 1
    }
  },
  "required": [
    "file_information"
  ],
  "definitions": {
    "file_information": {
      "type": "object",
      "title": "file_information",
      "properties": {
        "@odata.context": {
          "type": "string",
          "title": "OData Context",
          "description": "OData context",
          "order": 2
        },
        "file_list": {
          "type": "array",
          "title": "File List",
          "description": "List of file information entities",
          "items": {
            "$ref": "#/definitions/file_list_entry"
          },
          "order": 1
        }
      },
      "definitions": {
        "file_list_entry": {
          "type": "object",
          "title": "file_list_entry",
          "properties": {
            "fileProductName": {
              "type": "string",
              "title": "File Product Name",
              "description": "File product name",
              "order": 1
            },
            "filePublisher": {
              "type": "string",
              "title": "File Publisher",
              "description": "File publisher",
              "order": 2
            },
            "fileType": {
              "type": "string",
              "title": "File Type",
              "description": "File type",
              "order": 3
            },
            "globalFirstObserved": {
              "type": "string",
              "title": "Global First Observed",
              "description": "Global first observed",
              "order": 4
            },
            "globalLastObserved": {
              "type": "string",
              "title": "Global Last Observed",
              "description": "Global last observed",
              "order": 5
            },
            "globalPrevalence": {
              "type": "integer",
              "title": "Global Prevalence",
              "description": "Global prevalence",
              "order": 6
            },
            "isPeFile": {
              "type": "boolean",
              "title": "Is PE File",
              "description": "Is PE file",
              "order": 7
            },
            "isValidCertificate": {
              "type": "boolean",
              "title": "Is Valid Certificate",
              "description": "Is valid certificate",
              "order": 8
            },
            "issuer": {
              "type": "string",
              "title": "Issuer",
              "description": "Issuer",
              "order": 9
            },
            "md5": {
              "type": "string",
              "title": "MD5",
              "description": "MD5",
              "order": 10
            },
            "sha1": {
              "type": "string",
              "title": "SHA1",
              "description": "SHA1",
              "order": 11
            },
            "sha256": {
              "type": "string",
              "title": "SHA256",
              "description": "SHA256",
              "order": 12
            },
            "signer": {
              "type": "string",
              "title": "Signer",
              "description": "Signer",
              "order": 13
            },
            "signerHash": {
              "type": "string",
              "title": "Signer Hash",
              "description": "Signer hash",
              "order": 14
            },
            "size": {
              "type": "integer",
              "title": "Size",
              "description": "Size",
              "order": 15
            },
            "windowsDefenderAVThreatName": {
              "type": "string",
              "title": "Windows Defender AV Threat Name",
              "description": "Windows Defender AV threat name",
              "order": 16
            }
          }
        }
      }
    },
    "file_list_entry": {
      "type": "object",
      "title": "file_list_entry",
      "properties": {
        "fileProductName": {
          "type": "string",
          "title": "File Product Name",
          "description": "File product name",
          "order": 1
        },
        "filePublisher": {
          "type": "string",
          "title": "File Publisher",
          "description": "File publisher",
          "order": 2
        },
        "fileType": {
          "type": "string",
          "title": "File Type",
          "description": "File type",
          "order": 3
        },
        "globalFirstObserved": {
          "type": "string",
          "title": "Global First Observed",
          "description": "Global first observed",
          "order": 4
        },
        "globalLastObserved": {
          "type": "string",
          "title": "Global Last Observed",
          "description": "Global last observed",
          "order": 5
        },
        "globalPrevalence": {
          "type": "integer",
          "title": "Global Prevalence",
          "description": "Global prevalence",
          "order": 6
        },
        "isPeFile": {
          "type": "boolean",
          "title": "Is PE File",
          "description": "Is PE file",
          "order": 7
        },
        "isValidCertificate": {
          "type": "boolean",
          "title": "Is Valid Certificate",
          "description": "Is valid certificate",
          "order": 8
        },
        "issuer": {
          "type": "string",
          "title": "Issuer",
          "description": "Issuer",
          "order": 9
        },
        "md5": {
          "type": "string",
          "title": "MD5",
          "description": "MD5",
          "order": 10
        },
        "sha1": {
          "type": "string",
          "title": "SHA1",
          "description": "SHA1",
          "order": 11
        },
        "sha256": {
          "type": "string",
          "title": "SHA256",
          "description": "SHA256",
          "order": 12
        },
        "signer": {
          "type": "string",
          "title": "Signer",
          "description": "Signer",
          "order": 13
        },
        "signerHash": {
          "type": "string",
          "title": "Signer Hash",
          "description": "Signer hash",
          "order": 14
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "Size",
          "order": 15
        },
        "windowsDefenderAVThreatName": {
          "type": "string",
          "title": "Windows Defender AV Threat Name",
          "description": "Windows Defender AV threat name",
          "order": 16
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
