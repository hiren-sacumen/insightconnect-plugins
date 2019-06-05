# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create user account"


class Input:
    ADDRESS = "address"
    EXEMPT_DEVICE = "exempt_device"
    JOB_TITLE = "job_title"
    LOGIN = "login"
    NAME = "name"
    PHONE = "phone"
    ROLE = "role"
    SPACE_AMOUNT = "space_amount"
    SYNC = "sync"
    TIMEZONE = "timezone"
    TWO_FACTOR = "two_factor"
    

class Output:
    ADDRESS = "address"
    AVATAR_URL = "avatar_url"
    EXEMPT_DEVICE = "exempt_device"
    ID = "id"
    JOB_TITLE = "job_title"
    LOGIN = "login"
    NAME = "name"
    PHONE = "phone"
    SPACE_AMOUNT = "space_amount"
    SYNC = "sync"
    TIMEZONE = "timezone"
    TWO_FACTOR = "two_factor"
    

class CreateUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Street Address",
      "description": "User's street address",
      "order": 7
    },
    "exempt_device": {
      "type": "boolean",
      "title": "Exempt Device Limits",
      "description": "Exempt this user from Enterprise device limits",
      "order": 11
    },
    "job_title": {
      "type": "string",
      "title": "Job Title",
      "description": "User's job title",
      "order": 5
    },
    "login": {
      "type": "string",
      "title": "Login",
      "description": "Login email",
      "order": 1
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Username",
      "order": 2
    },
    "phone": {
      "type": "string",
      "title": "Phone",
      "description": "User's phone number",
      "order": 6
    },
    "role": {
      "type": "string",
      "title": "Role",
      "description": "Enterprise role e.g. coadmin, user",
      "default": "User",
      "enum": [
        "Coadmin",
        "User"
      ],
      "order": 3
    },
    "space_amount": {
      "type": "number",
      "title": "Space Amount",
      "description": "User's total available space amount in bytes",
      "order": 8
    },
    "sync": {
      "type": "boolean",
      "title": "Sync",
      "description": "Whether or not this user can use Box Sync",
      "order": 4
    },
    "timezone": {
      "type": "string",
      "title": "Timezone",
      "description": "User's timezone",
      "order": 9
    },
    "two_factor": {
      "type": "boolean",
      "title": "Two-Factor Auth",
      "description": "Exempt two-factor authentication",
      "order": 10
    }
  },
  "required": [
    "login",
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "User Address",
      "description": "User address",
      "order": 11
    },
    "avatar_url": {
      "type": "string",
      "title": "User Avatar",
      "description": "User avatar",
      "order": 12
    },
    "exempt_device": {
      "type": "boolean",
      "title": "Device Limits Exemption",
      "description": "Device limits exemption",
      "order": 7
    },
    "id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID",
      "order": 2
    },
    "job_title": {
      "type": "string",
      "title": "Job Title",
      "description": "Job title",
      "order": 9
    },
    "login": {
      "type": "string",
      "title": "User Email",
      "description": "User email",
      "order": 1
    },
    "name": {
      "type": "string",
      "title": "Username",
      "description": "Username",
      "order": 3
    },
    "phone": {
      "type": "string",
      "title": "User Phone Number",
      "description": "User phone number",
      "order": 10
    },
    "space_amount": {
      "type": "number",
      "title": "Max Space Amount",
      "description": "Max space amount",
      "order": 5
    },
    "sync": {
      "type": "boolean",
      "title": "Sync",
      "description": "Sync",
      "order": 6
    },
    "timezone": {
      "type": "string",
      "title": "Timezone",
      "description": "Timezone",
      "order": 4
    },
    "two_factor": {
      "type": "boolean",
      "title": "Login Verification Exemption",
      "description": "Login verification exemption",
      "order": 8
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
