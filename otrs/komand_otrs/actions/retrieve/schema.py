# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieve OTRS ticket"


class Input:
    TICKET_ID = "ticket_id"
    

class Output:
    TICKET = "Ticket"
    

class RetrieveInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ticket_id": {
      "type": "integer",
      "title": "Ticket ID",
      "description": "Ticket ID",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RetrieveOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "Ticket": {
      "$ref": "#/definitions/Ticket",
      "title": "Ticket",
      "description": "Ticket returned",
      "order": 1
    }
  },
  "definitions": {
    "Article": {
      "type": "object",
      "title": "Article",
      "properties": {
        "ArticleID": {
          "type": "string",
          "title": "Article ID",
          "description": "Article ID",
          "order": 1
        },
        "ArticleNumber": {
          "type": "integer",
          "title": "Article Number",
          "description": "Article number",
          "order": 2
        },
        "Attachment": {
          "type": "array",
          "title": "Attachment",
          "description": "Attachment",
          "items": {
            "$ref": "#/definitions/Attachment"
          },
          "order": 3
        },
        "Bcc": {
          "type": "string",
          "title": "BCC",
          "description": "BCC",
          "order": 4
        },
        "Body": {
          "type": "string",
          "title": "Body",
          "description": "Body",
          "order": 5
        },
        "Cc": {
          "type": "string",
          "title": "CC",
          "description": "CC",
          "order": 6
        },
        "ChangeBy": {
          "type": "string",
          "title": "Change By",
          "description": "Change by",
          "order": 7
        },
        "ChangeTime": {
          "type": "string",
          "title": "Change Time",
          "description": "Change time",
          "order": 8
        },
        "Charset": {
          "type": "string",
          "title": "Chartset",
          "description": "Charset",
          "order": 9
        },
        "CommunicationChannelID": {
          "type": "string",
          "title": "Communication Channel ID",
          "description": "Communication channel ID",
          "order": 10
        },
        "ContentCharset": {
          "type": "string",
          "title": "Content Charset",
          "description": "Content charset",
          "order": 11
        },
        "ContentType": {
          "type": "string",
          "title": "Content Type",
          "description": "Content type",
          "order": 12
        },
        "CreateBy": {
          "type": "string",
          "title": "Create By",
          "description": "Create by",
          "order": 13
        },
        "CreateTime": {
          "type": "string",
          "title": "Create Time",
          "description": "Create time",
          "order": 14
        },
        "From": {
          "type": "string",
          "title": "From",
          "description": "From",
          "order": 15
        },
        "InReplyTo": {
          "type": "string",
          "title": "In Reply To",
          "description": "In reply to",
          "order": 16
        },
        "IncomingTime": {
          "type": "string",
          "title": "Incoming Time",
          "description": "Incoming time",
          "order": 17
        },
        "IsVisibleForCustomer": {
          "type": "integer",
          "title": "Is Visible For Customer",
          "description": "Is visible For customer",
          "order": 18
        },
        "MessageID": {
          "type": "string",
          "title": "Message ID",
          "description": "Message ID",
          "order": 19
        },
        "MimeType": {
          "type": "string",
          "title": "MIME Type",
          "description": "MIME type",
          "order": 20
        },
        "References": {
          "type": "string",
          "title": "References",
          "description": "References",
          "order": 21
        },
        "ReplyTo": {
          "type": "string",
          "title": "Reply To",
          "description": "Reply to",
          "order": 22
        },
        "SenderType": {
          "type": "string",
          "title": "Sender type",
          "description": "Sender type",
          "order": 23
        },
        "SenderTypeID": {
          "type": "string",
          "title": "Sender Type ID",
          "description": "Sender type ID",
          "order": 24
        },
        "Subject": {
          "type": "string",
          "title": "Subject",
          "description": "Subject",
          "order": 25
        },
        "TicketID": {
          "type": "integer",
          "title": "Ticket ID",
          "description": "Ticket ID",
          "order": 26
        },
        "TimeUnit": {
          "type": "number",
          "title": "Time Unit",
          "description": "Time unit",
          "order": 27
        },
        "To": {
          "type": "string",
          "title": "To",
          "description": "To",
          "order": 28
        }
      },
      "definitions": {
        "Attachment": {
          "type": "object",
          "title": "Attachment",
          "properties": {
            "Content": {
              "type": "string",
              "title": "Content",
              "description": "Content",
              "order": 1
            },
            "ContentAlternative": {
              "type": "string",
              "title": "Content Alternative",
              "description": "Content alternative",
              "order": 2
            },
            "ContentID": {
              "type": "string",
              "title": "Content ID",
              "description": "Content ID",
              "order": 3
            },
            "ContentType": {
              "type": "string",
              "title": "Content Type",
              "description": "Content type",
              "order": 4
            },
            "Disposition": {
              "type": "string",
              "title": "Dispostion",
              "description": "Dispostion",
              "order": 5
            },
            "FileID": {
              "type": "string",
              "title": "File ID",
              "description": "File ID",
              "order": 6
            },
            "Filename": {
              "type": "string",
              "title": "Filename",
              "description": "Filename",
              "order": 7
            },
            "FilesizeRaw": {
              "type": "integer",
              "title": "File Size Raw",
              "description": "File size raw",
              "order": 8
            }
          }
        }
      }
    },
    "Attachment": {
      "type": "object",
      "title": "Attachment",
      "properties": {
        "Content": {
          "type": "string",
          "title": "Content",
          "description": "Content",
          "order": 1
        },
        "ContentAlternative": {
          "type": "string",
          "title": "Content Alternative",
          "description": "Content alternative",
          "order": 2
        },
        "ContentID": {
          "type": "string",
          "title": "Content ID",
          "description": "Content ID",
          "order": 3
        },
        "ContentType": {
          "type": "string",
          "title": "Content Type",
          "description": "Content type",
          "order": 4
        },
        "Disposition": {
          "type": "string",
          "title": "Dispostion",
          "description": "Dispostion",
          "order": 5
        },
        "FileID": {
          "type": "string",
          "title": "File ID",
          "description": "File ID",
          "order": 6
        },
        "Filename": {
          "type": "string",
          "title": "Filename",
          "description": "Filename",
          "order": 7
        },
        "FilesizeRaw": {
          "type": "integer",
          "title": "File Size Raw",
          "description": "File size raw",
          "order": 8
        }
      }
    },
    "DynamicField": {
      "type": "object",
      "title": "DynamicField",
      "properties": {
        "Name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        },
        "Value": {
          "type": "array",
          "title": "Value",
          "description": "Value",
          "items": {
            "type": "string"
          },
          "order": 2
        }
      }
    },
    "Ticket": {
      "type": "object",
      "title": "Ticket",
      "properties": {
        "Age": {
          "type": "integer",
          "title": "Age",
          "description": "Age",
          "order": 1
        },
        "ArchiveFlag": {
          "type": "string",
          "title": "Archive Flag",
          "description": "Archive flag",
          "order": 2
        },
        "Article": {
          "type": "array",
          "title": "Article",
          "description": "Article",
          "items": {
            "$ref": "#/definitions/Article"
          },
          "order": 3
        },
        "ChangeBy": {
          "type": "string",
          "title": "Change By",
          "description": "Change by",
          "order": 4
        },
        "Changed": {
          "type": "string",
          "title": "Changed",
          "description": "Changed",
          "order": 5
        },
        "CreateBy": {
          "type": "string",
          "title": "Create By",
          "description": "Create by",
          "order": 6
        },
        "Created": {
          "type": "string",
          "title": "Created",
          "description": "Created",
          "order": 7
        },
        "CustomerID": {
          "type": "string",
          "title": "Customer ID",
          "description": "Customer ID",
          "order": 8
        },
        "CustomerUserID": {
          "type": "string",
          "title": "Customer User ID",
          "description": "Customer user ID",
          "order": 9
        },
        "DynamicField": {
          "type": "array",
          "title": "Dynamic Field",
          "description": "Dynamic field",
          "items": {
            "$ref": "#/definitions/DynamicField"
          },
          "order": 10
        },
        "EscalationResponseTime": {
          "type": "integer",
          "title": "Escalation Response Time",
          "description": "Escalation response time",
          "order": 11
        },
        "EscalationSolutionTime": {
          "type": "integer",
          "title": "Escalation Solution Time",
          "description": "Escalation solution time",
          "order": 12
        },
        "EscalationTime": {
          "type": "integer",
          "title": "Escalation Time",
          "description": "Escalation time",
          "order": 13
        },
        "EscalationUpdateTime": {
          "type": "integer",
          "title": "Escalation Update Time",
          "description": "Escalation update time",
          "order": 14
        },
        "GroupID": {
          "type": "string",
          "title": "Group ID",
          "description": "Group ID",
          "order": 15
        },
        "Lock": {
          "type": "string",
          "title": "Lock",
          "description": "Lock",
          "order": 16
        },
        "LockID": {
          "type": "string",
          "title": "Lock ID",
          "description": "Lock ID",
          "order": 17
        },
        "Owner": {
          "type": "string",
          "title": "Owner",
          "description": "Owner",
          "order": 18
        },
        "OwnerID": {
          "type": "string",
          "title": "Owner ID",
          "description": "Owner ID",
          "order": 19
        },
        "Priority": {
          "type": "string",
          "title": "Priority",
          "description": "Priority",
          "order": 20
        },
        "PriorityID": {
          "type": "string",
          "title": "Priority ID",
          "description": "Priority ID",
          "order": 21
        },
        "Queue": {
          "type": "string",
          "title": "Queue",
          "description": "Queue",
          "order": 22
        },
        "QueueID": {
          "type": "string",
          "title": "Queue ID",
          "description": "Queue ID",
          "order": 23
        },
        "RealTillTimeNotUsed": {
          "type": "string",
          "title": "Real Till Time Not Used",
          "description": "Real till time not used",
          "order": 24
        },
        "Responsible": {
          "type": "string",
          "title": "Responsible",
          "description": "Responsible",
          "order": 25
        },
        "ResponsibleID": {
          "type": "string",
          "title": "Responsible ID",
          "description": "Responsible ID",
          "order": 26
        },
        "SLAID": {
          "type": "string",
          "title": "SLAID",
          "description": "SLAID",
          "order": 27
        },
        "ServiceID": {
          "type": "string",
          "title": "Service ID",
          "description": "Service ID",
          "order": 28
        },
        "State": {
          "type": "string",
          "title": "State",
          "description": "State",
          "order": 29
        },
        "StateID": {
          "type": "string",
          "title": "State ID",
          "description": "State ID",
          "order": 30
        },
        "StateType": {
          "type": "string",
          "title": "State Type",
          "description": "State type",
          "order": 31
        },
        "TicketID": {
          "type": "integer",
          "title": "Ticket ID",
          "description": "Ticket ID",
          "order": 32
        },
        "TicketNumber": {
          "type": "string",
          "title": "Ticket Number",
          "description": "Ticket number",
          "order": 33
        },
        "TimeUnit": {
          "type": "number",
          "title": "Time Unit",
          "description": "Time unit",
          "order": 34
        },
        "Title": {
          "type": "string",
          "title": "Title",
          "description": "Title",
          "order": 35
        },
        "Type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 36
        },
        "TypeID": {
          "type": "string",
          "title": "Type ID",
          "description": "Type ID",
          "order": 37
        },
        "UnlockTimeout": {
          "type": "string",
          "title": "Unlock Timeout",
          "description": "Unlock timeout",
          "order": 38
        },
        "UntilTime": {
          "type": "integer",
          "title": "Until Time",
          "description": "Until time",
          "order": 39
        }
      },
      "definitions": {
        "Article": {
          "type": "object",
          "title": "Article",
          "properties": {
            "ArticleID": {
              "type": "string",
              "title": "Article ID",
              "description": "Article ID",
              "order": 1
            },
            "ArticleNumber": {
              "type": "integer",
              "title": "Article Number",
              "description": "Article number",
              "order": 2
            },
            "Attachment": {
              "type": "array",
              "title": "Attachment",
              "description": "Attachment",
              "items": {
                "$ref": "#/definitions/Attachment"
              },
              "order": 3
            },
            "Bcc": {
              "type": "string",
              "title": "BCC",
              "description": "BCC",
              "order": 4
            },
            "Body": {
              "type": "string",
              "title": "Body",
              "description": "Body",
              "order": 5
            },
            "Cc": {
              "type": "string",
              "title": "CC",
              "description": "CC",
              "order": 6
            },
            "ChangeBy": {
              "type": "string",
              "title": "Change By",
              "description": "Change by",
              "order": 7
            },
            "ChangeTime": {
              "type": "string",
              "title": "Change Time",
              "description": "Change time",
              "order": 8
            },
            "Charset": {
              "type": "string",
              "title": "Chartset",
              "description": "Charset",
              "order": 9
            },
            "CommunicationChannelID": {
              "type": "string",
              "title": "Communication Channel ID",
              "description": "Communication channel ID",
              "order": 10
            },
            "ContentCharset": {
              "type": "string",
              "title": "Content Charset",
              "description": "Content charset",
              "order": 11
            },
            "ContentType": {
              "type": "string",
              "title": "Content Type",
              "description": "Content type",
              "order": 12
            },
            "CreateBy": {
              "type": "string",
              "title": "Create By",
              "description": "Create by",
              "order": 13
            },
            "CreateTime": {
              "type": "string",
              "title": "Create Time",
              "description": "Create time",
              "order": 14
            },
            "From": {
              "type": "string",
              "title": "From",
              "description": "From",
              "order": 15
            },
            "InReplyTo": {
              "type": "string",
              "title": "In Reply To",
              "description": "In reply to",
              "order": 16
            },
            "IncomingTime": {
              "type": "string",
              "title": "Incoming Time",
              "description": "Incoming time",
              "order": 17
            },
            "IsVisibleForCustomer": {
              "type": "integer",
              "title": "Is Visible For Customer",
              "description": "Is visible For customer",
              "order": 18
            },
            "MessageID": {
              "type": "string",
              "title": "Message ID",
              "description": "Message ID",
              "order": 19
            },
            "MimeType": {
              "type": "string",
              "title": "MIME Type",
              "description": "MIME type",
              "order": 20
            },
            "References": {
              "type": "string",
              "title": "References",
              "description": "References",
              "order": 21
            },
            "ReplyTo": {
              "type": "string",
              "title": "Reply To",
              "description": "Reply to",
              "order": 22
            },
            "SenderType": {
              "type": "string",
              "title": "Sender type",
              "description": "Sender type",
              "order": 23
            },
            "SenderTypeID": {
              "type": "string",
              "title": "Sender Type ID",
              "description": "Sender type ID",
              "order": 24
            },
            "Subject": {
              "type": "string",
              "title": "Subject",
              "description": "Subject",
              "order": 25
            },
            "TicketID": {
              "type": "integer",
              "title": "Ticket ID",
              "description": "Ticket ID",
              "order": 26
            },
            "TimeUnit": {
              "type": "number",
              "title": "Time Unit",
              "description": "Time unit",
              "order": 27
            },
            "To": {
              "type": "string",
              "title": "To",
              "description": "To",
              "order": 28
            }
          },
          "definitions": {
            "Attachment": {
              "type": "object",
              "title": "Attachment",
              "properties": {
                "Content": {
                  "type": "string",
                  "title": "Content",
                  "description": "Content",
                  "order": 1
                },
                "ContentAlternative": {
                  "type": "string",
                  "title": "Content Alternative",
                  "description": "Content alternative",
                  "order": 2
                },
                "ContentID": {
                  "type": "string",
                  "title": "Content ID",
                  "description": "Content ID",
                  "order": 3
                },
                "ContentType": {
                  "type": "string",
                  "title": "Content Type",
                  "description": "Content type",
                  "order": 4
                },
                "Disposition": {
                  "type": "string",
                  "title": "Dispostion",
                  "description": "Dispostion",
                  "order": 5
                },
                "FileID": {
                  "type": "string",
                  "title": "File ID",
                  "description": "File ID",
                  "order": 6
                },
                "Filename": {
                  "type": "string",
                  "title": "Filename",
                  "description": "Filename",
                  "order": 7
                },
                "FilesizeRaw": {
                  "type": "integer",
                  "title": "File Size Raw",
                  "description": "File size raw",
                  "order": 8
                }
              }
            }
          }
        },
        "Attachment": {
          "type": "object",
          "title": "Attachment",
          "properties": {
            "Content": {
              "type": "string",
              "title": "Content",
              "description": "Content",
              "order": 1
            },
            "ContentAlternative": {
              "type": "string",
              "title": "Content Alternative",
              "description": "Content alternative",
              "order": 2
            },
            "ContentID": {
              "type": "string",
              "title": "Content ID",
              "description": "Content ID",
              "order": 3
            },
            "ContentType": {
              "type": "string",
              "title": "Content Type",
              "description": "Content type",
              "order": 4
            },
            "Disposition": {
              "type": "string",
              "title": "Dispostion",
              "description": "Dispostion",
              "order": 5
            },
            "FileID": {
              "type": "string",
              "title": "File ID",
              "description": "File ID",
              "order": 6
            },
            "Filename": {
              "type": "string",
              "title": "Filename",
              "description": "Filename",
              "order": 7
            },
            "FilesizeRaw": {
              "type": "integer",
              "title": "File Size Raw",
              "description": "File size raw",
              "order": 8
            }
          }
        },
        "DynamicField": {
          "type": "object",
          "title": "DynamicField",
          "properties": {
            "Name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 1
            },
            "Value": {
              "type": "array",
              "title": "Value",
              "description": "Value",
              "items": {
                "type": "string"
              },
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
