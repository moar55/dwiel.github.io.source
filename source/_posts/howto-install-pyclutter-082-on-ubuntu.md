title: " Howto install pyclutter 0.8.2 on Ubuntu "
tags:
- Linux
---


Ubuntu 8.04 has pyclutter 0.6.2 in the repositories while the current stable version is 0.8.2.  Here is how I installed pyclutter 0.8.2 with all of the extra available libraries (gtk, gst, cairo):

download:

- [pyclutter-0.8.2](http://www.clutter-project.org/sources/pyclutter/0.8/pyclutter-0.8.2.tar.bz2)
- [clutter-0.8.4](http://www.clutter-project.org/sources/clutter/0.8/clutter-0.8.4.tar.bz2)
- [clutter-gst-0.8.0](http://www.clutter-project.org/sources/clutter-gst/0.8/clutter-gst-0.8.0.tar.bz2)
- [clutter-cairo-0.8.2](http://www.clutter-project.org/sources/clutter-cairo/0.8/clutter-cairo-0.8.2.tar.bz2)
- [clutter-gtk-0.8.2](http://www.clutter-project.org/sources/clutter-gtk/0.8/clutter-gtk-0.8.2.tar.bz2)

also make sure you have *python-cairo-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev* installed.  There may be more required, but these were the only ones I didn't already have installed.

For some reason I had to configure all of these libraries with --prefix /usr to get pycluster to see all of them.

Also, configure pycluster with --enable-docs if you want any documentation.

have fun!


