# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ID = "id"
    

class Output:
    POLICIES = "policies"
    

class RetrieveSecurityPoliciesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "ID of the security policies",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RetrieveSecurityPoliciesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "policies": {
      "type": "array",
      "title": "Policies",
      "description": "Array of security policy object",
      "items": {
        "$ref": "#/definitions/security_policy"
      },
      "order": 1
    }
  },
  "required": [
    "policies"
  ],
  "definitions": {
    "cookie_security": {
      "type": "object",
      "title": "cookie_security",
      "properties": {
        "allowUnrecognizedCookies": {
          "type": "string",
          "title": "AllowUnrecognizedCookies",
          "description": "Determines whether unrecognized cookies should be allowed",
          "order": 9
        },
        "cookieMaxAge": {
          "type": "integer",
          "title": "CookieMaxAge",
          "description": "The maximum age for session cookies",
          "order": 3
        },
        "cookieReplayProtectionType": {
          "type": "string",
          "title": "CookieReplayProtectionType",
          "description": "The type of protection to be used to prevent the cookie replay attacks. The enumerated values include",
          "order": 4
        },
        "cookies_exempted": {
          "type": "array",
          "title": "Cookies Exempted",
          "description": "The names of the cookies that needs to be exempted from the cookie security policy",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "customHeaders": {
          "type": "array",
          "title": "CustomHeaders",
          "description": "The custom headers to be used in the cookie if the parameter 'Cookie Replay Protection Type' is set to Custom Headers or IP and Custom Headers",
          "order": 8
        },
        "daysAllowed": {
          "type": "integer",
          "title": "DaysAllowed",
          "description": "The number of days the Barracuda Web Application Firewall to not reject unrecognized cookies",
          "order": 6
        },
        "http_only": {
          "type": "string",
          "title": "Http Only",
          "description": "Determines whether or not the cookie security feature will be enabled for HTTP cookies",
          "enum": [
            "no",
            "yes"
          ],
          "order": 5
        },
        "secureCookie": {
          "type": "integer",
          "title": "SecureCookie",
          "description": "Determines whether to allow or not the cookies if the client makes secure HTTPS connection",
          "order": 1
        },
        "tamperProofMode": {
          "type": "string",
          "title": "TamperProofMode",
          "description": "The tamper proof mode for cookies",
          "order": 7
        }
      }
    },
    "parameter_protection": {
      "type": "object",
      "title": "parameter_protection",
      "properties": {
        "allowedFileUploadType": {
          "type": "string",
          "title": "AllowedFileUploadType",
          "description": "The allowed file upload types",
          "order": 9
        },
        "base64DecodeParameterValue": {
          "type": "string",
          "title": "Base64DecodeParameterValue",
          "description": "Determines whether to apply base64 decoding to the parameter values or not",
          "order": 6
        },
        "blockedAttackTypes": {
          "type": "array",
          "title": "BlockedAttackTypes",
          "description": "The Attack Types to be matched in a request",
          "order": 5
        },
        "customBlockedAttackTypes": {
          "type": "array",
          "title": "CustomBlockedAttackTypes",
          "description": "The custom attack types defined on the ADVANCED \\u003e Libraries page (if any)",
          "order": 8
        },
        "deniedMetaCharacters": {
          "type": "string",
          "title": "DeniedMetaCharacters",
          "description": "The meta-characters to be denied in the parameter value. Meta-characters must be URL encoded. Non-printable characters such as 'backspace' and web interface reserved characters like '?' should be URL encoded",
          "order": 2
        },
        "enable": {
          "type": "string",
          "title": "Enable",
          "description": "Determines whether to enforce parameter protection or not",
          "enum": [
            "yes",
            "no"
          ],
          "order": 1
        },
        "exceptionPatterns": {
          "type": "array",
          "title": "ExceptionPatterns",
          "description": "The patterns to be allowed despite matching a malicious pattern group. Note: Configure the exact 'Pattern Name' displayed on the ADVANCED \\u003e View Internal Patterns page, or as defined when creating a 'New Group' on the ADVANCED \\u003e Libraries page",
          "order": 13
        },
        "fileUploadMimeTypes": {
          "type": "array",
          "title": "FileUploadMimeTypes",
          "description": "The Mime types to be allowed as uploaded files",
          "items": {
            "type": "string"
          },
          "order": 12
        },
        "fileUpload_extensions": {
          "type": "array",
          "title": "FileUpload Extensions",
          "description": "The extensions to be allowed as uploaded files",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "ignoreParameters": {
          "type": "array",
          "title": "IgnoreParameters",
          "description": "The parameters to be exempted from all validations",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "maximumInstances": {
          "type": "integer",
          "title": "MaximumInstances",
          "description": "The maximum number of times a parameter needs to be allowed in a request",
          "order": 11
        },
        "maximumParameterValueLength": {
          "type": "integer",
          "title": "MaximumParameterValueLength",
          "description": "The maximum allowed length of any parameter value, including no-name parameters",
          "order": 10
        },
        "maximumUploadFileSize": {
          "type": "integer",
          "title": "MaximumUploadFileSize",
          "description": "The maximum size (in KB) for an individual file that can be uploaded in a request",
          "order": 4
        }
      }
    },
    "request_limits": {
      "type": "object",
      "title": "request_limits",
      "properties": {
        "enable": {
          "type": "string",
          "title": "Enable",
          "description": "Enforce size limit checks on request headers or not",
          "enum": [
            "yes",
            "no"
          ],
          "order": 1
        },
        "maxCookieNameLength": {
          "type": "integer",
          "title": "MaxCookieNameLength",
          "description": "The maximum allowable length for a cookie name",
          "order": 4
        },
        "maxCookieValueLength": {
          "type": "integer",
          "title": "MaxCookieValueLength",
          "description": "The maximum allowable length for a cookie value",
          "order": 6
        },
        "maxHeaderNameLength": {
          "type": "integer",
          "title": "MaxHeaderNameLength",
          "description": "The maximum allowable length for a header name",
          "order": 3
        },
        "maxHeaderValueLength": {
          "type": "integer",
          "title": "MaxHeaderValueLength",
          "description": "The maximum allowable length for header value in a request",
          "order": 8
        },
        "maxNumberOfCookies": {
          "type": "integer",
          "title": "MaxNumberOfCookies",
          "description": "The maximum number of cookies to be allowed",
          "order": 11
        },
        "maxNumberOfHeaders": {
          "type": "integer",
          "title": "MaxNumberOfHeaders",
          "description": "The maximum number of headers to be allowed in a request",
          "order": 2
        },
        "maxQueryLength": {
          "type": "integer",
          "title": "MaxQueryLength",
          "description": "The maximum allowable length for the query string portion of the URL",
          "order": 5
        },
        "maxRequestLength": {
          "type": "integer",
          "title": "MaxRequestLength",
          "description": "The maximum allowable request length. This includes the Request Line and all HTTP request headers",
          "order": 7
        },
        "maxRequestLineLength": {
          "type": "integer",
          "title": "MaxRequestLineLength",
          "description": "The maximum allowable length for the request line. The request line consists of the method, the URL",
          "order": 10
        },
        "maxURLLength": {
          "type": "integer",
          "title": "MaxURLLength",
          "description": "The maximum allowable URL length including the query string portion of the URL",
          "order": 9
        }
      },
      "required": [
        "enable"
      ]
    },
    "security_policy": {
      "type": "object",
      "title": "security_policy",
      "properties": {
        "allowed_acls": {
          "type": "integer",
          "title": "Allowed Acls",
          "description": "Allowed ACLs",
          "order": 7
        },
        "apply_double_decoding": {
          "type": "string",
          "title": "Apply Double Decoding",
          "description": "Apply double decoding",
          "order": 4
        },
        "character": {
          "type": "string",
          "title": "Character",
          "description": "Default character set",
          "order": 2
        },
        "cloaking": {
          "type": "array",
          "title": "Cloaking",
          "description": "Cloaking",
          "order": 3
        },
        "cookie_protection": {
          "type": "string",
          "title": "Cookie Protection",
          "description": "Cookie protection",
          "order": 13
        },
        "cookie_security": {
          "$ref": "#/definitions/cookie_security",
          "title": "Cookie Security",
          "description": "Cookie security",
          "order": 11
        },
        "data_theft_protection": {
          "type": "array",
          "title": "Data Theft Protection",
          "description": "Data theft protection",
          "order": 5
        },
        "default_character_set": {
          "type": "string",
          "title": "Default character set",
          "description": "Default character set",
          "order": 19
        },
        "disallowed_acls": {
          "type": "integer",
          "title": "Disallowed Acls",
          "description": "Disallowed ACLs",
          "order": 17
        },
        "double_decoding": {
          "type": "string",
          "title": "Double Decoding",
          "description": "Determines whether or not to apply double-decoding of the character set",
          "order": 18
        },
        "id": {
          "type": "string",
          "title": "Id",
          "description": "ID of security policies",
          "order": 1
        },
        "limit_checks": {
          "type": "boolean",
          "title": "Limit Checks",
          "description": "Limit checks",
          "order": 14
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of security policies",
          "order": 15
        },
        "parameter_protection": {
          "$ref": "#/definitions/parameter_protection",
          "title": "Parameter Protection",
          "description": "Parameter protection",
          "order": 9
        },
        "parameter_protection_status": {
          "type": "string",
          "title": "Parameter Protection Status",
          "description": "Parameter protection status",
          "order": 16
        },
        "request_limits": {
          "$ref": "#/definitions/request_limits",
          "title": "Request Limits",
          "description": "Request limits",
          "order": 8
        },
        "url_normalization": {
          "$ref": "#/definitions/url_normalization",
          "title": "Url Normalization",
          "description": "URL normalization",
          "order": 12
        },
        "url_protection": {
          "$ref": "#/definitions/url_protection",
          "title": "Url Protection",
          "description": "URL protection configuration",
          "order": 10
        },
        "url_protection_status": {
          "type": "integer",
          "title": "Url Protection Status",
          "description": "URL protection status",
          "order": 6
        }
      },
      "required": [
        "allowed_acls",
        "cookie_protection",
        "data_theft_protection",
        "request_limits",
        "parameter_protection_status",
        "url_protection_status",
        "apply_double_decoding",
        "url_protection",
        "url_normalization",
        "name",
        "disallowed_acls",
        "id",
        "cloaking",
        "parameter_protection",
        "cookie_security",
        "limit_checks",
        "character"
      ],
      "definitions": {
        "cookie_security": {
          "type": "object",
          "title": "cookie_security",
          "properties": {
            "allowUnrecognizedCookies": {
              "type": "string",
              "title": "AllowUnrecognizedCookies",
              "description": "Determines whether unrecognized cookies should be allowed",
              "order": 9
            },
            "cookieMaxAge": {
              "type": "integer",
              "title": "CookieMaxAge",
              "description": "The maximum age for session cookies",
              "order": 3
            },
            "cookieReplayProtectionType": {
              "type": "string",
              "title": "CookieReplayProtectionType",
              "description": "The type of protection to be used to prevent the cookie replay attacks. The enumerated values include",
              "order": 4
            },
            "cookies_exempted": {
              "type": "array",
              "title": "Cookies Exempted",
              "description": "The names of the cookies that needs to be exempted from the cookie security policy",
              "items": {
                "type": "string"
              },
              "order": 2
            },
            "customHeaders": {
              "type": "array",
              "title": "CustomHeaders",
              "description": "The custom headers to be used in the cookie if the parameter 'Cookie Replay Protection Type' is set to Custom Headers or IP and Custom Headers",
              "order": 8
            },
            "daysAllowed": {
              "type": "integer",
              "title": "DaysAllowed",
              "description": "The number of days the Barracuda Web Application Firewall to not reject unrecognized cookies",
              "order": 6
            },
            "http_only": {
              "type": "string",
              "title": "Http Only",
              "description": "Determines whether or not the cookie security feature will be enabled for HTTP cookies",
              "enum": [
                "no",
                "yes"
              ],
              "order": 5
            },
            "secureCookie": {
              "type": "integer",
              "title": "SecureCookie",
              "description": "Determines whether to allow or not the cookies if the client makes secure HTTPS connection",
              "order": 1
            },
            "tamperProofMode": {
              "type": "string",
              "title": "TamperProofMode",
              "description": "The tamper proof mode for cookies",
              "order": 7
            }
          }
        },
        "parameter_protection": {
          "type": "object",
          "title": "parameter_protection",
          "properties": {
            "allowedFileUploadType": {
              "type": "string",
              "title": "AllowedFileUploadType",
              "description": "The allowed file upload types",
              "order": 9
            },
            "base64DecodeParameterValue": {
              "type": "string",
              "title": "Base64DecodeParameterValue",
              "description": "Determines whether to apply base64 decoding to the parameter values or not",
              "order": 6
            },
            "blockedAttackTypes": {
              "type": "array",
              "title": "BlockedAttackTypes",
              "description": "The Attack Types to be matched in a request",
              "order": 5
            },
            "customBlockedAttackTypes": {
              "type": "array",
              "title": "CustomBlockedAttackTypes",
              "description": "The custom attack types defined on the ADVANCED \\u003e Libraries page (if any)",
              "order": 8
            },
            "deniedMetaCharacters": {
              "type": "string",
              "title": "DeniedMetaCharacters",
              "description": "The meta-characters to be denied in the parameter value. Meta-characters must be URL encoded. Non-printable characters such as 'backspace' and web interface reserved characters like '?' should be URL encoded",
              "order": 2
            },
            "enable": {
              "type": "string",
              "title": "Enable",
              "description": "Determines whether to enforce parameter protection or not",
              "enum": [
                "yes",
                "no"
              ],
              "order": 1
            },
            "exceptionPatterns": {
              "type": "array",
              "title": "ExceptionPatterns",
              "description": "The patterns to be allowed despite matching a malicious pattern group. Note: Configure the exact 'Pattern Name' displayed on the ADVANCED \\u003e View Internal Patterns page, or as defined when creating a 'New Group' on the ADVANCED \\u003e Libraries page",
              "order": 13
            },
            "fileUploadMimeTypes": {
              "type": "array",
              "title": "FileUploadMimeTypes",
              "description": "The Mime types to be allowed as uploaded files",
              "items": {
                "type": "string"
              },
              "order": 12
            },
            "fileUpload_extensions": {
              "type": "array",
              "title": "FileUpload Extensions",
              "description": "The extensions to be allowed as uploaded files",
              "items": {
                "type": "string"
              },
              "order": 3
            },
            "ignoreParameters": {
              "type": "array",
              "title": "IgnoreParameters",
              "description": "The parameters to be exempted from all validations",
              "items": {
                "type": "string"
              },
              "order": 7
            },
            "maximumInstances": {
              "type": "integer",
              "title": "MaximumInstances",
              "description": "The maximum number of times a parameter needs to be allowed in a request",
              "order": 11
            },
            "maximumParameterValueLength": {
              "type": "integer",
              "title": "MaximumParameterValueLength",
              "description": "The maximum allowed length of any parameter value, including no-name parameters",
              "order": 10
            },
            "maximumUploadFileSize": {
              "type": "integer",
              "title": "MaximumUploadFileSize",
              "description": "The maximum size (in KB) for an individual file that can be uploaded in a request",
              "order": 4
            }
          }
        },
        "request_limits": {
          "type": "object",
          "title": "request_limits",
          "properties": {
            "enable": {
              "type": "string",
              "title": "Enable",
              "description": "Enforce size limit checks on request headers or not",
              "enum": [
                "yes",
                "no"
              ],
              "order": 1
            },
            "maxCookieNameLength": {
              "type": "integer",
              "title": "MaxCookieNameLength",
              "description": "The maximum allowable length for a cookie name",
              "order": 4
            },
            "maxCookieValueLength": {
              "type": "integer",
              "title": "MaxCookieValueLength",
              "description": "The maximum allowable length for a cookie value",
              "order": 6
            },
            "maxHeaderNameLength": {
              "type": "integer",
              "title": "MaxHeaderNameLength",
              "description": "The maximum allowable length for a header name",
              "order": 3
            },
            "maxHeaderValueLength": {
              "type": "integer",
              "title": "MaxHeaderValueLength",
              "description": "The maximum allowable length for header value in a request",
              "order": 8
            },
            "maxNumberOfCookies": {
              "type": "integer",
              "title": "MaxNumberOfCookies",
              "description": "The maximum number of cookies to be allowed",
              "order": 11
            },
            "maxNumberOfHeaders": {
              "type": "integer",
              "title": "MaxNumberOfHeaders",
              "description": "The maximum number of headers to be allowed in a request",
              "order": 2
            },
            "maxQueryLength": {
              "type": "integer",
              "title": "MaxQueryLength",
              "description": "The maximum allowable length for the query string portion of the URL",
              "order": 5
            },
            "maxRequestLength": {
              "type": "integer",
              "title": "MaxRequestLength",
              "description": "The maximum allowable request length. This includes the Request Line and all HTTP request headers",
              "order": 7
            },
            "maxRequestLineLength": {
              "type": "integer",
              "title": "MaxRequestLineLength",
              "description": "The maximum allowable length for the request line. The request line consists of the method, the URL",
              "order": 10
            },
            "maxURLLength": {
              "type": "integer",
              "title": "MaxURLLength",
              "description": "The maximum allowable URL length including the query string portion of the URL",
              "order": 9
            }
          },
          "required": [
            "enable"
          ]
        },
        "url_normalization": {
          "type": "object",
          "title": "url_normalization",
          "properties": {
            "defaultCharset": {
              "type": "string",
              "title": "DefaultCharset",
              "description": "The character set decoding type to be used for incoming requests",
              "order": 2
            },
            "detectResponseCharset": {
              "type": "string",
              "title": "DetectResponseCharset",
              "description": "Determines whether or not the Barracuda Web Application Firewall will detect the character set decoding from the response",
              "order": 4
            },
            "double_decoding": {
              "type": "string",
              "title": "Double Decoding",
              "description": "Determines whether or not to apply double-decoding of the character set",
              "order": 3
            },
            "parameter_separators": {
              "type": "string",
              "title": "Parameter Separators",
              "description": "The url-decoded parameter separator to be used",
              "order": 1
            }
          }
        },
        "url_protection": {
          "type": "object",
          "title": "url_protection",
          "properties": {
            "allowedContentTypes": {
              "type": "array",
              "title": "AllowedContentTypes",
              "description": "The list of content types to be allowed in the POST body of a request",
              "items": {
                "type": "string"
              },
              "order": 5
            },
            "allowedMethods": {
              "type": "array",
              "title": "AllowedMethods",
              "description": "The list of allowable methods in a request",
              "items": {
                "type": "string"
              },
              "order": 10
            },
            "blockedAttackTypes": {
              "type": "array",
              "title": "BlockedAttackTypes",
              "description": "The Attack Types to be matched in a request",
              "order": 7
            },
            "csrfPrevention": {
              "type": "string",
              "title": "CsrfPrevention",
              "description": "The Cross-Site Request Forgery (CSRF) prevention for the forms and URLs",
              "order": 9
            },
            "custom_blockedAttackTypes": {
              "type": "array",
              "title": "Custom BlockedAttackTypes",
              "description": "The custom attack types defined on the ADVANCED \\u003e Libraries page (if any)",
              "order": 8
            },
            "enable": {
              "type": "string",
              "title": "Enable",
              "description": "Determines whether to enforce URL protection or not",
              "enum": [
                "yes",
                "no"
              ],
              "order": 1
            },
            "exceptionPatterns": {
              "type": "array",
              "title": "ExceptionPatterns",
              "description": "The patterns to be allowed despite matching a malicious pattern group. Note: Configure the exact 'Pattern Name' displayed on the ADVANCED \\u003e View Internal Patterns page, or as defined when creating a 'New Group' on the ADVANCED \\u003e Libraries page",
              "order": 11
            },
            "maxContentLength": {
              "type": "integer",
              "title": "MaxContentLength",
              "description": "The maximum content length to be allowed for POST request body",
              "order": 3
            },
            "maxParameters": {
              "type": "integer",
              "title": "MaxParameters",
              "description": "The maximum number of parameters to be allowed in a request",
              "order": 4
            },
            "maximumParameterNameLength": {
              "type": "integer",
              "title": "MaximumParameterNameLength",
              "description": "The maximum length of a parameter name in a request",
              "order": 2
            },
            "maximumUploadFiles": {
              "type": "integer",
              "title": "MaximumUploadFiles",
              "description": "The maximum number of files that can be of file-upload type in a request",
              "order": 6
            }
          }
        }
      }
    },
    "url_normalization": {
      "type": "object",
      "title": "url_normalization",
      "properties": {
        "defaultCharset": {
          "type": "string",
          "title": "DefaultCharset",
          "description": "The character set decoding type to be used for incoming requests",
          "order": 2
        },
        "detectResponseCharset": {
          "type": "string",
          "title": "DetectResponseCharset",
          "description": "Determines whether or not the Barracuda Web Application Firewall will detect the character set decoding from the response",
          "order": 4
        },
        "double_decoding": {
          "type": "string",
          "title": "Double Decoding",
          "description": "Determines whether or not to apply double-decoding of the character set",
          "order": 3
        },
        "parameter_separators": {
          "type": "string",
          "title": "Parameter Separators",
          "description": "The url-decoded parameter separator to be used",
          "order": 1
        }
      }
    },
    "url_protection": {
      "type": "object",
      "title": "url_protection",
      "properties": {
        "allowedContentTypes": {
          "type": "array",
          "title": "AllowedContentTypes",
          "description": "The list of content types to be allowed in the POST body of a request",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "allowedMethods": {
          "type": "array",
          "title": "AllowedMethods",
          "description": "The list of allowable methods in a request",
          "items": {
            "type": "string"
          },
          "order": 10
        },
        "blockedAttackTypes": {
          "type": "array",
          "title": "BlockedAttackTypes",
          "description": "The Attack Types to be matched in a request",
          "order": 7
        },
        "csrfPrevention": {
          "type": "string",
          "title": "CsrfPrevention",
          "description": "The Cross-Site Request Forgery (CSRF) prevention for the forms and URLs",
          "order": 9
        },
        "custom_blockedAttackTypes": {
          "type": "array",
          "title": "Custom BlockedAttackTypes",
          "description": "The custom attack types defined on the ADVANCED \\u003e Libraries page (if any)",
          "order": 8
        },
        "enable": {
          "type": "string",
          "title": "Enable",
          "description": "Determines whether to enforce URL protection or not",
          "enum": [
            "yes",
            "no"
          ],
          "order": 1
        },
        "exceptionPatterns": {
          "type": "array",
          "title": "ExceptionPatterns",
          "description": "The patterns to be allowed despite matching a malicious pattern group. Note: Configure the exact 'Pattern Name' displayed on the ADVANCED \\u003e View Internal Patterns page, or as defined when creating a 'New Group' on the ADVANCED \\u003e Libraries page",
          "order": 11
        },
        "maxContentLength": {
          "type": "integer",
          "title": "MaxContentLength",
          "description": "The maximum content length to be allowed for POST request body",
          "order": 3
        },
        "maxParameters": {
          "type": "integer",
          "title": "MaxParameters",
          "description": "The maximum number of parameters to be allowed in a request",
          "order": 4
        },
        "maximumParameterNameLength": {
          "type": "integer",
          "title": "MaximumParameterNameLength",
          "description": "The maximum length of a parameter name in a request",
          "order": 2
        },
        "maximumUploadFiles": {
          "type": "integer",
          "title": "MaximumUploadFiles",
          "description": "The maximum number of files that can be of file-upload type in a request",
          "order": 6
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
