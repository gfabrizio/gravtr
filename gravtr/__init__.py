import hashlib
import sys
if sys.version_info[0] < 3:
    import urllib
else:
    import urllib.parse as urllib

class Gravtr(object):
    GRAVATAR_URL = 'https://www.gravatar.com/avatar/'
    GRAVATAR_URL_UNSECURE = 'http://www.gravatar.com/avatar/'

    class ratingType(object):
        G = 'g'
        PG = 'pg'
        R = 'r'
        X = 'x'

    def __init__(self, email):
        self.email = email.encode('utf-8')

    def generate(self, unsecure=False, size=None, typed=False, default=None, force_default=False, rating_type=None):
        gravatar_url = self.GRAVATAR_URL if not unsecure else self.GRAVATAR_URL_UNSECURE
        self.url = gravatar_url + hashlib.md5(self.email).hexdigest()
        params = dict()
        if size:
            params['s'] = str(size)
        if typed:
            self.url = self.url + '.jpg'
        if default:
            params['d'] = str(default)
        if force_default:
            params['f'] = 'y'
        if rating_type:
            params['r'] = str(rating_type)
        return self.url + '?' + urllib.urlencode(params)
