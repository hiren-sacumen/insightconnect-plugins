# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DOMAIN = "domain"
    

class Output:
    WHOIS = "whois"
    

class DomainWhoisInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain name without wildcards and including TLD",
      "order": 1
    }
  },
  "required": [
    "domain"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DomainWhoisOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "whois": {
      "type": "array",
      "title": "WHOIS",
      "description": "Array of WHOIS results for the domain provided with all available information",
      "order": 1
    }
  },
  "required": [
    "whois"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
