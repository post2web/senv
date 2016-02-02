shared environment
======

in development

to install:
pip ..

to use:

import SENV
SENV['foo'] = 'bar'

# in another process

import SENV
print SENV['foo']
