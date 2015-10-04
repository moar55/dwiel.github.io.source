title: " Axpress "
date: 2013-01-01
tags:
---


Query languages of the past have been good at locating data in existing databases.  I wanted to see what it might look like to have a query language for not just local information but all available information and information yet to be generated.  Here is what it looks like right now:

*Examples*

```

    image[file.pattern] = "/home/dwiel/pictures/*.jpg"
    image[file.filename] = _filename
```
This query returns a list of filenames of jpg images in my pictures directory:

```

[
    {
        'filename' : '/home/dwiel/pictures/sunset.jpg'
    }, {
        'filename' : '/home/dwiel/pictures/funny.jpg'
    }
]
```
And another query:

```

    image[file.pattern] = "/home/dwiel/pictures/*.jpg"
    image[image.average_color] = _color
```
which this time just returns colors:

```

[
    {
        'color' : (244, 100, 133)
    }, {
        'color' : (24, 15, 12)
    }
]
```
If we want both the filename and the color, we can request both

```

    image[file.pattern] = "/home/dwiel/pictures/*.jpg"
    image[file.filename] = _filename
    image[image.average_color] = _color
```
```

[
    {
        'filename' : '/home/dwiel/pictures/sunset.jpg',
        'color' : (244, 100, 133)
    }, {
        'filename' : '/home/dwiel/pictures/funny.jpg'
        'color' : (24, 15, 12)
    }
]
```
If we want to query for images on flickr it looks very similar (sorry about the lack of square brackets around flickr ... wordpress tries to turn it into a flickr video) :

```

    image flickr = "sunset"
    image[image.average_color] = _color
```
Which atm, is (#2 is black and white):

```

[
  {
    'color' : [ 184, 139, 92, ],
  }, {
    'color' : 11,
  }, {
    'color' : [ 153, 117, 87, ],
  }, {
    'color' : [ 134, 138, 161, ],
  }, {
    'color' : [ 121, 119, 119, ],
  },
]
```
Again, if we want a filename for these we can add that like we did before and the pictures will be downloaded to a temporary file as a side-effect so that there will be a filename to provide.  Or we could just ask for a url.

For a more complex example, we'll query for all of the artists similar to the artist that the last.fm user dwiel has most recently listened to:

```

    user[lastfm.user_name] = 'dwiel'
    user[lastfm.recent_track] = track
    track[lastfm.artist] = artist
    artist[lastfm.similar_to] = similar_artist
    similar_artist[lastfm.artist_name] = _similar_name
```
or if you prefer, a more concise format:

```

    user[lastfm.user_name] = 'dwiel'
    user[lastfm.recent_track][lastfm.artist][lastfm.similar_to][lastfm.artist_name] = _similar_name
```
```

[
  {
    u'similar_name' : u'Scout Niblett',
  }, {
    u'similar_name' : u'Blonde Redhead',
  }, ... {
    u'similar_name' : u'The Fiery Furnaces',
  },
]
```
*Overall*

As I explored this query language, one of the most interesting aspects was the ability to easily query for information which would otherwise require lots of glue code in other languages.  If there is a translation from one data type to another, then you don't need to code that translation explicitly.  If you have an image URL or flickr tag, you can immediately start talking about it's average color.  This is very powerful, and I am still working out what kinds of new user interface designs that this may make possible.

One user interface design that I have been exploring would use this as an intermediate query language which some form of natural language could be compiled into.  I am excited to explore where this goes when mixed with ideas from one of my previous projects [english](http://dwiel.net/english) and some new ideas coming out of mozilla labs with [ubiquity](http://labs.mozilla.com/projects/ubiquity/).

Code is available [here](http://code.google.com/p/simplesparql/).  Though note that you must check out the latest svn as the version available under the download section is a very old version of the code.  Back when it was merely a MQL style query language for accessing SPARQL endpoints.  Although, if that is what you want, then the front page and the download files are applicable.

I have a simple web interface running locally, but I am not yet ready to let other people run arbitrary code on my machine (even in a sandbox).  Hopefully soon.


