### WunderGround API [![Build Status](https://travis-ci.org/codelabs/WunderGround.svg?branch=master)](https://travis-ci.org/codelabs/WunderGround) [![Coverage Status](https://coveralls.io/repos/codelabs/WunderGround/badge.svg?branch=master&service=github)](https://coveralls.io/github/codelabs/WunderGround?branch=master)

Python API to get weather data from Wunderground public web services

Help on module wunderground:

NAME
    wunderground

FILE
    /home/ec2-user/WunderGround/lib/wunderground.py

CLASSES
    WunderGround
    
    class WunderGround
     |  API to get weather information from Wundeground public webservices
     |  
     |  Methods defined here:
     |  
     |  __init__(self, apikey)
     |      Constructor
     |      
     |      :param apikey: String - Wunderground's API key.
     |      :returns: instance
     |  
     |  get_conditions_by_city(self, city, state)
     |      Returns current conditions with given city state/country
     |      
     |      :param city: String - City name
     |      :param state: String - state code for US states, country name for non US states
     |      :returns: dictionary with all weather data
     |  
     |  get_conditions_by_zipcode(self, zipcode)
     |      Returns current conditions with geo lookup info for given zipcode
     |      
     |      :param zipcode: Number - Condtions for selected zipcode
     |      :returns: dictionary with all weather and geo data


