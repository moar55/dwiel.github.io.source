title: " python-memcache is thread safe "
tags:
- FYI
---


python-memcache is a thread safe library.  In memcache.py, which is the single source file, you'll find:

```
 
try:
    # Only exists in Python 2.4+
    from threading import local
except ImportError:
    # TODO:  add the pure-python local implementation
    class local(object):
        pass
class Client(local):
  ...
 
```
Which means that all data accessed through self.variable_name have values which are thread specific (as long as you are running python version 2.4 or higher.)  Very cool.  Before I looked at the code, I wrote some multi-threaded tests to check and see if anything fishy would happen.  I'd say looking at the code is a better solution.

more details [threading.local](http://docs.python.org/library/threading.html#threading.local)


