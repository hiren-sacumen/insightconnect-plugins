# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a new target in the OpenVAS server"


class Input:
    HOST_LIST = "host_list"
    NAME = "name"
    PORT_LIST_ID = "port_list_id"
    

class Output:
    MESSAGE = "message"
    SUCCESS = "success"
    TARGET_ID = "target_id"
    

class CreateTargetInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "host_list": {
      "type": "array",
      "title": "Target IP List",
      "description": "Target IP List, in the form of a JSON array for each host or list of hosts. CIDR notation can be used. For example, the following would be a valid list: ['192.168.0.101', '192.168.1.101,192.168.1.103,192.168.1.105','192.168.1.2/24','192.168.3.105-112']",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Target Name",
      "description": "Target Name",
      "order": 1
    },
    "port_list_id": {
      "type": "string",
      "title": "Port List ID",
      "description": "ID of the Port List to use for scanning, if you want to scan a custom list of ports",
      "order": 3
    }
  },
  "required": [
    "host_list",
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateTargetOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message",
      "order": 3
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
      "order": 2
    },
    "target_id": {
      "type": "string",
      "title": "Target ID",
      "description": "Target ID",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
