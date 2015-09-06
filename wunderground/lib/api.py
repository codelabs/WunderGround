import yaml
import requests
import json

class WunderGround(object):

    'API to get weather information from Wundeground public webservices'

    def __init__(self, keyfile='/tmp/keyfile.yml'):

        __kf   = open(keyfile, 'r')
        __data = yaml.safe_load(__kf)
        __kf.close();

        self.key     = __data["key"]
        self.keyfile = keyfile
        self.url     = "http://api.wunderground.com/api/" + self.key

    def get_conditions_by_zipcode(self, zipcode):

        url     = self.url + "/geolookup/conditions/q/" + str(zipcode) + ".json"
        headers = {
            "Host"         : "api.wunderground.com",
            "X-Target-URI" : "http://api.wunderground.com",
            "Connection"   : "Keep-Alive"
        }

        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != requests.codes.ok:
            return None

        content  = response.json()
        return {
            "city"              : content["location"]["city"],
            "state"             : content["location"]["state"],
            "latitude"          : content["location"]["lat"],
            "longitude"         : content["location"]["lon"],
            "elevation"         : content["display_location"]["elevation"],
            "temp_f"            : content["temp_f"],
            "temp_c"            : content["temp_c"],
            "observation_epoch" : content["observation_epoch"],
        }

