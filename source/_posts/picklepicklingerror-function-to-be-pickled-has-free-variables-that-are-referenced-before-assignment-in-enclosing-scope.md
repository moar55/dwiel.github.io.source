title: " pickle.PicklingError: Function to be pickled has free variables that are referenced before assignment in enclosing scope "
tags:
- Uncategorized
---


The code I had that caused this problem looked like this:

```
if x :
    y = x

def foo() :
    print y

cloud.pickle(foo)
```
If this were a normal call to foo, the error instead would be:

```
UnboundLocalError: local variable 'y' referenced before assignment
```
The fix is to make sure that all variables used in foo have values at the time that it is pickled:

```
if x :
    y = x
else :
    y = None

def foo() :
    print y

cloud.pickle(foo)
```
Even this would be ok:

```
def foo() :
    print y

if x :
    y = x
else :
    y = None

cloud.pickle(foo)
```


