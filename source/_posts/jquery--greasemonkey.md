title: " JQuery + Greasemonkey "
date: 2013-01-01
tags:
- Code
- How to
- Linux
---


Had to look around to figure out how to include jquery in greasemonkey.  Should have just guessed this first; Just use the @require, and your standard jquery document ready code.  Heres my template anyway.

```
 
// ==UserScript==
// @name           JQuery Template
// @author         Zach Dwiel
// @description    Provide a basic template for using jquery in greasemonkey
// @include        *://*
// @require        http://code.jquery.com/jquery-latest.js
// ==/UserScript==
 
$(document).ready( function() {
    // your jquery code here
}
 
```


