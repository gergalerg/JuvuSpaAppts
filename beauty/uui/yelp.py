"""Formely Yelp's API Python example"""

import simplejson as json
import oauth2
import urllib

class YelpApi:
    "Gets search results from Yelp"

    def __init__(self, term, location, limit):
        self.api = 'http://api.yelp.com/v2/search?'
        self.term = term
        self.location = location
        self.limit = limit
        self.us_url = self.unsigned_url()
        self.s_url = self.signed_url()
        self.data = self.load()
        self.x, self.providers, self.total, self.region = self.parse()

    def unsigned_url(self):
        t = '&term=' + self.term
        l = '&location=' + self.location
        m = '&limit=' + self.limit
        link = self.api+t+l+m
        return link

    def signed_url(self):
        # My personal Yelp API credentials, revmove before production 
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

    def load(self):
        j = json.load(urllib.urlopen(self.s_url))
        return j

    def parse(self):
        # Yelp JSON result attributes
        providers = self.data['businesses']
        total = self.data['total']
        region = self.data['region']
        
        # Yelp Object Data
        x = []

        for i, provider in enumerate(providers):
            y = []

            if 'name' in provider:
                y.append(provider['name'])

            if 'rating_img_url' in provider:
                y.append(provider['rating_img_url'])

            if 'location' in provider:
                y.append(provider['location'])

            if 'image_url' in provider:
                y.append(provider['image_url'])

            if 'snippet_text' in provider:
                y.append(provider['snippet_text'])

            if 'review_count' in provider:
                y.append(provider['review_count'])

            if 'url' in provider:
                y.append(provider['url'])

            x.append(y)

        """
            ['categories'] # list
            ['display_phone'] # pretty formatted
            ['id']
            ['image_url']
            ['location'] # querydict
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

        return x, providers, total, region
