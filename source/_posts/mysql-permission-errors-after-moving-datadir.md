title: " MySQL Permission Errors After Moving Datadir "
tags:
- Code
- FYI
- How to
- Linux
---


I wanted to make space on my root partition and so moved my mysql data dir to /home/mysql in /etc/mysql/my.conf and received the following errors:

dwiel@dwiel:~$ sudo mysqld
091111 20:39:16 [Warning] Can't create test file /home/mysql/dwiel.lower-test
091111 20:39:16 [Warning] Can't create test file /home/mysql/dwiel.lower-test
091111 20:39:16 [Note] Plugin 'FEDERATED' is disabled.
mysqld: Can't find file: './mysql/plugin.frm' (errno: 13)
091111 20:39:16 [ERROR] Can't open the mysql.plugin table. Please run mysql_upgrade to create it.
091111 20:39:16  InnoDB: Operating system error number 13 in a file operation.
InnoDB: The error means mysqld does not have the access rights to
InnoDB: the directory.
InnoDB: File name ./ibdata1
InnoDB: File operation call: 'open'.
InnoDB: Cannot continue operation.

The problem was with apparmor.  It was restricting mysql from reading and writing to /home/mysql.  To correct this I edited the file /etc/apparmor.d/usr.sbin.mysqld and added:

/home/mysql r,
/home/mysql** rwk,

to the end of the file.  Then restarted apparmor:

sudo /etc/init.d/apparmor restart

and then restarted apache with no problem


