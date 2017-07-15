[![Code Health](https://landscape.io/github/gfabricio/gravtr/master/landscape.svg?style=flat)](https://landscape.io/github/gfabricio/gravtr/master)  [![Build Status](https://travis-ci.org/gfabricio/gravtr.svg)](https://travis-ci.org/gfabricio/gravtr)  [![Codacy Badge](https://api.codacy.com/project/badge/grade/a45c40b0e1a945319012ef3382f63eae)](https://www.codacy.com/app/gfabricio/gravtr) [![PyPI Downloads](http://img.shields.io/pypi/dm/gravtr.svg)](https://pypi.python.org/pypi/gravtr)
----
# Gravtr
A simple package to generate a gravatar url
---
## Installation:
```
$ pip install gravtr
```
---
## Usage:
```
>>> from gravtr import Gravtr
>>> gravtr = Gravtr("gfabricio@tests.com")
>>> gravtr.generate()
'https://www.gravatar.com/avatar/1c0d59fd98fb89ba3a4f3ea950d31e1e'
```
- You could specify the size of the returned image (by default is 80px):
```
>>> gravtr.generate(size=2048)
'https://www.gravatar.com/avatar/1c0d59fd98fb89ba3a4f3ea950d31e1e?s=2048'
```

- You can specify if you want an http link instead of an https one:
```
>>> gravtr.generate(unsecure=True)
'http://www.gravatar.com/avatar/1c0d59fd98fb89ba3a4f3ea950d31e1e'
```

- You can set a default image to render instead of the default one from Gravatar:
```
>>> gravtr.generate(default=http://example.com/image.jpg)
'https://www.gravatar.com/avatar/1c0d59fd98fb89ba3a4f3ea950d31e1e?d=http%3A%2F%2Fexample.com%2Fimage.jpg'
```

- If for some reason you wanted to force the default image to always load, you can do that by using the force_default parameter
```
>>> gravtr.generate(force_default=True)
'https://www.gravatar.com/avatar/1c0d59fd98fb89ba3a4f3ea950d31e1e?f=y'
```

- Gravatar allows users to self-rate their images so that they can indicate if an image is appropriate for a certain audience. By default, only 'G' rated images are displayed unless you indicate that you would like to see higher ratings. You can do that with the rating_type parameter.
4 values are available as constant under `Gravtr.ratingType` : G, PG, R, X

More information about them here: https://fr.gravatar.com/site/implement/images#rating
```
>>> gravtr.generate(rating_type=Gravtr.ratingType.PG)
'https://www.gravatar.com/avatar/1c0d59fd98fb89ba3a4f3ea950d31e1e?r=pg'
```





Enjoy! :)


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/gfabricio/gravtr/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

