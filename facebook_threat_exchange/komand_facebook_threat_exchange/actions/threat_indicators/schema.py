# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    LIMIT = "limit"
    SINCE = "since"
    SORT_BY = "sort_by"
    SORT_ORDER = "sort_order"
    STRICT_TEXT = "strict_text"
    TEXT = "text"
    THREAT_TYPE = "threat_type"
    TYPE = "type"
    UNTIL = "until"
    

class Output:
    DATA = "data"
    FIELDS = "fields"
    PAGING = "paging"
    

class ThreatIndicatorsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "limit": {
      "type": "string",
      "title": "Limit",
      "description": "Defines the maximum size of a page of results. The maximum is 1,000",
      "order": 1
    },
    "since": {
      "type": "string",
      "title": "Since",
      "displayType": "date",
      "description": "Returns indicators collected after a timestamp",
      "format": "date-time",
      "order": 8
    },
    "sort_by": {
      "type": "string",
      "title": "Sort By",
      "description": "Sort results by Relevance, create_time ",
      "enum": [
        "RELEVANCE",
        "CREATE_Time"
      ],
      "order": 4
    },
    "sort_order": {
      "type": "string",
      "title": "Sort Order",
      "description": "Sorts responses by ascending or descending",
      "enum": [
        "ASCENDING",
        "DESCENDING"
      ],
      "order": 3
    },
    "strict_text": {
      "type": "boolean",
      "title": "Strict Text",
      "description": "When set to 'true', the API will not do approximate matching on the value in text",
      "default": false,
      "order": 5
    },
    "text": {
      "type": "string",
      "title": "Text",
      "description": "Freeform text field with a value to search for. This can be a file hash or a string found in other fields of the objects",
      "order": 2
    },
    "threat_type": {
      "type": "string",
      "title": "Threat Type",
      "description": "The broad threat type the indicator is associated with",
      "enum": [
        "",
        "ADJUST_TOKEN",
        "API_KEY",
        "AS_NUMBER",
        "BANNER",
        "CMD_LINE",
        "COOKIE_NAME",
        "CRX",
        "DEBUG_STRING",
        "DEST_PORT",
        "DIRECTORY_QUERIED",
        "DOMAIN",
        "EMAIL_ADDRESS",
        "FILE_CREATED",
        "FILE_DELETED",
        "FILE_MOVED",
        "FILE_NAME",
        "FILE_OPENED",
        "FILE_READ",
        "FILE_WRITTEN",
        "GET_PARAM",
        "HASH_IMPHASH",
        "HASH_MD5",
        "HASH_SHA1",
        "HASH_SHA256",
        "HASH_SSDEEP",
        "HTML_ID",
        "HTTP_REQUEST",
        "IP_ADDRESS",
        "IP_SUBNET",
        "ISP",
        "LATITUDE",
        "LAUNCH_AGENT",
        "LOCATION",
        "LONGITUDE",
        "MALWARE_NAME",
        "MEMORY_ALLOC",
        "MEMORY_PROTECT",
        "MEMORY_WRITTEN",
        "MUTANT_CREATED",
        "MUTEX",
        "NAME_SERVER",
        "OTHER_FILE_OP",
        "PASSWORD",
        "PASSWORD_SALT",
        "PAYLOAD_DATA",
        "PAYLOAD_TYPE",
        "POST_DATA",
        "PROTOCOL",
        "REFERER",
        "REGISTRAR",
        "REGISTRY_KEY",
        "REG_KEY_CREATED",
        "REG_KEY_DELETED",
        "REG_KEY_ENUMERATED",
        "REG_KEY_MONITORED",
        "REG_KEY_OPENED",
        "REG_KEY_VALUE_CREATED",
        "REG_KEY_VALUE_DELETED",
        "REG_KEY_VALUE_MODIFIED",
        "REG_KEY_VALUE_QUERIED",
        "SIGNATURE",
        "SOURCE_PORT",
        "TELEPHONE",
        "URI",
        "USER_AGENT",
        "VOLUME_QUERIED",
        "WEBSTORAGE_KEY",
        "WEB_PAYLOAD",
        "WHOIS_NAME",
        "WHOIS_ADDR1",
        "WHOIS_ADDR2",
        "XPI"
      ],
      "order": 6
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "The type of indicators to search for IndicatorTypes",
      "enum": [
        "",
        "ADJUST_TOKEN",
        "API_KEY",
        "AS_NUMBER",
        "BANNER",
        "CMD_LINE",
        "COOKIE_NAME",
        "CRX",
        "DEBUG_STRING",
        "DEST_PORT",
        "DIRECTORY_QUERIED",
        "DOMAIN",
        "EMAIL_ADDRESS",
        "FILE_CREATED",
        "FILE_DELETED",
        "FILE_MOVED",
        "FILE_NAME",
        "FILE_OPENED",
        "FILE_READ",
        "FILE_WRITTEN",
        "GET_PARAM",
        "HASH_IMPHASH",
        "HASH_MD5",
        "HASH_SHA1",
        "HASH_SHA256",
        "HASH_SSDEEP",
        "HTML_ID",
        "HTTP_REQUEST",
        "IP_ADDRESS",
        "IP_SUBNET",
        "ISP",
        "LATITUDE",
        "LAUNCH_AGENT",
        "LOCATION",
        "LONGITUDE",
        "MALWARE_NAME",
        "MEMORY_ALLOC",
        "MEMORY_PROTECT",
        "MEMORY_WRITTEN",
        "MUTANT_CREATED",
        "MUTEX",
        "NAME_SERVER",
        "OTHER_FILE_OP",
        "PASSWORD",
        "PASSWORD_SALT",
        "PAYLOAD_DATA",
        "PAYLOAD_TYPE",
        "POST_DATA",
        "PROTOCOL",
        "REFERER",
        "REGISTRAR",
        "REGISTRY_KEY",
        "REG_KEY_CREATED",
        "REG_KEY_DELETED",
        "REG_KEY_ENUMERATED",
        "REG_KEY_MONITORED",
        "REG_KEY_OPENED",
        "REG_KEY_VALUE_CREATED",
        "REG_KEY_VALUE_DELETED",
        "REG_KEY_VALUE_MODIFIED",
        "REG_KEY_VALUE_QUERIED",
        "SIGNATURE",
        "SOURCE_PORT",
        "TELEPHONE",
        "URI",
        "USER_AGENT",
        "VOLUME_QUERIED",
        "WEBSTORAGE_KEY",
        "WEB_PAYLOAD",
        "WHOIS_NAME",
        "WHOIS_ADDR1",
        "WHOIS_ADDR2",
        "XPI"
      ],
      "order": 7
    },
    "until": {
      "type": "string",
      "title": "Until",
      "displayType": "date",
      "description": "Returns indicators collected before a timestamp",
      "format": "date-time",
      "order": 9
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ThreatIndicatorsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "array",
      "title": "Data",
      "description": "Information around the indicator such as the Indicator, Type and ID",
      "items": {
        "$ref": "#/definitions/data"
      },
      "order": 3
    },
    "fields": {
      "type": "array",
      "title": "Fields",
      "description": "A list of fields to return in the response",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "paging": {
      "$ref": "#/definitions/paging",
      "title": "Paging",
      "description": "Paging information",
      "order": 2
    }
  },
  "required": [
    "paging",
    "data"
  ],
  "definitions": {
    "cursors": {
      "type": "object",
      "title": "cursors",
      "properties": {
        "after": {
          "type": "string",
          "title": "After",
          "description": "End of page",
          "order": 1
        },
        "before": {
          "type": "string",
          "title": "Before",
          "description": "Start of page",
          "order": 2
        }
      }
    },
    "data": {
      "type": "object",
      "title": "data",
      "properties": {
        "id": {
          "type": "string",
          "title": "Indicator IP",
          "description": "Indicator ID",
          "order": 1
        },
        "indicator": {
          "type": "string",
          "title": "Indicator",
          "description": "IP Address",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Indicator Type",
          "description": "Type of Indicator",
          "order": 3
        }
      }
    },
    "paging": {
      "type": "object",
      "title": "paging",
      "properties": {
        "cursors": {
          "$ref": "#/definitions/cursors",
          "title": "Cursor",
          "description": "Start and end of the page",
          "order": 1
        },
        "next": {
          "type": "string",
          "title": "Next Result",
          "description": "Next result",
          "order": 2
        }
      },
      "definitions": {
        "cursors": {
          "type": "object",
          "title": "cursors",
          "properties": {
            "after": {
              "type": "string",
              "title": "After",
              "description": "End of page",
              "order": 1
            },
            "before": {
              "type": "string",
              "title": "Before",
              "description": "Start of page",
              "order": 2
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
