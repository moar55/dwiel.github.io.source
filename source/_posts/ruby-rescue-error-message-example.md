title: " ruby rescue error message example "
date: 2013-01-01
tags:
- Code
---


```
begin
  raise "this is an error message"
rescue Exception => e
  # prints "this is an error message"
  puts e.message
  # or if you want the entire error message with stack trace and all:
  puts "failed sending weekly power usage to house: #{$!}"
end
```


