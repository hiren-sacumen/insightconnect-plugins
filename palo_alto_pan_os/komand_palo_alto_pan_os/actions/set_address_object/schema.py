# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ADDRESS = "address"
    OBJECT_DESCRIPTION = "object_description"
    OBJECT_NAME = "object_name"
    TAGS = "tags"
    TYPE = "type"
    

class Output:
    CODE = "code"
    MESSAGE = "message"
    STATUS = "status"
    

class SetAddressObjectInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "The IP-Netmask, IP-Range, or FQDN e.g. 192.168.1.0/24, 10.0.0.1-10.0.0.12, google.com",
      "order": 1
    },
    "object_description": {
      "type": "string",
      "title": "Object Description",
      "description": "A description for the address object",
      "order": 4
    },
    "object_name": {
      "type": "string",
      "title": "Object Name",
      "description": "The name of the address object",
      "order": 3
    },
    "tags": {
      "type": "string",
      "title": "Tags",
      "description": "Tags for the address object. Use commas to separate multiple tags",
      "order": 5
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "The type of address object to create",
      "enum": [
        "IP-Netmask",
        "IP-Range",
        "FQDN"
      ],
      "order": 2
    }
  },
  "required": [
    "address",
    "type",
    "object_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SetAddressObjectOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "code": {
      "type": "string",
      "title": "Code",
      "description": "Response code from PAN-OS",
      "order": 2
    },
    "message": {
      "type": "string",
      "title": "Message",
      "description": "A message with more detail about the status",
      "order": 3
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "The status of the requested operation e.g. success, error, etc",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
