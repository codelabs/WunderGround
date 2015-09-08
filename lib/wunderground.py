import json, requests, logging

class WunderGround(object):

    'API to get weather information from Wundeground public webservices'

    def __init__(self, apikey):
        self.__apikey = apikey
        self.url      = "http://api.wunderground.com/api/" + self.__apikey

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

