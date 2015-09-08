import json, requests, logging

class WunderGround():

    'API to get weather information from Wundeground public webservices'

    def __init__(self, apikey):
        """
        Constructor

        :param apikey: String - Wunderground's API key.
        :returns: instance
        """
        self.__apikey = apikey
        self.url      = "http://api.wunderground.com/api/" + self.__apikey

    def __request(self, url, headers, timeout):

        response = requests.get(url,headers = headers, timeout = timeout)
        logging.info( "url=" + url + " status_code=" + str(response.status_code) )

        if response.status_code != requests.codes.ok: return None
        return response.json()


    def get_conditions_by_zipcode(self, zipcode):
        """
        Returns current conditions with geo lookup info for given zipcode

        :param zipcode: Number - Condtions for selected zipcode
        :returns: dictionary with all weather and geo data
        """

        url     = self.url + "/geolookup/conditions/q/" + str(zipcode) + ".json"
        headers = {
            "Host"         : "api.wunderground.com",
            "X-Target-URI" : "http://api.wunderground.com",
            "Connection"   : "Keep-Alive"
        }

        result = self.__request(url, headers, 5)
        return result

    def get_conditions_by_city(self, city, state):
        """
        Returns current conditions with given city state/country

        :param city: String - City name
        :param state: String - state code for US states, country name for non US states
        :returns: dictionary with all weather data
        """

        # Replace all spaces in city with underscores
        city = city.replace(" ", "_")
        url  = self.url + "/conditions/q/" + state + "/" + city + ".json"
        headers = {
            "Host"         : "api.wunderground.com",
            "X-Target-URI" : "http://api.wunderground.com",
            "Connection"   : "Keep-Alive"
        }

        result = self.__request(url, headers, 5)
        return result


