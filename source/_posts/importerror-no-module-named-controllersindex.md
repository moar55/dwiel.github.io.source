title: " ImportError: No module named controllers.index "
date: 2013-01-01
tags:
- Bug Fix
---


Fix: create empty file: appname/appname/controllers/__init__.py

Anytime I tried to load a page in my pylons app, I received the error message: ImportError: No module named controllers.index I had just deleted all of the .pyc files because I was getting wrong magic number errors, and somehow this problem resulted.


