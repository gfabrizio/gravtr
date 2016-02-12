import hashlib

GRAVATAR_URL = 'http://www.gravatar.com/'

class Gravtr(object):
    def __init__(self, email):
        self.email = email

    def email_hash(self):
        email = self.email.encode('utf-8')
        return hashlib.md5(email).hexdigest()

    def generate(self, size=None):
        email = self.email_hash()
        url = GRAVATAR_URL + 'avatar/{}'.format(email)
        if size:
          url = url + 's={}'.format(str(size))
        return url

    def profile(self, format_type=None):
        email = self.email_hash()
        if format_type:
            return GRAVATAR_URL + email +'.{}'.format(format_type)
        return GRAVATAR_URL + email
