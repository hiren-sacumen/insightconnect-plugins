# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    BASE_TIME = "base_time"
    DAYS = "days"
    HOURS = "hours"
    MINUTES = "minutes"
    MONTHS = "months"
    SECONDS = "seconds"
    YEARS = "years"
    

class Output:
    DATE = "date"
    

class AddToDatetimeInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "base_time": {
      "type": "string",
      "title": "Base Time",
      "displayType": "date",
      "description": "Datetime with which to add to",
      "format": "date-time",
      "order": 1
    },
    "days": {
      "type": "integer",
      "title": "Days",
      "description": "How many days to add to the specified Datetime",
      "default": 0,
      "order": 4
    },
    "hours": {
      "type": "integer",
      "title": "Hours",
      "description": "How many hours to add to the specified Datetime",
      "default": 0,
      "order": 5
    },
    "minutes": {
      "type": "integer",
      "title": "Minutes",
      "description": "How many minutes to add to the specified Datetime",
      "default": 0,
      "order": 6
    },
    "months": {
      "type": "integer",
      "title": "Months",
      "description": "How many months to add to the specified Datetime",
      "default": 0,
      "order": 3
    },
    "seconds": {
      "type": "integer",
      "title": "Seconds",
      "description": "How many seconds to add to the specified Datetime",
      "default": 0,
      "order": 7
    },
    "years": {
      "type": "integer",
      "title": "Years",
      "description": "How many years to add to the specified Datetime",
      "default": 0,
      "order": 2
    }
  },
  "required": [
    "base_time",
    "years",
    "months",
    "days",
    "hours",
    "minutes",
    "seconds"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddToDatetimeOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "date": {
      "type": "string",
      "title": "Date",
      "displayType": "date",
      "description": "The Datetime after addition",
      "format": "date-time",
      "order": 1
    }
  },
  "required": [
    "date"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
