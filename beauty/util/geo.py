'''
Work with locations, latitude, longitude, etc...
'''
from pprint import pprint, pformat
from json import load
from urllib import urlopen, quote_plus


def geocode_from_address(address):
    url = (
        'http://maps.googleapis.com/maps/api/geocode/json'
        '?address=%s&sensor=false'
        % quote_plus(address)
        )
    return load(urlopen(url))


def grok_address(status, results):
    assert status == 'OK', pformat(results)
    addy = results[0]
    lat_long = addy['geometry']['location']
    location_full_text = addy['formatted_address']
    return lat_long, location_full_text


if __name__ == '__main__':
    geodata = geocode_from_address("San Francisco, CA")
    pprint(geodata)
    print
    pprint(grok_address(**geodata))
