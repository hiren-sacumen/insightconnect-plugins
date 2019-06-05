# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CC = "cc"
    CONFIDENCE = "confidence"
    ITYPES = "itypes"
    LIMIT = "limit"
    NOLOG = "nolog"
    OBSERVABLE = "observable"
    OTYPE = "otype"
    PORTLIST = "portlist"
    PROTOCOL = "protocol"
    PROVIDER = "provider"
    Q = "q"
    TAGS = "tags"
    

class Output:
    QUERY = "query"
    

class QueryInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cc": {
      "type": "string",
      "title": "Country Code",
      "description": "The country code to filter on e.g. us",
      "order": 6
    },
    "confidence": {
      "type": "integer",
      "title": "Confidence",
      "description": "Minimum confidence level to return e.g. 65",
      "default": 65,
      "order": 5
    },
    "itypes": {
      "type": "string",
      "title": "Itypes",
      "description": "Itypes",
      "default": "",
      "enum": [
        "ipv4",
        "ipv6",
        "fqdn",
        "url",
        "email",
        "md5",
        "sha1",
        "sha256"
      ],
      "order": 12
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Limit number of results",
      "default": 10,
      "order": 11
    },
    "nolog": {
      "type": "boolean",
      "title": "No Log",
      "description": "Whether CIF should log the query",
      "order": 4
    },
    "observable": {
      "type": "string",
      "title": "Observable",
      "description": "The observable to query for",
      "order": 2
    },
    "otype": {
      "type": "string",
      "title": "Type",
      "description": "Type of observable",
      "enum": [
        "all",
        "ipv4",
        "ipv6",
        "fqdn",
        "url",
        "email"
      ],
      "order": 3
    },
    "portlist": {
      "type": "string",
      "title": "Ports",
      "description": "List of ports (ex: 1,2,445-557)",
      "order": 8
    },
    "protocol": {
      "type": "string",
      "title": "Protocol",
      "description": "Layer 4 protocol (icmp, tcp, udp)",
      "enum": [
        "all",
        "icmp",
        "tcp",
        "udp"
      ],
      "order": 7
    },
    "provider": {
      "type": "string",
      "title": "Provider",
      "description": "The provider(s) to filter on e.g. dragonresearchgroup.com",
      "order": 9
    },
    "q": {
      "type": "string",
      "title": "Query",
      "description": "The observable to query for",
      "order": 1
    },
    "tags": {
      "type": "string",
      "title": "Tags",
      "description": "The tag(s) to filter on e.g. tags=botnet,zeus",
      "order": 10
    }
  },
  "required": [
    "limit",
    "nolog",
    "otype",
    "confidence"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QueryOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "array",
      "title": "Query Results",
      "description": "Query Results",
      "items": {
        "$ref": "#/definitions/result"
      },
      "order": 1
    }
  },
  "definitions": {
    "peers": {
      "type": "object",
      "title": "peers",
      "properties": {
        "asn": {
          "type": "string",
          "title": "ASN",
          "description": "ANS",
          "order": 1
        },
        "asn_description": {
          "type": "string",
          "title": "ASN Description",
          "description": "ANS description",
          "order": 2
        },
        "cc": {
          "type": "string",
          "title": "Country Code",
          "description": "Country code",
          "order": 3
        },
        "date": {
          "type": "string",
          "title": "Date",
          "description": "Date",
          "order": 4
        },
        "prefix": {
          "type": "string",
          "title": "Prefix",
          "description": "Prefix",
          "order": 5
        },
        "rir": {
          "type": "string",
          "title": "RIR",
          "description": "RIR",
          "order": 6
        }
      }
    },
    "result": {
      "type": "object",
      "title": "result",
      "properties": {
        "altid": {
          "type": "string",
          "title": "Alt ID",
          "description": "Alt ID",
          "order": 11
        },
        "altid_tlp": {
          "type": "string",
          "title": "Alt ID TLP",
          "description": "Alt ID TLP",
          "order": 19
        },
        "application": {
          "type": "array",
          "title": "Application",
          "description": "Application",
          "items": {
            "type": "string"
          },
          "order": 12
        },
        "asn": {
          "type": "string",
          "title": "ASN",
          "description": "ASN",
          "order": 24
        },
        "asn_desc": {
          "type": "string",
          "title": "ASN Desc",
          "description": "ASN Desc",
          "order": 13
        },
        "cc": {
          "type": "string",
          "title": "Country Code",
          "description": "Country code",
          "order": 3
        },
        "citycode": {
          "type": "string",
          "title": "City Code",
          "description": "City code",
          "order": 9
        },
        "confidence": {
          "type": "number",
          "title": "Confidence",
          "description": "Confidence",
          "order": 20
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 16
        },
        "firsttime": {
          "type": "string",
          "title": "First Time",
          "description": "First time",
          "order": 22
        },
        "geolocation": {
          "type": "string",
          "title": "Geolocation",
          "description": "Geolocation",
          "order": 1
        },
        "group": {
          "type": "array",
          "title": "Group",
          "description": "Group",
          "items": {
            "type": "string"
          },
          "order": 10
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 8
        },
        "lang": {
          "type": "string",
          "title": "Lang",
          "description": "Lang",
          "order": 25
        },
        "lasttime": {
          "type": "string",
          "title": "Last Time",
          "description": "Last Time",
          "order": 23
        },
        "latitude": {
          "type": "string",
          "title": "Latitude",
          "description": "Latitude",
          "order": 15
        },
        "longitude": {
          "type": "string",
          "title": "Longitude",
          "description": "Logitude",
          "order": 30
        },
        "observable": {
          "type": "string",
          "title": "Observable",
          "description": "Observable",
          "order": 26
        },
        "otype": {
          "type": "string",
          "title": "O Type",
          "description": "O type",
          "order": 31
        },
        "peers": {
          "type": "array",
          "title": "Peers",
          "description": "Peers",
          "items": {
            "$ref": "#/definitions/peers"
          },
          "order": 27
        },
        "portlist": {
          "type": "string",
          "title": "Portlist",
          "description": "Portlist",
          "order": 18
        },
        "prefix": {
          "type": "string",
          "title": "Prefix",
          "description": "Prefix",
          "order": 6
        },
        "protocol": {
          "type": "integer",
          "title": "Protocol",
          "description": "Protocol",
          "order": 2
        },
        "provider": {
          "type": "string",
          "title": "Provider",
          "description": "Provider",
          "order": 14
        },
        "rdata": {
          "type": "array",
          "title": "rdata",
          "description": "rdata",
          "items": {
            "type": "string"
          },
          "order": 21
        },
        "related": {
          "type": "string",
          "title": "Related",
          "description": "Related",
          "order": 5
        },
        "rir": {
          "type": "string",
          "title": "RIR",
          "description": "RIR",
          "order": 4
        },
        "subdivision": {
          "type": "string",
          "title": "Subdivision",
          "description": "Subdivision",
          "order": 29
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags",
          "items": {
            "type": "string"
          },
          "order": 17
        },
        "timezone": {
          "type": "string",
          "title": "Timezone",
          "description": "Timezone",
          "order": 7
        },
        "tlp": {
          "type": "string",
          "title": "TLP",
          "description": "TLP",
          "order": 28
        }
      },
      "definitions": {
        "peers": {
          "type": "object",
          "title": "peers",
          "properties": {
            "asn": {
              "type": "string",
              "title": "ASN",
              "description": "ANS",
              "order": 1
            },
            "asn_description": {
              "type": "string",
              "title": "ASN Description",
              "description": "ANS description",
              "order": 2
            },
            "cc": {
              "type": "string",
              "title": "Country Code",
              "description": "Country code",
              "order": 3
            },
            "date": {
              "type": "string",
              "title": "Date",
              "description": "Date",
              "order": 4
            },
            "prefix": {
              "type": "string",
              "title": "Prefix",
              "description": "Prefix",
              "order": 5
            },
            "rir": {
              "type": "string",
              "title": "RIR",
              "description": "RIR",
              "order": 6
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
