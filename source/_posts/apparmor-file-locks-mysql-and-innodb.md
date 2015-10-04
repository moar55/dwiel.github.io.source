title: " Apparmor, file locks, MySQL and Innodb "
date: 2013-01-01
tags:
- Bug Fix
- Linux
---


In my syslogs I was getting this:
Oct 10 23:48:51 dwiel-srv kernel: [  141.664049] type=1503 audit(1349927331.203:107):  operation="file_lock" pid=2192 parent=1 profile="/usr/sbin/mysqld" requested_mask="k::" denied_mask="k::" fsuid=113 ouid=113 name="/home/mysql/ibdata1"

It turns out that the problem was that the problem was because in /etc/apparmor.d/usr.sbin.mysqld I had the lines:
/home/mysql/ rw,
  /home/mysql/** rw,

instead of the lines:
/home/mysql/ rw,
  /home/mysql/** rwk,

Note the k at the end of the second line which enables mysqld to make file locks


