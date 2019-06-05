# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ATTACK_GROUP_ID = "attack_group_ID"
    POLICY_ID = "policy_id"
    

class Output:
    ACTION_POLICY = "action_policy"
    

class RetrieveAttackGroupsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attack_group_ID": {
      "type": "string",
      "title": "Attack Group ID",
      "description": "Attack group ID",
      "order": 2
    },
    "policy_id": {
      "type": "string",
      "title": "Policy Id",
      "description": "ID of security policy",
      "order": 1
    }
  },
  "required": [
    "policy_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RetrieveAttackGroupsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "action_policy": {
      "type": "array",
      "title": "Action Policy",
      "description": "Attack groups information",
      "items": {
        "$ref": "#/definitions/action_policy"
      },
      "order": 1
    }
  },
  "required": [
    "action_policy"
  ],
  "definitions": {
    "action_policy": {
      "type": "object",
      "title": "action_policy",
      "properties": {
        "action": {
          "type": "string",
          "title": "Action",
          "description": "The action to be taken for an invalid request",
          "enum": [
            "none",
            "protect_and_log",
            "allow_and_log",
            "protect_with_no_log"
          ],
          "order": 1
        },
        "deny_response": {
          "type": "string",
          "title": "Deny Response",
          "description": "The response to be sent to the client if the request is denied",
          "enum": [
            "close_connection",
            "send_response",
            "temporary_redirect",
            "permanent_redirect"
          ],
          "order": 2
        },
        "follow_up_action": {
          "type": "string",
          "title": "Follow Up Action",
          "description": "The follow up action to be taken if the request is denied",
          "enum": [
            "none",
            "block_client_ip",
            "challenge_with_captcha"
          ],
          "order": 5
        },
        "follow_up_action_time": {
          "type": "integer",
          "title": "Follow Up Action Time",
          "description": "The time in seconds to block the client IP",
          "order": 6
        },
        "redirect_url": {
          "type": "string",
          "title": "Redirect Url",
          "description": "The URL to be used to redirect the request",
          "order": 3
        },
        "response_page": {
          "type": "string",
          "title": "Response Page",
          "description": "The response page to be sent to the client",
          "enum": [
            "default",
            "default-virus",
            "default-error-resp",
            "default-captcha-tries-error-page",
            "default-captcha-sessions-error-page",
            "default-suspected-activity-error-page",
            "default-captcha-response-page"
          ],
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
