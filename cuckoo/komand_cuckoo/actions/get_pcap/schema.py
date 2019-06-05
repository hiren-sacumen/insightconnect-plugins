# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Returns the content of the PCAP associated with the given task"


class Input:
    TASK_ID = "task_id"
    

class Output:
    CONTENTS = "contents"
    

class GetPcapInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "task_id": {
      "type": "integer",
      "title": "Task ID",
      "description": "Task ID",
      "order": 1
    }
  },
  "required": [
    "task_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetPcapOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "contents": {
      "type": "string",
      "title": "Contents",
      "displayType": "bytes",
      "description": "PCAP contents",
      "format": "bytes",
      "order": 1
    }
  },
  "required": [
    "contents"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
