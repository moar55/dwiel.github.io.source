title: " TP-Link TL-WN722N on Ubuntu 10.04 "
date: 2013-01-01
tags:
- How to
- Linux
---


Note: according [this guy](http://ricardolopes.net/blog/tutorial-my-perfect-linux-setup-with-fedora-15-lovelock/ "this guy") this set of steps also works for Fedora 15.

I had a lot of trouble getting this card to work.  Here is how I finally got it.

I am running 2.6.32-30-generic-pae #59-Ubuntu SMP
running "lsusb" shows the following line for my device: 0cf3:9271 Atheros Communications, Inc.

I tried a bunch of different compat-wireless versions and [this one](http://linuxwireless.org/download/compat-wireless-2.6/compat-wireless-2.6.tar.bz2) finally did it.  At the time, it was the latest stable release.  The daily snapshots were causing kernel panics ... Download it, decompress it and build it:

$ tar xvf compat-wireless-2.6.38.2-2.tar.bz2
$ cd compat-wireless-2.6.38.2-2
$ ./scripts/driver-select ath9k_htc
$ sudo make
$ sudo make install

I had to download version 1.2 of htc_9271.fw the firmware from [here](http://wireless.kernel.org/download/htc_fw/) and copied the file to /lib/firmware.

I was getting wlan%d instead of something reasonable like wlan0. Running sudo ifconfig wlan%d showed me the mac address which I could use to add an entry to /etc/udev/rules.d/70-persistent-net.rules.  Heres the entry I added: (note that the browser adds newlines here, but you should add just two lines: one for the comment, and one for the rule)

# USB device 0x0cf3:0x9271 (usb)
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="54:e6:fc:94:91:35", ATTR{dev_id}=="0x0", ATTR{type}=="1", KERNEL=="wlan*", NAME="wlan2"

reload the drivers by running:

sudo modprobe ath9k_htc

Now plug in the device.  There were a lot of other steps that I followed while trying to get this to work, so I may have left something out.


