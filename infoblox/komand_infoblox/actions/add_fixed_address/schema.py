# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ADDRESS = "address"
    

class Output:
    _REF = "_ref"
    

class AddFixedAddressInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "$ref": "#/definitions/FixedAddressCreate",
      "title": "Address",
      "description": "New fixed address data",
      "order": 1
    }
  },
  "required": [
    "address"
  ],
  "definitions": {
    "FixedAddressCreate": {
      "type": "object",
      "title": "FixedAddressCreate",
      "properties": {
        "ipv4addr": {
          "type": "string",
          "title": "IPv4 Address",
          "description": "Either an IP address or a function (e.g. func:nextavailableip:10.1.1.0/24)",
          "order": 1
        },
        "mac": {
          "type": "string",
          "title": "MAC",
          "description": "MAC address",
          "order": 2
        }
      },
      "required": [
        "ipv4addr",
        "mac"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddFixedAddressOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "_ref": {
      "type": "string",
      "title": "Ref",
      "description": "Object Reference of a newly added fixed address",
      "order": 1
    }
  },
  "required": [
    "_ref"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
