# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    GROUPID = "groupid"
    HOSTNAME = "hostname"
    ID = "id"
    IP = "ip"
    

class Output:
    SENSORS = "sensors"
    

class ListSensorsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "groupid": {
      "type": "string",
      "title": "Group ID",
      "description": "The sensor group ID",
      "order": 4
    },
    "hostname": {
      "type": "string",
      "title": "Hostname",
      "description": "The sensor hostname",
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The sensor ID",
      "order": 1
    },
    "ip": {
      "type": "string",
      "title": "IP Address",
      "description": "The sensor IP address",
      "order": 3
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListSensorsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "sensors": {
      "type": "array",
      "title": "Sensors",
      "description": "The list of sensors",
      "items": {
        "$ref": "#/definitions/sensor"
      },
      "order": 1
    }
  },
  "definitions": {
    "sensor": {
      "type": "object",
      "title": "sensor",
      "properties": {
        "boot_id": {
          "type": "string",
          "title": "Boot ID",
          "description": "Boot ID",
          "order": 12
        },
        "build_id": {
          "type": "integer",
          "title": "Build ID",
          "description": "Sensor build ID",
          "order": 6
        },
        "build_version_string": {
          "type": "string",
          "title": "Build Version String",
          "description": "Build version string",
          "order": 25
        },
        "computer_dns_name": {
          "type": "string",
          "title": "Computer DNS Name",
          "description": "DNS name of the computer",
          "order": 8
        },
        "computer_name": {
          "type": "string",
          "title": "Computer Name",
          "description": "Computer name",
          "order": 15
        },
        "computer_sid": {
          "type": "string",
          "title": "Computer SID",
          "description": "Computer SID",
          "order": 13
        },
        "cookie": {
          "type": "integer",
          "title": "Cookie",
          "description": "Cookie",
          "order": 24
        },
        "display": {
          "type": "boolean",
          "title": "Display",
          "description": "Display",
          "order": 28
        },
        "event_log_flush_time": {
          "type": "string",
          "title": "Event Log Flush Time",
          "description": "Event log flush time",
          "order": 14
        },
        "found": {
          "type": "boolean",
          "title": "Found",
          "description": "If sensor was found",
          "order": 30
        },
        "group_id": {
          "type": "integer",
          "title": "Group ID",
          "description": "Group ID",
          "order": 27
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Sensor ID",
          "order": 5
        },
        "is_isolating": {
          "type": "boolean",
          "title": "Is Isolating",
          "description": "Is sensor isolated",
          "order": 4
        },
        "last_checkin_time": {
          "type": "string",
          "title": "Last Checkin Time",
          "description": "Last checkin time",
          "order": 26
        },
        "license_expiration": {
          "type": "string",
          "title": "License Expiration",
          "description": "License expiration",
          "order": 16
        },
        "network_adapters": {
          "type": "string",
          "title": "Network Adapters",
          "description": "Network adapters",
          "order": 17
        },
        "network_isolation_enabled": {
          "type": "boolean",
          "title": "Network Isolation Enabled",
          "description": "Network isolation enabled",
          "order": 22
        },
        "next_checkin_time": {
          "type": "string",
          "title": "Next Check-In Time",
          "description": "Next check-in time",
          "order": 10
        },
        "notes": {
          "type": "string",
          "title": "Notes",
          "description": "Notes",
          "order": 21
        },
        "os_environment_display_string": {
          "type": "string",
          "title": "OS Environment Display String",
          "description": "OS environment display string",
          "order": 2
        },
        "os_environment_id": {
          "type": "integer",
          "title": "OS Environment ID",
          "description": "OS environment ID",
          "order": 23
        },
        "physical_memory_size": {
          "type": "string",
          "title": "Physical Memory Size",
          "description": "Physical memory size",
          "order": 9
        },
        "registration_time": {
          "type": "string",
          "title": "Registration Time",
          "description": "Registration time",
          "order": 19
        },
        "sensor_health_message": {
          "type": "string",
          "title": "Sensor Health Message",
          "description": "Sensor health message",
          "order": 11
        },
        "sensor_health_status": {
          "type": "integer",
          "title": "Sensor Health Status",
          "description": "Sensor health status",
          "order": 18
        },
        "sensor_uptime": {
          "type": "string",
          "title": "Sensor Uptime",
          "description": "How long the sensor has been up",
          "order": 3
        },
        "systemvolume_free_size": {
          "type": "string",
          "title": "Systemvolume Free Size",
          "description": "Systemvolume free size",
          "order": 20
        },
        "systemvolume_total_size": {
          "type": "string",
          "title": "Systemvolume Total Size",
          "description": "Total size of system volume",
          "order": 1
        },
        "uninstall": {
          "type": "boolean",
          "title": "Uninstall",
          "description": "Uninstall",
          "order": 29
        },
        "uptime": {
          "type": "string",
          "title": "Uptime",
          "description": "Uptime",
          "order": 7
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
