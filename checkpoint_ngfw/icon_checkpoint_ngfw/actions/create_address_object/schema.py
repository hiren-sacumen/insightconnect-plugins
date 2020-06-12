# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Add an address object (host object) as a network object"


class Input:
    COLOR = "color"
    HOST_IP = "host_ip"
    NAME = "name"
    SKIP_RFC1918 = "skip_rfc1918"
    WHITELIST = "whitelist"
    

class Output:
    ERROR_MESSAGE = "error_message"
    HOST_OBJECT = "host_object"
    SUCCESS = "success"
    

class CreateAddressObjectInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "color": {
      "type": "string",
      "title": "Color",
      "description": "Color",
      "default": "black",
      "enum": [
        "black",
        "aquamarine",
        "blue",
        "brown",
        "burlywood",
        "coral",
        "crete",
        "cyan",
        "dark blue",
        "dark gold",
        "dark gray",
        "dark green",
        "dark orange",
        "dark sea green",
        "firebrick",
        "forest green",
        "gold",
        "gray",
        "khaki",
        "lemon chiffon",
        "light green",
        "magenta",
        "navy blue",
        "olive",
        "orange",
        "orchid",
        "pink",
        "purple",
        "red",
        "sea green",
        "sienna",
        "sky blue",
        "slate blue",
        "turquoise",
        "violet red",
        "yellow"
      ],
      "order": 3
    },
    "host_ip": {
      "type": "string",
      "title": "Host IP Address",
      "description": "Host IP address",
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name",
      "order": 1
    },
    "skip_rfc1918": {
      "type": "boolean",
      "title": "Skip RFC 1918 (Private) IP Addresses",
      "description": "Skip private IP addresses as defined in RFC 1918",
      "default": true,
      "order": 5
    },
    "whitelist": {
      "type": "array",
      "title": "Whitelist",
      "description": "This list contains a set of network objects that should not be blocked. This can include IP addresses and CIDR IP addresses",
      "items": {
        "type": "string"
      },
      "order": 4
    }
  },
  "required": [
    "host_ip",
    "name",
    "skip_rfc1918"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateAddressObjectOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "error_message": {
      "type": "string",
      "title": "Error Message",
      "description": "The cause of the error (if the action fails)",
      "order": 3
    },
    "host_object": {
      "$ref": "#/definitions/host_object",
      "title": "Host",
      "description": "Information about the host object that was added",
      "order": 1
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether or not Check Point could successfully create the address object",
      "order": 2
    }
  },
  "required": [
    "success"
  ],
  "definitions": {
    "creation_time_type": {
      "type": "object",
      "title": "creation_time_type",
      "properties": {
        "iso-8601": {
          "type": "string",
          "title": "ISO-8601",
          "description": "ISO-8601",
          "order": 2
        },
        "posix": {
          "type": "integer",
          "title": "POSIX",
          "description": "POSIX",
          "order": 1
        }
      }
    },
    "domain": {
      "type": "object",
      "title": "domain",
      "properties": {
        "domain-type": {
          "type": "string",
          "title": "Domain",
          "description": "Domain",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "uid": {
          "type": "string",
          "title": "UID",
          "description": "UID",
          "order": 3
        }
      }
    },
    "host_object": {
      "type": "object",
      "title": "host_object",
      "properties": {
        "color": {
          "type": "string",
          "title": "Color",
          "description": "Color",
          "order": 4
        },
        "comments": {
          "type": "string",
          "title": "Comments",
          "description": "Comments",
          "order": 7
        },
        "domain": {
          "$ref": "#/definitions/domain",
          "title": "Domain",
          "description": "Domain",
          "order": 1
        },
        "groups": {
          "type": "array",
          "title": "Groups",
          "description": "Groups",
          "items": {
            "type": "object"
          },
          "order": 9
        },
        "icon": {
          "type": "string",
          "title": "Icon",
          "description": "Icon",
          "order": 14
        },
        "interfaces": {
          "type": "array",
          "title": "Interfaces",
          "description": "Interfaces",
          "items": {
            "type": "object"
          },
          "order": 5
        },
        "ipv4-address": {
          "type": "string",
          "title": "IPv4-Address",
          "description": "IPv4-address",
          "order": 11
        },
        "meta-info": {
          "$ref": "#/definitions/meta_info_type",
          "title": "Meta-Info",
          "description": "Meta-info",
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "nat-settings": {
          "type": "object",
          "title": "NAT-Settings",
          "description": "NAT-settings",
          "order": 6
        },
        "read-only": {
          "type": "boolean",
          "title": "Read-Only",
          "description": "Read-only",
          "order": 13
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags",
          "items": {
            "type": "object"
          },
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 12
        },
        "uid": {
          "type": "string",
          "title": "UID",
          "description": "UID",
          "order": 10
        }
      },
      "definitions": {
        "creation_time_type": {
          "type": "object",
          "title": "creation_time_type",
          "properties": {
            "iso-8601": {
              "type": "string",
              "title": "ISO-8601",
              "description": "ISO-8601",
              "order": 2
            },
            "posix": {
              "type": "integer",
              "title": "POSIX",
              "description": "POSIX",
              "order": 1
            }
          }
        },
        "domain": {
          "type": "object",
          "title": "domain",
          "properties": {
            "domain-type": {
              "type": "string",
              "title": "Domain",
              "description": "Domain",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "uid": {
              "type": "string",
              "title": "UID",
              "description": "UID",
              "order": 3
            }
          }
        },
        "meta_info_type": {
          "type": "object",
          "title": "meta_info_type",
          "properties": {
            "creation-time": {
              "$ref": "#/definitions/creation_time_type",
              "title": "Creation-Time",
              "description": "Creation-time",
              "order": 2
            },
            "creator": {
              "type": "string",
              "title": "Creator",
              "description": "Creator",
              "order": 6
            },
            "last-modifier": {
              "type": "string",
              "title": "Last-Modifier",
              "description": "Last-modifier",
              "order": 3
            },
            "last-modify-time": {
              "$ref": "#/definitions/creation_time_type",
              "title": "Last-Modify-Time",
              "description": "Last-modify-time",
              "order": 4
            },
            "lock": {
              "type": "string",
              "title": "Lock",
              "description": "Lock",
              "order": 5
            },
            "validation-state": {
              "type": "string",
              "title": "Validation-State",
              "description": "Validation-state",
              "order": 1
            }
          },
          "definitions": {
            "creation_time_type": {
              "type": "object",
              "title": "creation_time_type",
              "properties": {
                "iso-8601": {
                  "type": "string",
                  "title": "ISO-8601",
                  "description": "ISO-8601",
                  "order": 2
                },
                "posix": {
                  "type": "integer",
                  "title": "POSIX",
                  "description": "POSIX",
                  "order": 1
                }
              }
            }
          }
        }
      }
    },
    "meta_info_type": {
      "type": "object",
      "title": "meta_info_type",
      "properties": {
        "creation-time": {
          "$ref": "#/definitions/creation_time_type",
          "title": "Creation-Time",
          "description": "Creation-time",
          "order": 2
        },
        "creator": {
          "type": "string",
          "title": "Creator",
          "description": "Creator",
          "order": 6
        },
        "last-modifier": {
          "type": "string",
          "title": "Last-Modifier",
          "description": "Last-modifier",
          "order": 3
        },
        "last-modify-time": {
          "$ref": "#/definitions/creation_time_type",
          "title": "Last-Modify-Time",
          "description": "Last-modify-time",
          "order": 4
        },
        "lock": {
          "type": "string",
          "title": "Lock",
          "description": "Lock",
          "order": 5
        },
        "validation-state": {
          "type": "string",
          "title": "Validation-State",
          "description": "Validation-state",
          "order": 1
        }
      },
      "definitions": {
        "creation_time_type": {
          "type": "object",
          "title": "creation_time_type",
          "properties": {
            "iso-8601": {
              "type": "string",
              "title": "ISO-8601",
              "description": "ISO-8601",
              "order": 2
            },
            "posix": {
              "type": "integer",
              "title": "POSIX",
              "description": "POSIX",
              "order": 1
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
