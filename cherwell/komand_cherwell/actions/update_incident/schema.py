# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    BUSINESS_OBJECT_ID = "business_object_id"
    FIELDS_TO_UPDATE = "fields_to_update"
    PUBLIC_ID = "public_id"
    

class Output:
    RAW_RESPONSE = "raw_response"
    SUCCESS = "success"
    

class UpdateIncidentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "business_object_id": {
      "type": "string",
      "title": "Business Object ID",
      "description": "Business Object ID of the incident",
      "order": 1
    },
    "fields_to_update": {
      "type": "object",
      "title": "Fields to Update",
      "description": "A JSON blob of keys and values that are to be updated in the incident e.g. {\\"Status\\", \\"New\\"} will update the Status field of the incident",
      "order": 3
    },
    "public_id": {
      "type": "string",
      "title": "Public ID",
      "description": "Public ID of the incident",
      "order": 2
    }
  },
  "required": [
    "business_object_id",
    "public_id",
    "fields_to_update"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateIncidentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "raw_response": {
      "type": "object",
      "title": "Raw Response",
      "description": "The raw JSON returned by the endpoint",
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Boolean indicating whether the business object was successfully created",
      "order": 1
    }
  },
  "required": [
    "success",
    "raw_response"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
