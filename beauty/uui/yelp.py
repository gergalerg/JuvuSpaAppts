"""Formely Yelp's API Python example"""
"""Now SpaStalker's Yelp class"""

"""YelpApi takes three parameters: a search term, a location, and result limit."""
"""Class passes back raw JSON data, total item count, region, and parsed results."""
"""Uses OAuth for handshaking and data request."""


import simplejson as json
import oauth2
import urllib

class YelpApi:
    "Gets search results from Yelp"

    def __init__(self, search_term, location, result_limit):
        self.api = 'http://api.yelp.com/v2/search?'
        self.search_term, self.location, self.result_limit = search_term, location, result_limit
        self.us_url = self.unsigned_url()
        self.s_url = self.signed_url()
        self.jsondata, self.total, self.region, self.results = self.parse()

    def unsigned_url(self):
        t = '&term=' + self.search_term
        l = '&location=' + self.location
        m = '&limit=' + self.result_limit
        link = self.api+t+l+m
        return link

    def signed_url(self):
        # jw: My personal Yelp API keys, remove before production 
        consumer_key = 'KJ6cR0iz4AFgyTiWI3rqVQ'
        consumer_secret = 'ASkzCfW9DJzOwrqJLIOxipeCe40'
        token = 'u5h0Xg8GKxDkld-D0i1A_m5udCxv4ka4'
        token_secret = '-PQcVtbGyx_lWiti1NvXBB76F7U'

        consumer = oauth2.Consumer(consumer_key, consumer_secret)
        url = self.us_url

        oauth_request = oauth2.Request('GET', url, {})
        oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                      'oauth_timestamp': oauth2.generate_timestamp(),
                      'oauth_token': token,
                      'oauth_consumer_key': consumer_key})

        token = oauth2.Token(token, token_secret)

        oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)

        signed_url = oauth_request.to_url()

        return signed_url

    def parse(self):
        # Yelp JSON result attributes
        jsondata = json.load(urllib.urlopen(self.s_url))
        total = jsondata.get('total')
        region = jsondata.get('region')

        for k, v in jsondata.items():
            results = dict({k: v})
        return jsondata, total, region, results 

        """
            ['categories'] 
            ['display_phone']
            ['id']
            ['image_url']
            ['location']
            ['mobile_url']
            ['name']
            ['phone']
            ['rating']
            ['rating_img_url']
            ['rating_img_url_large']
            ['rating_img_url_small']
            ['review_count']
            ['snippet_image_url']
            ['snippet_text']
            ['url']
        """

