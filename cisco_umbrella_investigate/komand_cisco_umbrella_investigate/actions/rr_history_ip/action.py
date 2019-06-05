import komand
from .schema import RrHistoryIpInput, RrHistoryIpOutput
# Custom imports below
from IPy import IP as IP_Validate


class RrHistoryIp(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='rr_history_ip',
                description='Return the history that Umbrella has seen for a given IP address',
                input=RrHistoryIpInput(),
                output=RrHistoryIpOutput())

    def run(self, params={}):
        IP = params.get('IP')
        try:
            IP_Validate(IP)
        except Exception as e:
            self.logger.error("RrHistoryIp: Run: Wrong IP format")
            raise e

        try:
            type = params.get('type')
            if not type:
                rr_history = self.connection.investigate.rr_history(IP)
            else:
                rr_history = self.connection.investigate.rr_history(IP, type)
        except Exception as e:
            self.logger.error("RrHistoryIp: Run: Problem with request")
            raise e

        return {"features": [rr_history.get("features")], "rrs": rr_history.get("rrs")}

    def test(self):
        return {"features": [], "rrs": []}
