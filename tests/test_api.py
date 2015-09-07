import unittest
import os, sys
import requests_mock

sys.path.append(os.path.abspath(sys.path[0]) + '/../')

from lib import api


class TestWunderGround( unittest.TestCase ):

    def test_init(self):

        wg = api.WunderGround()

        self.assertEqual(wg.keyfile, "/tmp/keyfile.yml")
        self.assertEqual(wg.key, 'abcfsssd')
        self.assertEqual(wg.url, "http://api.wunderground.com/api/abcfsssd")

    @requests_mock.mock()
    def test_get_conditions_by_zipcode(self, m):

        weather  = api.WunderGround()
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

        expected = {
            "city"              : "SomeCity",
            "state"             : "CA",
            "latitude"          : "37.76834106",
            "longitude"         : "-122.39418793",
            "elevation"         : "5",
            "temp_f"            : "83.5",
            "temp_c"            : "22.5",
            "observation_epoch" : "1441575478"
        }

        zip = "95035"
        
        # Mocking request.get
        m.get(weather.url + '/geolookup/conditions/q/' + str(zip) + '.json', json = response[zip], status_code = 200)
        # Test
        self.assertDictEqual(weather.get_conditions_by_zipcode(zip), expected, "Valid Response")

        zip = 11
        # Mocking request.get
        m.get(weather.url + '/geolookup/conditions/q/' + str(zip) + '.json', status_code = 404)
        # Test
        self.assertEqual(weather.get_conditions_by_zipcode(zip), None, "Invalid Response")



if __name__ == '__main__':
    unittest.main()

