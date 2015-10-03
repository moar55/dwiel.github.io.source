title: " service error when starting mongodb "
tags:
- FYI
- Linux
---


I was trying to start mongodb just now and couldn't understand why it wasn't working.  Turns out I needed to be sudo - not the most clear error message ...

```
 
$ service mongodb start
start: Rejected send message, 1 matched rules; type="method_call", sender=":1.11
212" (uid=1000 pid=1360 comm="start) interface="com.ubuntu.Upstart0_6.Job" membe
r="Start" error name="(unset)" requested_reply=0 destination="com.ubuntu.Upstart
" (uid=0 pid=1 comm="/sbin/init"))
$ sudo service mongodb start
mongodb start/running, process 1326
 

```


