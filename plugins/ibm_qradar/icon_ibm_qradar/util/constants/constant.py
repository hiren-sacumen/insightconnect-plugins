"""Character constants."""
EMPTY_STR = ""
COLON_STR = ":"
FORWARD_SLASH_STR = "/"
AQL = "AQL"
SEARCH_ID = "search_id"
POLL_INTERVAL = "poll_interval"
# Regex constants
ENDPOINT_RGX = r"(\/)+$"
HTTPS = "https"
# Http URL connector
CONNECTOR = f"{COLON_STR}{FORWARD_SLASH_STR}{FORWARD_SLASH_STR}"

SUCCESS_RESPONSE_CODE = [201, 200, 206]
INTERNAL_SERVER_ERROR = "Internal Server Error in Qradar Instance"

# methods

POST = "POST"
GET = "GET"
