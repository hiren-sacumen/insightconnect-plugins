import komand
from .schema import DecrInput, DecrOutput
# Custom imports below
import socket


class Decr(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='decr',
                description='This action is used to decrement a counter',
                input=DecrInput(),
                output=DecrOutput())

    def run(self, params={}):
        instance = self.connection.instance
        stat = params.get('stat')
        count = params.get('count', 1)
        if count == 0: count = 1
        rate = params.get('rate', 1)
        instance.decr(stat, count, rate)
        return { 'stat': stat, 'decrement': count }

    def test(self):
        host = self.connection.host
        port = self.connection.port
        protocol = self.connection.protocol
        try:
            socket.inet_aton(host) # Check if is correct ip address
        except socket.error: # DNS
            try:
                socket.gethostbyname(host)
            except socket.error:
                self.logger.error('Hostname %s cannot be resolved by DNS' % host)
                raise
        if protocol == 'TCP':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5) # Setting 5 sec of timeout
            result = sock.connect_ex((host,port))
            if result != 0:
                self.logger.error('Port %d is not open' % port)
                raise Exception
        return { 'host': host, 'port': port, 'protocol': protocol }
