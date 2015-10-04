title: " MySQLdb: TypeError: %d format: a number is required, not str "
date: 2013-01-01
tags:
- Code
---


I was getting this error message from MySQLdb:

TypeError: %d format: a number is required, not str

The error message was the result of this code:

```
  assert type(gateway_id) == int
  sql = """
    SELECT meter_id 
    FROM mtus 
    WHERE gateway_id = %d 
      AND name = '%s' """
  conn = mysql_connect()
  cursor = conn.cursor()
  cursor.execute(sql, (gateway_id, name))
  ret = cursor.fetchone()
  cursor.close()
```
It turns out, execute converts all the arguments to SQL literal values. [reference](http://mysql-python.sourceforge.net/MySQLdb.html#some-examples) All %Xs should be %s and there shouldn't be any quotes around them. MySQLdb takes care of the string escaping too.

## Other Causes:

For those of you arriving here from a search and are not having problems with MySQL, the reason for this error is that a string was passed into a format where a number was expected:

```
# throws the TypeError:
message = "%d seconds until done" % "three"
# works:
message = "%d seconds until done" % 3
```


