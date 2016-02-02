shared environment
======

In development, do not use.

to install:
pip install git+git://github.com/post2web/senv@master

to use:

import SENV
SENV['foo'] = 'bar'

# in another process

import SENV
print SENV['foo']
