# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    
    NUMBER_OF_MESSAGES = "number_of_messages"
    PROJECT_ID = "project_id"
    SUBSCRIPTION = "subscription"
    

class Output:
    
    MESSAGES = "messages"
    

class SubscriptionInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "number_of_messages": {
      "type": "integer",
      "title": "Number of Messages",
      "description": "The number of messages to return at one time as a list. Must be 1 or more",
      "default": 1,
      "order": 3
    },
    "project_id": {
      "type": "string",
      "title": "Project ID",
      "description": "The project ID for the subscription e.g. subpub-1528163449245",
      "order": 2
    },
    "subscription": {
      "type": "string",
      "title": "Subscription",
      "description": "The subscription to pull from",
      "order": 1
    }
  },
  "required": [
    "subscription",
    "project_id",
    "number_of_messages"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SubscriptionOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "messages": {
      "type": "array",
      "title": "Messages",
      "description": "Messages found in the subscription",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
