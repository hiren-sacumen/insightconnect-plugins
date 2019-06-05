# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    EVENT = "event"
    HOST = "host"
    INDEX = "index"
    SOURCE = "source"
    SOURCETYPE = "sourcetype"
    

class Output:
    pass

class InsertInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "event": {
      "type": "string",
      "title": "Event",
      "description": "The event to submit",
      "order": 2
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "The source host, e.g. localhost or 192.168.2.2",
      "order": 3
    },
    "index": {
      "type": "string",
      "title": "Index",
      "description": "Name of index",
      "order": 1
    },
    "source": {
      "type": "string",
      "title": "Source",
      "description": "Source of the event (e.g., /var/log/syslog)",
      "order": 4
    },
    "sourcetype": {
      "type": "string",
      "title": "Sourcetype",
      "description": "The optional source type value of the event (e.g. access_combined, syslog)",
      "order": 5
    }
  },
  "required": [
    "index",
    "event"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class InsertOutput(komand.Output):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
