title: " List of bound variables in Python (excluding variables from modules) "
tags:
- Code
---


I've heard multiple people ask for a way to see a list of locally bound variables in python.  It would be especially useful for use in the interactive prompt.  They like the interface that matlab gave them and this is one of the features they miss the most.  I'm not sure what the best way to accomplish this is, but I've coded together one solution.  Here is an example use case:

```
 
from boundvars import boundvars
def test() :
         a = 1
         b = 2
         assert boundvars(vars()) == {'a': 1, 'b': 2}
         import urllib
         assert boundvars(vars()) == {'a': 1, 'b': 2}
 
x = 1
y = 2
boundvars(vars())
= {'y': 2, 'x': 1, 'test': <function test at 0x0000>}
from urllib import *
boundvars(vars())
= {'x': 1, 'y': 2, 'test' : <function test at 0x0000>}
 
test()
 ```
As you can see, boundvars is called with vars() as a parameter which then returns a dictionary of locally bound variables.  If boundvars.ignore_external_functions is set to False, the first two calls which show x and y bound would also show the variable boundvars.  If it is set to True, then all values which are functions not defined in the __main__  module are excluded from the output dictionary.  The latest code can be downloaded below.  Installation is as simple as:

$ wget http://dwiel.net/wp-content/uploads/2008/10/boundvars.tar.gz
$ tar -xvf boundvars.tar.gz
$ cd boundvars
$ sudo python setup.py install

Its not big enough to warrant a project at a code hosting service so its just provided here.  If you know of any way that this module could be improved (or avoided by some cool function I don't know about) please, let me know!

[boundvars.tar.gz](http://dwiel.net/wp-content/uploads/2008/10/boundvars.tar.gz) (version 0.1)


