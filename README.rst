:WunderGround API |build_status| |coverage_status|

Python API to get weather data from Wunderground public web services

Requires to have API key from wunderground. Goto <http://wunderground.com> to get your free developer API key

To use the API

.. code-block:: python

   from wunderground import WunderGround

   client = WunderGround("your api key")

   # Get current conditions for a zipcode
   zip_current = client.get_conditions_by_zipcode("94085")

   # Get current conitions for a city
   city_current = client.get_conditions_by_city("Sunnyvale", "CA")

.. |build_status| image:: https://travis-ci.org/codelabs/WunderGround.svg?branch=master
   :target: https://travis-ci.org/codelabs/WunderGround

.. |coverage_status| image:: https://coveralls.io/repos/codelabs/WunderGround/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/codelabs/WunderGround?branch=master

