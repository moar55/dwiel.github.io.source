title: " python onexit "
tags:
- Code
- How to
---


Was looking for python's equivalent to onexit and found [atexit](http://docs.python.org/2/library/atexit.html):

```
import atexit
atexit.register(function_that_will_be_called_before_this_program_exits)
```


