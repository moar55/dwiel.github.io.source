title: " PiCloud Simulation: OSError: [errno 13] permission denied "
date: 2013-01-01
tags:
- Bug Fix
- Linux
---


I tried running a PiCloud simulation on Ubuntu 10.04 on linode and got the following error:

OSError: [errno 13] permission denied

I found the solution [here](http://stackoverflow.com/questions/2009278/python-multiprocessing-permission-denied/2009505#2009505):

add the following line to your fstab and reboot:

none /dev/shm tmpfs rw,nosuid,nodev,noexec 0 0

If you don't want to reboot, a temporary fix might be:

sudo chgrp $GROUP /dev/shm
sudo chmod g+w /dev/shm

That last part might not be the best way to do it, but it worked for me.


