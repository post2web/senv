shared environment
======

In development, do not use.

To install:
pip install git+git://github.com/post2web/senv@master

To use:

from senv.sdict import Sdict
# create shared dict
a = Sdict()
# use it just as you normally use dic
a['foo'] = 'bar'

# in another process
from senv.sdict import Sdict
a = Sdict()
print a
{'foo': 'bar'}
del a['foo']

# in the previous process
print a
{}
