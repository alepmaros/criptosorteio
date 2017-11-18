from datetime import datetime
from xml.dom import minidom
import urllib.request
import pytz


class RBeacon:
    def __init__(self):
        self.time_zone = pytz.timezone("America/Sao_Paulo")
        self.url_str = 'https://beacon.nist.gov/rest/record/'

    def get_output_value(self, timestamp):
        """
        Function to get the output value from NIST Randomness Beacon with a specific timestamp
        """
        timestamp = int(timestamp)
        try:
            url = urllib.request.urlopen(self.url_str + str(timestamp))
            xmldoc = minidom.parseString(url.read())
            response = {
                'valid'          : True,
                'timestamp'      : timestamp,
                'timestamp_value': xmldoc.getElementsByTagName('timeStamp')[0].firstChild.data,
                'output_value'   : xmldoc.getElementsByTagName('outputValue')[0].firstChild.data
            }
        except urllib.error.HTTPError:
            response = {
                'valid'     : False,
                'timestamp' : timestamp
            }
        
        return response

    def get_output_value_now(self):
        """
        Get the outputValue from current timestamp. Usually results in 404 errors.
        """
        return self.get_output_value(datetime.now(tz=self.time_zone).timestamp())