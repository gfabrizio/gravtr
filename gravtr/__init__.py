import hashlib

GRAVATAR_URL = 'http://www.gravatar.com/avatar/'

class Gravtr(object):
    def __init__(self, email):
        self.email = email

    def generate(self):
        email = self.email.encode('utf-8')
        self.url = GRAVATAR_URL + hashlib.md5(email).hexdigest()
        return self.url
