[![Code Health](https://landscape.io/github/gfabricio/gravtr/master/landscape.svg?style=flat)](https://landscape.io/github/gfabricio/gravtr/master) | [![Build Status](https://travis-ci.org/gfabricio/gravtr.svg)](https://travis-ci.org/gfabricio/gravtr) | [![Codacy Badge](https://api.codacy.com/project/badge/grade/a45c40b0e1a945319012ef3382f63eae)](https://www.codacy.com/app/gfabricio/gravtr)

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
'http://www.gravatar.com/avatar/1c0d59fd98fb89ba3a4f3ea950d31e1e'
```
- You could specify the size of the returned image (by default is 80px):
```
>>> gravtr.generate(size=2048)
'http://www.gravatar.com/avatar/1c0d59fd98fb89ba3a4f3ea950d31e1e?s=2048'
```

Enjoy! :)
