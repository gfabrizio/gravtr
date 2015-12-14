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

    def test_generate_url_with_specified_size_should_succeed(self):
        gravtr = Gravtr(email=self.email)
        assert self.gravtr_url + '?' + str(200), gravtr.generate(size=200)


if __name__ == '__main__':
    unittest.main()
