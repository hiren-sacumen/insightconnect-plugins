# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ID = "id"
    VIRTUAL_SERVICE_ID = "virtual_service_id"
    

class Output:
    COMMENTS = "comments"
    EXTENDED_MATCH = "extended_match"
    EXTENDED_MATCH_SEQUENCE = "extended_match_sequence"
    HOST_MATCH = "host_match"
    ID = "id"
    LB_ALGORITHM = "lb_algorithm"
    NAME = "name"
    PERSISTENCE_METHOD = "persistence_method"
    SERVERS = "servers"
    SERVICE_NAME = "service_name"
    URL_MATCH = "url_match"
    

class RetrieveContentRulesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Content rule ID",
      "order": 2
    },
    "virtual_service_id": {
      "type": "string",
      "title": "Virtual Service ID",
      "description": "Virtual Service ID",
      "order": 1
    }
  },
  "required": [
    "virtual_service_id",
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RetrieveContentRulesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comments": {
      "type": "string",
      "title": "Comments",
      "description": "Description about the content rule",
      "order": 5
    },
    "extended_match": {
      "type": "string",
      "title": "Extended Match",
      "description": "The expression that consists of a combination of HTTP headers and/or query string parameters",
      "order": 6
    },
    "extended_match_sequence": {
      "type": "integer",
      "title": "Extended Match Sequence",
      "description": "The number to indicate the order in which the extended match rule must be evaluated in the requests",
      "order": 2
    },
    "host_match": {
      "type": "string",
      "title": "Host Match",
      "description": "The host name to be matched against the host in the request header",
      "order": 4
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "ID content rule",
      "order": 9
    },
    "lb_algorithm": {
      "type": "string",
      "title": "Load Balancing Algorithm",
      "description": "The algorithm to be used for load balancing",
      "order": 1
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name of content rule",
      "order": 3
    },
    "persistence_method": {
      "type": "string",
      "title": "Persistance Method",
      "description": "The Persistence Method to be used to maintain the connection between a client and the first server that it connects to, even when the system is load balancing traffic",
      "order": 11
    },
    "servers": {
      "type": "array",
      "title": "Servers",
      "description": "Servers info",
      "order": 10
    },
    "service_name": {
      "type": "string",
      "title": "Service Name",
      "description": "Service name",
      "order": 7
    },
    "url_match": {
      "type": "string",
      "title": "URL Match",
      "description": "The URL to be matched to the URL in the request header",
      "order": 8
    }
  },
  "required": [
    "id",
    "servers",
    "extended_match_sequence",
    "name",
    "host_match",
    "comments",
    "extended_match",
    "lb_algorithm",
    "service_name",
    "url_match",
    "persistence_method"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
