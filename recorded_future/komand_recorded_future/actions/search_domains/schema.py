# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DIRECTION = "direction"
    FROM = "from"
    LIMIT = "limit"
    ORDERBY = "orderby"
    PARENT = "parent"
    

class Output:
    DATA = "data"
    

class SearchDomainsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "direction": {
      "type": "string",
      "title": "Result Direction",
      "description": "Sort results ascending/descending",
      "default": "asc",
      "enum": [
        "asc",
        "desc"
      ],
      "order": 4
    },
    "from": {
      "type": "number",
      "title": "Offset",
      "description": "Number of initial records to skip",
      "default": 0,
      "order": 2
    },
    "limit": {
      "type": "number",
      "title": "Limit",
      "description": "Number of results to retrieve, up to 100",
      "order": 1
    },
    "orderby": {
      "type": "string",
      "title": "Order By",
      "description": "Which property to sort the results by",
      "enum": [
        "Created",
        "Firstseen",
        "Lastseen",
        "Modified",
        "Riskscore",
        "Rules",
        "Sevendayshits",
        "Sixtydayshits",
        "Totalhits"
      ],
      "order": 3
    },
    "parent": {
      "type": "string",
      "title": "Parent",
      "description": "Parent domain, if any",
      "order": 5
    }
  },
  "required": [
    "direction",
    "parent",
    "limit",
    "from",
    "orderby"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchDomainsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "$ref": "#/definitions/search_data",
      "title": "Data",
      "description": "Data",
      "order": 1
    }
  },
  "definitions": {
    "counts": {
      "type": "object",
      "title": "counts",
      "properties": {
        "count": {
          "type": "integer",
          "title": "Count",
          "order": 1
        },
        "date": {
          "type": "string",
          "title": "Date",
          "order": 2
        }
      }
    },
    "entities": {
      "type": "object",
      "title": "entities",
      "properties": {
        "count": {
          "type": "integer",
          "title": "Count",
          "order": 1
        },
        "entity": {
          "$ref": "#/definitions/entity",
          "title": "Entity",
          "order": 2
        }
      },
      "definitions": {
        "entity": {
          "type": "object",
          "title": "entity",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 4
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 3
            }
          }
        }
      }
    },
    "entity": {
      "type": "object",
      "title": "entity",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 3
        }
      }
    },
    "evidenceDetails": {
      "type": "object",
      "title": "evidenceDetails",
      "properties": {
        "criticality": {
          "type": "integer",
          "title": "Criticality",
          "order": 1
        },
        "criticalityLabel": {
          "type": "string",
          "title": "Criticality Label",
          "order": 2
        },
        "evidenceString": {
          "type": "string",
          "title": "Evidence String",
          "order": 3
        },
        "rule": {
          "type": "string",
          "title": "Rule",
          "order": 4
        },
        "timestamp": {
          "type": "string",
          "title": "Timestamp",
          "order": 5
        }
      }
    },
    "metrics": {
      "type": "object",
      "title": "metrics",
      "properties": {
        "type": {
          "type": "string",
          "title": "Type",
          "order": 1
        },
        "value": {
          "type": "integer",
          "title": "Value",
          "order": 2
        }
      }
    },
    "relatedEntities": {
      "type": "object",
      "title": "relatedEntities",
      "properties": {
        "entities": {
          "type": "array",
          "title": "Entities",
          "items": {
            "$ref": "#/definitions/entities"
          },
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 2
        }
      },
      "definitions": {
        "entities": {
          "type": "object",
          "title": "entities",
          "properties": {
            "count": {
              "type": "integer",
              "title": "Count",
              "order": 1
            },
            "entity": {
              "$ref": "#/definitions/entity",
              "title": "Entity",
              "order": 2
            }
          },
          "definitions": {
            "entity": {
              "type": "object",
              "title": "entity",
              "properties": {
                "description": {
                  "type": "string",
                  "title": "Description",
                  "order": 4
                },
                "id": {
                  "type": "string",
                  "title": "Id",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "order": 3
                }
              }
            }
          }
        },
        "entity": {
          "type": "object",
          "title": "entity",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 4
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 3
            }
          }
        }
      }
    },
    "risk": {
      "type": "object",
      "title": "risk",
      "properties": {
        "criticality": {
          "type": "integer",
          "title": "Criticality",
          "order": 1
        },
        "criticalityLabel": {
          "type": "string",
          "title": "Criticality Label",
          "order": 2
        },
        "evidenceDetails": {
          "type": "array",
          "title": "Evidence Details",
          "items": {
            "$ref": "#/definitions/evidenceDetails"
          },
          "order": 3
        },
        "riskSummary": {
          "type": "string",
          "title": "Risk Summary",
          "order": 4
        },
        "rules": {
          "type": "integer",
          "title": "Rules",
          "order": 5
        },
        "score": {
          "type": "integer",
          "title": "Score",
          "order": 6
        }
      },
      "definitions": {
        "evidenceDetails": {
          "type": "object",
          "title": "evidenceDetails",
          "properties": {
            "criticality": {
              "type": "integer",
              "title": "Criticality",
              "order": 1
            },
            "criticalityLabel": {
              "type": "string",
              "title": "Criticality Label",
              "order": 2
            },
            "evidenceString": {
              "type": "string",
              "title": "Evidence String",
              "order": 3
            },
            "rule": {
              "type": "string",
              "title": "Rule",
              "order": 4
            },
            "timestamp": {
              "type": "string",
              "title": "Timestamp",
              "order": 5
            }
          }
        }
      }
    },
    "search_data": {
      "type": "object",
      "title": "search_data",
      "properties": {
        "counts": {
          "type": "array",
          "title": "Counts",
          "items": {
            "$ref": "#/definitions/counts"
          },
          "order": 1
        },
        "entity": {
          "$ref": "#/definitions/entity",
          "title": "Entity",
          "order": 2
        },
        "hashAlgorithm": {
          "type": "string",
          "title": "Hash Algorithm",
          "order": 3
        },
        "intelCard": {
          "type": "string",
          "title": "Intel Card",
          "order": 4
        },
        "metrics": {
          "type": "array",
          "title": "Metrics",
          "items": {
            "$ref": "#/definitions/metrics"
          },
          "order": 5
        },
        "relatedEntities": {
          "type": "array",
          "title": "Related Entities",
          "items": {
            "$ref": "#/definitions/relatedEntities"
          },
          "order": 6
        },
        "risk": {
          "$ref": "#/definitions/risk",
          "title": "Risk",
          "order": 7
        },
        "sightings": {
          "type": "array",
          "title": "Sightings",
          "items": {
            "$ref": "#/definitions/sightings"
          },
          "order": 8
        },
        "threatLists": {
          "type": "array",
          "title": "Threat Lists",
          "items": {
            "type": "object"
          },
          "order": 9
        },
        "timestamps": {
          "$ref": "#/definitions/timestamps",
          "title": "Timestamps",
          "order": 10
        }
      },
      "definitions": {
        "counts": {
          "type": "object",
          "title": "counts",
          "properties": {
            "count": {
              "type": "integer",
              "title": "Count",
              "order": 1
            },
            "date": {
              "type": "string",
              "title": "Date",
              "order": 2
            }
          }
        },
        "entities": {
          "type": "object",
          "title": "entities",
          "properties": {
            "count": {
              "type": "integer",
              "title": "Count",
              "order": 1
            },
            "entity": {
              "$ref": "#/definitions/entity",
              "title": "Entity",
              "order": 2
            }
          },
          "definitions": {
            "entity": {
              "type": "object",
              "title": "entity",
              "properties": {
                "description": {
                  "type": "string",
                  "title": "Description",
                  "order": 4
                },
                "id": {
                  "type": "string",
                  "title": "Id",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "order": 3
                }
              }
            }
          }
        },
        "entity": {
          "type": "object",
          "title": "entity",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 4
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 3
            }
          }
        },
        "evidenceDetails": {
          "type": "object",
          "title": "evidenceDetails",
          "properties": {
            "criticality": {
              "type": "integer",
              "title": "Criticality",
              "order": 1
            },
            "criticalityLabel": {
              "type": "string",
              "title": "Criticality Label",
              "order": 2
            },
            "evidenceString": {
              "type": "string",
              "title": "Evidence String",
              "order": 3
            },
            "rule": {
              "type": "string",
              "title": "Rule",
              "order": 4
            },
            "timestamp": {
              "type": "string",
              "title": "Timestamp",
              "order": 5
            }
          }
        },
        "metrics": {
          "type": "object",
          "title": "metrics",
          "properties": {
            "type": {
              "type": "string",
              "title": "Type",
              "order": 1
            },
            "value": {
              "type": "integer",
              "title": "Value",
              "order": 2
            }
          }
        },
        "relatedEntities": {
          "type": "object",
          "title": "relatedEntities",
          "properties": {
            "entities": {
              "type": "array",
              "title": "Entities",
              "items": {
                "$ref": "#/definitions/entities"
              },
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 2
            }
          },
          "definitions": {
            "entities": {
              "type": "object",
              "title": "entities",
              "properties": {
                "count": {
                  "type": "integer",
                  "title": "Count",
                  "order": 1
                },
                "entity": {
                  "$ref": "#/definitions/entity",
                  "title": "Entity",
                  "order": 2
                }
              },
              "definitions": {
                "entity": {
                  "type": "object",
                  "title": "entity",
                  "properties": {
                    "description": {
                      "type": "string",
                      "title": "Description",
                      "order": 4
                    },
                    "id": {
                      "type": "string",
                      "title": "Id",
                      "order": 1
                    },
                    "name": {
                      "type": "string",
                      "title": "Name",
                      "order": 2
                    },
                    "type": {
                      "type": "string",
                      "title": "Type",
                      "order": 3
                    }
                  }
                }
              }
            },
            "entity": {
              "type": "object",
              "title": "entity",
              "properties": {
                "description": {
                  "type": "string",
                  "title": "Description",
                  "order": 4
                },
                "id": {
                  "type": "string",
                  "title": "Id",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "order": 3
                }
              }
            }
          }
        },
        "risk": {
          "type": "object",
          "title": "risk",
          "properties": {
            "criticality": {
              "type": "integer",
              "title": "Criticality",
              "order": 1
            },
            "criticalityLabel": {
              "type": "string",
              "title": "Criticality Label",
              "order": 2
            },
            "evidenceDetails": {
              "type": "array",
              "title": "Evidence Details",
              "items": {
                "$ref": "#/definitions/evidenceDetails"
              },
              "order": 3
            },
            "riskSummary": {
              "type": "string",
              "title": "Risk Summary",
              "order": 4
            },
            "rules": {
              "type": "integer",
              "title": "Rules",
              "order": 5
            },
            "score": {
              "type": "integer",
              "title": "Score",
              "order": 6
            }
          },
          "definitions": {
            "evidenceDetails": {
              "type": "object",
              "title": "evidenceDetails",
              "properties": {
                "criticality": {
                  "type": "integer",
                  "title": "Criticality",
                  "order": 1
                },
                "criticalityLabel": {
                  "type": "string",
                  "title": "Criticality Label",
                  "order": 2
                },
                "evidenceString": {
                  "type": "string",
                  "title": "Evidence String",
                  "order": 3
                },
                "rule": {
                  "type": "string",
                  "title": "Rule",
                  "order": 4
                },
                "timestamp": {
                  "type": "string",
                  "title": "Timestamp",
                  "order": 5
                }
              }
            }
          }
        },
        "sightings": {
          "type": "object",
          "title": "sightings",
          "properties": {
            "fragment": {
              "type": "string",
              "title": "Fragment",
              "order": 1
            },
            "published": {
              "type": "string",
              "title": "Published",
              "order": 2
            },
            "source": {
              "type": "string",
              "title": "Source",
              "order": 3
            },
            "title": {
              "type": "string",
              "title": "Title",
              "order": 4
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 5
            },
            "url": {
              "type": "string",
              "title": "Url",
              "order": 6
            }
          }
        },
        "timestamps": {
          "type": "object",
          "title": "timestamps",
          "properties": {
            "firstSeen": {
              "type": "string",
              "title": "First Seen",
              "order": 1
            },
            "lastSeen": {
              "type": "string",
              "title": "Last Seen",
              "order": 2
            }
          }
        }
      }
    },
    "sightings": {
      "type": "object",
      "title": "sightings",
      "properties": {
        "fragment": {
          "type": "string",
          "title": "Fragment",
          "order": 1
        },
        "published": {
          "type": "string",
          "title": "Published",
          "order": 2
        },
        "source": {
          "type": "string",
          "title": "Source",
          "order": 3
        },
        "title": {
          "type": "string",
          "title": "Title",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 5
        },
        "url": {
          "type": "string",
          "title": "Url",
          "order": 6
        }
      }
    },
    "timestamps": {
      "type": "object",
      "title": "timestamps",
      "properties": {
        "firstSeen": {
          "type": "string",
          "title": "First Seen",
          "order": 1
        },
        "lastSeen": {
          "type": "string",
          "title": "Last Seen",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
