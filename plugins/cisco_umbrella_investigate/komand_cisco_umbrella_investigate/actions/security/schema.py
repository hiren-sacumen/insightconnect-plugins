# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Returns scores or security features"


class Input:
    DOMAIN = "domain"


class Output:
    ASN_SCORE = "asn_score"
    ATTACK = "attack"
    DGA_SCORE = "dga_score"
    ENTROPY = "entropy"
    GEODIVERSITY = "geodiversity"
    GEODIVERSITY_NORMALIZED = "geodiversity_normalized"
    GEOSCORE = "geoscore"
    KS_TEST = "ks_test"
    PAGERANK = "pagerank"
    PERPLEXITY = "perplexity"
    POPULARITY = "popularity"
    PREFIX_SCORE = "prefix_score"
    RIP_SCORE = "rip_score"
    SECURERANK2 = "securerank2"
    THREAT_TYPE = "threat_type"
    TLD_GEODIVERSITY = "tld_geodiversity"


class SecurityInput(komand.Input):
    schema = json.loads(
        """
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain Name",
      "description": "Domain name",
      "order": 1
    }
  },
  "required": [
    "domain"
  ]
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SecurityOutput(komand.Output):
    schema = json.loads(
        """
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asn_score": {
      "type": "number",
      "title": "ASN Score",
      "description": "ASN reputation score, ranges from -100 to 0 with -100 being very suspicious",
      "order": 6
    },
    "attack": {
      "type": "string",
      "title": "Attack",
      "description": "The name of any known attacks associated with this domain. Returns blank if no known threat associated with domain",
      "order": 15
    },
    "dga_score": {
      "type": "number",
      "title": "Domain Generation Algorithm",
      "description": "Domain Generation Algorithm. This score is generated based on the likeliness of the domain name being generated by an algorithm rather than a human",
      "order": 1
    },
    "entropy": {
      "type": "number",
      "title": "Entropy",
      "description": "The number of bits required to encode the domain name, as a score. This score is to be used in conjunction with DGA and Perplexity",
      "order": 3
    },
    "geodiversity": {
      "type": "array",
      "title": "Geodiversity",
      "description": "A score representing the number of queries from clients visiting the domain, broken down by country. Score is a non-normalized ratio between 0 and 1",
      "order": 10
    },
    "geodiversity_normalized": {
      "type": "array",
      "title": "Geodiversity Normalized",
      "description": "A score representing the amount of queries for clients visiting the domain, broken down by country. Score is a normalized ratio between 0 and 1",
      "order": 11
    },
    "geoscore": {
      "type": "number",
      "title": "Geo Score",
      "description": "A score that represents how far the different physical locations serving this name are from each other",
      "order": 13
    },
    "ks_test": {
      "type": "number",
      "title": "Kolmogorov Smirnov Test",
      "description": "Kolmogorov Smirnov test on geodiversity. 0 means that the client traffic matches what is expected for this TLD",
      "order": 14
    },
    "pagerank": {
      "type": "number",
      "title": "Google Pagerank",
      "description": "Popularity according to Google's pagerank algorithm",
      "order": 5
    },
    "perplexity": {
      "type": "number",
      "title": "Perplexity",
      "description": "A second score on the likeliness of the name to be algorithmically generated, on a scale from 0 to 1",
      "order": 2
    },
    "popularity": {
      "type": "number",
      "title": "Popularity",
      "description": "The number of unique client IPs visiting this site, relative to the all requests to all sites. A score of how many different client/unique IPs go to this domain compared to others",
      "order": 9
    },
    "prefix_score": {
      "type": "number",
      "title": "Prefix Score",
      "description": "Prefix ranks domains given their IP prefixes (an IP prefix is the first three octets in an IP address) and the reputation score of these prefixes. Ranges from -100 to 0, -100 being very suspicious",
      "order": 7
    },
    "rip_score": {
      "type": "number",
      "title": "RIP Score",
      "description": "RIP ranks domains given their IP addresses and the reputation score of these IP addresses. Ranges from -100 to 0, -100 being very suspicious",
      "order": 8
    },
    "securerank2": {
      "type": "number",
      "title": "Suspicious Domain Rank",
      "description": "Securerank is designed to identify hostnames requested by known infected clients but never requested by clean clients, assuming these domains are more likely to be bad. Scores range from -100 (suspicious) to 100 (benign)",
      "order": 4
    },
    "threat_type": {
      "type": "string",
      "title": "Threat Type",
      "description": "The type of the known attack, such as botnet or APT. Returns blank if no known threat associated with domain",
      "order": 16
    },
    "tld_geodiversity": {
      "type": "array",
      "title": "TLD Country Code Geodiversity",
      "description": "A score that represents the TLD country code geodiversity as a percentage of clients visiting the domain. Occurs most often with domains that have a ccTLD. Score is normalized ratio between 0 and 1",
      "order": 12
    }
  },
  "required": [
    "dga_score",
    "entropy",
    "geodiversity",
    "geodiversity_normalized",
    "geoscore",
    "ks_test",
    "pagerank",
    "perplexity",
    "popularity",
    "securerank2",
    "tld_geodiversity"
  ]
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
