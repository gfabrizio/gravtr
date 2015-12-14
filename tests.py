import hashlib
import unittest

from gravtr import Gravtr

class GravtrTestCase(unittest.TestCase):
    def setUp(self):
        self.email = "gfabricio@gmail.com".encode('utf-8')
        self.gravtr_url = ("http://www.gravatar.com/avatar/" +
                     hashlib.md5(self.email).hexdigest())


    def test_generate_url_should_succeed(self):
        gravtr = Gravtr(email=self.email)
        assert self.gravtr_url, gravtr.generate()


if __name__ == '__main__':
    unittest.main()
