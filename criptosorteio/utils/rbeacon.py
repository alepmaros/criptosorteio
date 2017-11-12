 
from datetime import datetime
import pytz
from xml.dom import minidom
import urllib.request

class RBeacon:
    def __init__(self):
        self.tz = pytz.timezone("America/Sao_Paulo")
        self.url_str = 'https://beacon.nist.gov/rest/record/'

    def getValue(self, timestamp):
        timestamp = int(timestamp)
        print(self.url_str + str(timestamp))
        xml_str = urllib.request.urlopen(self.url_str + str(timestamp)).read()
        xmldoc = minidom.parseString(xml_str)
        print(xmldoc.toprettyxml())

    def getValueNow(self):
        return self.getValue(datetime.now(tz=self.tz).timestamp())


a = RBeacon()
a.getValue(1510526774)