import unittest
import os, sys
import requests
import requests_mock

sys.path.append(os.path.abspath(sys.path[0]) + '/../')

from lib import api

class TestWunderGround( unittest.TestCase ):

    def test_init(self):

        wg = api.WunderGround()

        self.assertEqual(wg.keyfile, "/tmp/keyfile.yml")
        self.assertEqual(wg.key, 'abcfsssd')
        self.assertEqual(wg.url, "http://api.wunderground.com/api/abcfsssd/geolookup/conditions/q")

    def test_by_zipcode(self):

        wg      = api.WunderGround()
        zipcode = 95035

        with requests_mock.Mocker() as m:
            m.get(wg.url + '/' + str(zipcode) + '.json', json = {"foo":"bar"})

        data = wg.by_zipcode('95035')
        print data


if __name__ == '__main__':
    unittest.main()

