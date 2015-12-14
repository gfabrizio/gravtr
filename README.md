[![Code Health](https://landscape.io/github/gfabricio/gravtr/master/landscape.svg?style=flat)](https://landscape.io/github/gfabricio/gravtr/master) | [![Build Status](https://travis-ci.org/gfabricio/gravtr.svg)](https://travis-ci.org/gfabricio/gravtr)
# Gravtr
A simple package to generate a gravatar url

## Installation:
```
$ pip install gravtr
```
## Usage:
```
>>> from gravtr import Gravtr
>>> gravtr = Gravtr("gfabricio@tests.com")
>>> gravtr.generate()
'http://www.gravatar.com/avatar/1c0d59fd98fb89ba3a4f3ea950d31e1e'
```
Enjoy! :)
