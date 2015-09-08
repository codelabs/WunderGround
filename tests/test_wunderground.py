import unittest
import os, sys
import requests_mock

sys.path.append(os.path.abspath(sys.path[0]) + '/../')

from lib import wunderground


class TestWunderGround( unittest.TestCase ):

    def setUp(self):
        self.obj = wunderground.WunderGround("abcfsssd")

    def tearDown(self):
        del self.obj

    def test_00_doc_string(self):
        self.assertEqual(wunderground.WunderGround.__doc__, 'API to get weather information from Wundeground public webservices')

    def test_01_init(self):
        self.assertEqual(self.obj.url, "http://api.wunderground.com/api/abcfsssd")

    @requests_mock.mock()
    def test_02_get_conditions_by_valid_zipcode(self, m):

        response = {
            "95035" : {
                "location" : {
                    "city"  : "SomeCity",
                    "state" : "CA",
                    "lat"   : "37.76834106",
                    "lon"   : "-122.39418793"
                },
                "display_location" : {
                    "elevation" : "5"
                },
                "temp_f"            : "83.5",
                "temp_c"            : "22.5",
                "observation_epoch" : "1441575478"
            }
        }

        zip = "95035"
        
        m.get(self.obj.url + '/geolookup/conditions/q/' + str(zip) + '.json', json = response[zip], status_code = 200)
        self.assertDictEqual(self.obj.get_conditions_by_zipcode(zip), response[zip])

    @requests_mock.mock()
    def test_03_get_conditions_by_invalid_zipcode(self, m):

        zip = 11
        m.get(self.obj.url + '/geolookup/conditions/q/' + str(zip) + '.json', status_code = 404)
        self.assertEqual(self.obj.get_conditions_by_zipcode(zip), None)

    @requests_mock.mock()
    def test_04_get_conditions_by_fake_city(self, m):

        city  = "Fake"
        state = "CA"
        response = {
           "response": {
                "version": "0.1",
                "termsofService": "http://www.wunderground.com/weather/api/d/terms.html",
                "features": {
                    "conditions": 1
                },
                "error": {
                    "type": "querynotfound",
                    "description": "No cities match your search query"
                }
            }
        }

        m.get(self.obj.url + '/conditions/q/' + state + "/" + city + ".json", json = response, status_code = 200)
        self.assertEqual(self.obj.get_conditions_by_city(city, state), response)

    @requests_mock.mock()
    def test_05_get_conditions_by_fake_city_with_spaces(self, m):

        state = "CA"
        response = {
           "response": {
                "version": "0.1",
                "termsofService": "http://www.wunderground.com/weather/api/d/terms.html",
                "features": {
                    "conditions": 1
                },
                "error": {
                    "type": "querynotfound",
                    "description": "No cities match your search query"
                }
            }
        }

        m.get(self.obj.url + '/conditions/q/' + state + "/Fake_City.json", json = response, status_code = 200)
        self.assertEqual(self.obj.get_conditions_by_city("Fake City", state), response)


if __name__ == '__main__':
    unittest.main()

