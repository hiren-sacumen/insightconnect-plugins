# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ADDRESS = "address"
    PAYMENT_DECLINE_CODE = "payment_decline_code"
    PAYMENT_PROCESSOR = "payment_processor"
    PAYMENT_WAS_AUTHORIZED = "payment_was_authorized"
    

class Output:
    RISK_SCORE = "risk_score"
    

class PaymentLookupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address to query",
      "order": 1
    },
    "payment_decline_code": {
      "type": "string",
      "title": "Payment Decline Code",
      "description": "Payment decline code",
      "order": 4
    },
    "payment_processor": {
      "type": "string",
      "title": "Payment Processor",
      "description": "Payment process ued for transaction",
      "enum": [
        "none",
        "adyen",
        "altapay",
        "amazon_payments",
        "authorizenet",
        "balanced",
        "beanstream",
        "bluepay",
        "braintree",
        "ccnow",
        "chase_paymentech",
        "cielo",
        "collector",
        "compropago",
        "concept_payments",
        "conekta",
        "cuentadigital",
        "dalpay",
        "dibs",
        "digital_river",
        "ecomm365",
        "elavon",
        "epay",
        "eprocessing_network",
        "eway",
        "first_data",
        "global_payments",
        "ingenico",
        "internetsecure",
        "intuit_quickbooks_payments",
        "iugu",
        "mastercard_payment_gateway",
        "mercadopago",
        "merchant_esolutions",
        "mirjeh",
        "mollie",
        "moneris_solutions",
        "nmi",
        "openpaymx",
        "optimal_payments",
        "orangepay",
        "other",
        "pacnet_services",
        "payfast",
        "paygate",
        "payone",
        "paypal",
        "payplus",
        "paystation",
        "paytrace",
        "paytrail",
        "payture",
        "payu",
        "payulatam",
        "pinpayments",
        "princeton_payment_solutions",
        "psigate",
        "qiwi",
        "quickpay",
        "raberil",
        "rede",
        "redpagos",
        "rewardspay",
        "sagepay",
        "simplify_commerce",
        "skrill",
        "smartcoin",
        "sps_decidir",
        "stripe",
        "telerecargas",
        "towah",
        "usa_epay",
        "verepay",
        "vindicia",
        "virtual_card_services",
        "vme",
        "worldpay"
      ],
      "order": 2
    },
    "payment_was_authorized": {
      "type": "boolean",
      "title": "Payment Was Authorized",
      "description": "Payment authroized: true/false",
      "order": 3
    }
  },
  "required": [
    "address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PaymentLookupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "risk_score": {
      "type": "string",
      "title": "Risk Score",
      "description": "Overall risk score",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
