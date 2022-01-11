# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List all New Offenses"


class Input:

    FIELDS = "fields"
    FILTER = "filter"
    INTERVAL = "interval"
    RANGE = "range"
    SORT = "sort"


class Output:

    DATA = "data"


class GetNewOffenseInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        """
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fields": {
      "type": "string",
      "title": "Fields",
      "description": "Use this parameter to specify which fields you would like to get back in the response. Fields that are not named are excluded. Specify subfields in brackets and multiple fields in the same object are separated by commas.",
      "order": 3
    },
    "filter": {
      "type": "string",
      "title": "Filter",
      "description": "This parameter is used to restrict the elements in a list base on the contents of various fields.",
      "order": 2
    },
    "interval": {
      "type": "integer",
      "title": "Interval",
      "description": "How frequently (in seconds) to trigger a greeting",
      "default": 15,
      "order": 5
    },
    "range": {
      "type": "string",
      "title": "Range",
      "description": "Use this parameter to restrict the number of elements that are returned in the list to a specified range. The list is indexed starting at zero.",
      "order": 1
    },
    "sort": {
      "type": "string",
      "title": "Sort",
      "description": "Use parameter to sort the elements in a list.",
      "order": 4
    }
  },
  "required": [
    "interval"
  ]
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetNewOffenseOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        """
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "array",
      "title": "Offense Data",
      "description": "Json Data of the Offense",
      "items": {
        "$ref": "#/definitions/offense"
      },
      "order": 1
    }
  },
  "definitions": {
    "log_sources": {
      "type": "object",
      "title": "log_sources",
      "properties": {
        "id": {
          "type": "integer",
          "title": "Id",
          "description": "Id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "type_id": {
          "type": "integer",
          "title": "Type Id",
          "description": "Type id",
          "order": 3
        },
        "type_name": {
          "type": "string",
          "title": "Type Name",
          "description": "Type name",
          "order": 4
        }
      }
    },
    "offense": {
      "type": "object",
      "title": "offense",
      "properties": {
        "assigned_to": {
          "type": "string",
          "title": "Assigned To",
          "description": "Assigned to",
          "order": 1
        },
        "categories": {
          "type": "array",
          "title": "Categories",
          "description": "Categories",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "category_count": {
          "type": "integer",
          "title": "Category Count",
          "description": "Category count",
          "order": 3
        },
        "close_time": {
          "type": "integer",
          "title": "Close Time",
          "description": "Close time",
          "order": 4
        },
        "closing_reason_id": {
          "type": "integer",
          "title": "Closing Reason Id",
          "description": "Closing reason id",
          "order": 5
        },
        "closing_user": {
          "type": "string",
          "title": "Closing User",
          "description": "Closing user",
          "order": 6
        },
        "credibility": {
          "type": "integer",
          "title": "Credibility",
          "description": "Credibility",
          "order": 7
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 8
        },
        "destination_networks": {
          "type": "array",
          "title": "Destination Networks",
          "description": "Destination networks",
          "items": {
            "type": "string"
          },
          "order": 9
        },
        "device_count": {
          "type": "integer",
          "title": "Device Count",
          "description": "Device count",
          "order": 10
        },
        "domain_id": {
          "type": "integer",
          "title": "Domain Id",
          "description": "Domain id",
          "order": 11
        },
        "event_count": {
          "type": "integer",
          "title": "Event Count",
          "description": "Event count",
          "order": 12
        },
        "first_persisted_time": {
          "type": "integer",
          "title": "First Persisted Time",
          "description": "First persisted time",
          "order": 13
        },
        "flow_count": {
          "type": "integer",
          "title": "Flow Count",
          "description": "Flow count",
          "order": 14
        },
        "follow_up": {
          "type": "boolean",
          "title": "Follow Up",
          "description": "Follow up",
          "order": 15
        },
        "id": {
          "type": "integer",
          "title": "Id",
          "description": "Id",
          "order": 16
        },
        "inactive": {
          "type": "boolean",
          "title": "Inactive",
          "description": "Inactive",
          "order": 17
        },
        "last_persisted_time": {
          "type": "integer",
          "title": "Last Persisted Time",
          "description": "Last persisted time",
          "order": 18
        },
        "last_updated_time": {
          "type": "integer",
          "title": "Last Updated Time",
          "description": "Last updated time",
          "order": 19
        },
        "local_destination_address_ids": {
          "type": "array",
          "title": "Local Destination Address Ids",
          "description": "Local destination address ids",
          "items": {
            "type": "integer"
          },
          "order": 20
        },
        "local_destination_count": {
          "type": "integer",
          "title": "Local Destination Count",
          "description": "Local destination count",
          "order": 21
        },
        "log_sources": {
          "type": "array",
          "title": "Log Sources",
          "description": "Log sources",
          "items": {
            "$ref": "#/definitions/log_sources"
          },
          "order": 22
        },
        "magnitude": {
          "type": "integer",
          "title": "Magnitude",
          "description": "Magnitude",
          "order": 23
        },
        "offense_source": {
          "type": "string",
          "title": "Offense Source",
          "description": "Offense source",
          "order": 24
        },
        "offense_type": {
          "type": "integer",
          "title": "Offense Type",
          "description": "Offense type",
          "order": 25
        },
        "policy_category_count": {
          "type": "integer",
          "title": "Policy Category Count",
          "description": "Policy category count",
          "order": 26
        },
        "protected": {
          "type": "boolean",
          "title": "Protected",
          "description": "Protected",
          "order": 27
        },
        "relevance": {
          "type": "integer",
          "title": "Relevance",
          "description": "Relevance",
          "order": 28
        },
        "remote_destination_count": {
          "type": "integer",
          "title": "Remote Destination Count",
          "description": "Remote destination count",
          "order": 29
        },
        "rules": {
          "type": "array",
          "title": "Rules",
          "description": "Rules",
          "items": {
            "$ref": "#/definitions/rules"
          },
          "order": 30
        },
        "security_category_count": {
          "type": "integer",
          "title": "Security Category Count",
          "description": "Security category count",
          "order": 31
        },
        "severity": {
          "type": "integer",
          "title": "Severity",
          "description": "Severity",
          "order": 32
        },
        "source_address_ids": {
          "type": "array",
          "title": "Source Address Ids",
          "description": "Source address ids",
          "items": {
            "type": "integer"
          },
          "order": 33
        },
        "source_count": {
          "type": "integer",
          "title": "Source Count",
          "description": "Source count",
          "order": 34
        },
        "source_network": {
          "type": "string",
          "title": "Source Network",
          "description": "Source network",
          "order": 35
        },
        "start_time": {
          "type": "integer",
          "title": "Start Time",
          "description": "Start time",
          "order": 36
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 37
        },
        "username_count": {
          "type": "integer",
          "title": "Username Count",
          "description": "Username count",
          "order": 38
        }
      },
      "definitions": {
        "log_sources": {
          "type": "object",
          "title": "log_sources",
          "properties": {
            "id": {
              "type": "integer",
              "title": "Id",
              "description": "Id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "type_id": {
              "type": "integer",
              "title": "Type Id",
              "description": "Type id",
              "order": 3
            },
            "type_name": {
              "type": "string",
              "title": "Type Name",
              "description": "Type name",
              "order": 4
            }
          }
        },
        "rules": {
          "type": "object",
          "title": "rules",
          "properties": {
            "id": {
              "type": "integer",
              "title": "Id",
              "description": "Id",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type",
              "order": 2
            }
          }
        }
      }
    },
    "rules": {
      "type": "object",
      "title": "rules",
      "properties": {
        "id": {
          "type": "integer",
          "title": "Id",
          "description": "Id",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 2
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
