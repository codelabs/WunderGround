import yaml
import requests
import json

class WunderGround(object):

    def __init__(self, keyfile='/tmp/keyfile.yml'):

        kf   = open(keyfile, 'r')
        data = yaml.safe_load(kf)
        kf.close();

        self.key     = data["key"]
        self.keyfile = keyfile
        self.url     = "http://api.wunderground.com/api/" + self.key + "/geolookup/conditions/q"

    def by_zipcode(self, zipcode):

        url     = self.url + "/" + str(zipcode) + ".json"
        headers = {
            "Host"         : "api.wunderground.com",
            "X-Target-URI" : "http://api.wunderground.com",
            "Connection"   : "Keep-Alive"
        }

        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != requests.codes.ok:
            return None

        content  = response.json()
        return content

