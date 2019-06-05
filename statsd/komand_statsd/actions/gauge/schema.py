# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DELTA = "delta"
    RATE = "rate"
    STAT = "stat"
    VALUE = "value"
    

class Output:
    STAT = "stat"
    VALUE = "value"
    

class GaugeInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "delta": {
      "type": "boolean",
      "title": "Delta value",
      "description": "Whether or not to consider this a delta value or an absolute value",
      "default": false,
      "order": 4
    },
    "rate": {
      "type": "number",
      "title": "Sample rate",
      "description": "A sample rate e.g. 1. Default is 1",
      "order": 3
    },
    "stat": {
      "type": "string",
      "title": "Gauge name",
      "description": "The name of the gauge to set",
      "order": 1
    },
    "value": {
      "type": "integer",
      "title": "Value",
      "description": "The current value of the gauge",
      "order": 2
    }
  },
  "required": [
    "stat",
    "value"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GaugeOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "stat": {
      "type": "string",
      "title": "Stat",
      "description": "The name of the set gauge",
      "order": 1
    },
    "value": {
      "type": "integer",
      "title": "Value",
      "description": "The current value of the gauge",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
