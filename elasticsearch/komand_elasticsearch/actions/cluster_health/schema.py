# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    pass

class Output:
    CLUSTER_HEALTH = "cluster_health"
    

class ClusterHealthInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ClusterHealthOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cluster_health": {
      "$ref": "#/definitions/health",
      "title": "Cluster Health",
      "description": "Cluster Health",
      "order": 1
    }
  },
  "definitions": {
    "health": {
      "type": "object",
      "title": "health",
      "properties": {
        "active_primary_shards": {
          "type": "integer",
          "title": "Active Primary Shards",
          "order": 6
        },
        "active_shards": {
          "type": "integer",
          "title": "Active Shards",
          "order": 7
        },
        "active_shards_percent_as_number": {
          "type": "number",
          "title": "Active Shards Percent as Number",
          "order": 15
        },
        "cluster_name": {
          "type": "string",
          "title": "Cluster Name",
          "order": 1
        },
        "delayed_unassigned_shards": {
          "type": "integer",
          "title": "Delayed Unassigned Shards",
          "order": 11
        },
        "initializing_shards": {
          "type": "integer",
          "title": "Initializing Shards",
          "order": 9
        },
        "number_of_data_nodes": {
          "type": "integer",
          "title": "Number of Data Nodes",
          "order": 5
        },
        "number_of_in_flight_fetch": {
          "type": "integer",
          "title": "Number of in Flight Fetch",
          "order": 13
        },
        "number_of_nodes": {
          "type": "integer",
          "title": "Number of Nodes",
          "order": 4
        },
        "number_of_pending_tasks": {
          "type": "integer",
          "title": "Number of Pending Tasks",
          "order": 12
        },
        "relocating_shards": {
          "type": "integer",
          "title": "Relocating Shards",
          "order": 8
        },
        "status": {
          "type": "string",
          "title": "Status",
          "order": 2
        },
        "task_max_waiting_in_queue_limits": {
          "type": "integer",
          "title": "Task Max Waiting in Queue Mills",
          "order": 14
        },
        "timed_out": {
          "type": "boolean",
          "title": "Timed Out",
          "order": 3
        },
        "unassigned_shards": {
          "type": "integer",
          "title": "Unassigned Shards",
          "order": 10
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
