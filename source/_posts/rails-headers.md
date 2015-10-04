title: " Rails Headers "
date: 2013-01-01
tags:
- Code
---


You can access header values from rails from the request.env hash.  request.env contains a lot of other non HTTP header values.  The header name is a bit transformed too:

- prepended with HTTP_
- converted to uppercase
- dashes converted to undersocres
- ... more?

Example:

```
 
curl -H 'x-custom-value: foo' http://example.com/
 
```
can be accessed in rails with:

```
 
request.env['HTTP_X_CUSTOM_VALUE']
 
```


