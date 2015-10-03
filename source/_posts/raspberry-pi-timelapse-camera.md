title: " Raspberry Pi Timelapse Camera "
tags:
- Code
---


Some steps I took to build my Raspberry Pi Timelapse camera:

Power

The location of the timelapse camera puts it about 400 feet from the nearest building with electricity, so I figured it might make sense to put it on solar power and a battery, but it turns out to be prohibitively expensive.  Even by piecing together a system myself from panels on ebay, car batteries, a home made controller, etc, it was still going to wind up costing at least $400.  400 feet of 12/2 cable is only around $120.  Also, in a year or two, the electricity run will be shortened by a new power service installed near by.  So for power, I am just going to run some cable from the house.  There will be some voltage drop, but that shouldn't be a problem, it won't be much.

Enclosure

I spent a long time trying to figure out what kind of enclosure I should build or use to hold everything.  I wanted something that I could open and close relatively easily (in case I needed to repair it).  Turns out the easiest thing to use was a 8" x 8" x 4" junction box I found in the electrical section of a hardware store.  It is much bigger than I needed, but it was the smallest I could find that would fit the raspberry pi with a cable sticking out both the USB port and the power port, which comes out to about 8".

Camera

The camera I am using is a Nikon S3000.  I made sure that it was in the [list of cameras supported by gphoto2](http://gphoto.org/proj/libgphoto2/support.php).  Unfortunately, I wasn't able to use the build of gphoto2 that is in the debian package manager because it is too old, so I downloaded and built the latest versions of libgphoto2 and gphoto2 from source.

Code

I wrote a basic python script which will take pictures every 5 minutes.  But then, for some reason on the raspberrypi, I've been having trouble controlling the camera.  Every few commands I send to the camera, the usb connection fails.  I have to issue a usbreset to get it back working, so I added some code to do that automatically before running every command.  Also added some code to only take pictures during the day (in Bloomington, Indiana) which uses a nifty library which will give sunrise and sunset times for any day given a latitude and longitude.

All code is open source and available [here](https://github.com/dwiel/gphoto2-timelapse).

Mounting:

I've mounted the camera to a small piece of scrap plywood and the plywood to a tree, with the camera facing both of the building sites that we are working on this year

What is the one feature you see as missing?


