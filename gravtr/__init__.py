import hashlib

GRAVATAR_URL = 'http://www.gravatar.com/avatar/'

class Gravtr(object):
    def __init__(self, email):
        self.email = email

    def generate(self, size=None):
        email = self.email.encode('utf-8')
        self.url = GRAVATAR_URL + hashlib.md5(email).hexdigest()
        if size:
            self.url = self.url + '?' + 's={}'.format(str(size))
        return self.url
