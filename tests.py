import hashlib
import unittest
import re

from gravtr import Gravtr

class GravtrTestCase(unittest.TestCase):
    def setUp(self):
        self.email = "gfabricio@gmail.com"
        self.gravtr_url = ("http://www.gravatar.com/avatar/" +
                     hashlib.md5(self.email.encode('utf-8')).hexdigest())

    def test_generate_url_should_succeed(self):
        gravtr = Gravtr(email=self.email)
        assert self.gravtr_url, gravtr.generate()

    def test_generate_url_with_specified_size_should_succeed(self):
        gravtr = Gravtr(email=self.email).generate(size=200)
        assert re.search(ur"(\?|\&)s\=200", gravtr)

    def test_generate_url_with_type_should_succeed(self):
        gravtr = Gravtr(email=self.email).generate(typed=True, size=200)
        assert re.search(ur"\.jpg", gravtr)

    def test_generate_url_with_default_should_succeed(self):
        default_image = 'http://example.com/image.jpg'
        gravtr = Gravtr(email=self.email).generate(default=default_image, size=200)
        assert re.search(ur"(\?|\&)d\=http\%3A\%2F\%2Fexample\.com\%2Fimage\.jpg", gravtr)

    def test_generate_url_with_force_default_should_succeed(self):
        default_image = 'http://example.com/image.jpg'
        gravtr = Gravtr(email=self.email).generate(default=default_image, force_default=True)
        assert re.search(ur"(\?|\&)d\=http\%3A\%2F\%2Fexample\.com\%2Fimage\.jpg", gravtr)
        assert re.search(ur"(\?|\&)f\=y", gravtr)

    def test_generate_url_with_rating_type_should_succeed(self):
        gravtr = Gravtr(email=self.email).generate(typed=True, rating_type=Gravtr.ratingType.X)
        assert re.search(ur"(\?|\&)r\=x", gravtr)

if __name__ == '__main__':
    unittest.main()
