title: " web.py: error: No socket could be created "
tags:
- Code
- Bug Fix
---


This error message most often occurrs when trying to run web.py on an invalid address and port.  An example of an invalid address would be  example.net, instead of a proper ip address like 98.228.37.242.

## Other Causes:

Was just trying to get a simple web.py test running:

```
import web
 
urls = (
  '/x', 'X',
)
 
class X :
  def GET(self) :
    return 'x'
 
app = web.application(urls, globals())
app.run()
```
but I kept getting the error:

 error: No socket could be created 

The problem was that due to the way web.py loading works, you need to have the creation and running of the app only occur if this is the main entry point of the program.  Otherwise, the class loader in web.py will reload this file again later, and wind up spawning a new server when its intent was simply to load a class:

```
if __name__ == '__main__' :
  app = web.application(urls, globals())
  app.run()
```


