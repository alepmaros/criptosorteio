 
from datetime import datetime
from xml.dom import minidom
import pytz
import urllib.request

class RBeacon:
    def __init__(self):
        self.tz = pytz.timezone("America/Sao_Paulo")
        self.url_str = 'https://beacon.nist.gov/rest/record/'

    def getOutputValue(self, timestamp):
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

    def getOutputValueNow(self):
        return self.getOutputValue(datetime.now(tz=self.tz).timestamp())