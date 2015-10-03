title: " Build tolua++ files with makefile "
tags:
- Code
- How to
- Linux
---


Here is how you can have your makefile build your tolua++ .cpp and .h files for you.  It should work for plain tolua also.

```
TOLUA = tolua++5.1
 
tolua_%.cpp tolua_%.h : %.pkg
	$(TOLUA) -o $(@:%.h=%.cpp) -H $(@:%.cpp=%.h) $<
```
this will generate tolua_file.cpp and tolua_file.h files from corresponding file.pkg files anytime they the .cpp or .h file is depended on somewhere else in the file.  In my case I just added tolua_file.o to my list of objects.  Here is the full makefile for the project which required this - for reference:

```
 
 
# LINUX
LIBLUA=lua5.1
# MAC OSX
#LIBLUA=lua
 
# LDFLAGS=-arch x86_64
OBJS = swarm.o group.o scene.o vmath.o tolua_group.o tolua_swarm.o tolua_vmath.o
CXX = g++
CXXFLAGS = -Wall -c -O2 `sdl-config --cflags`
LDFLAGS = -Wall `sdl-config --libs`
INCLUDES = -I./include -I/usr/include/lua5.1 -I/opt/local/include
LIBS = -L./lib -lANN -lGL -lGLU -llo -ltolua++5.1 -l$(LIBLUA)
TOLUA = tolua++5.1
 
tolua_%.cpp tolua_%.h : %.pkg
	$(TOLUA) -o $(@:%.h=%.cpp) -H $(@:%.cpp=%.h) $<
 
%.o: %.cpp
	$(CXX) $(INCLUDES) $(CXXFLAGS) -c $< -o $@
 
# the executable
swarm: $(OBJS)
	$(CXX) $(LDFLAGS) -o $@ $^ $(LIBS)
 
 
```
[download](http://github.com/dwiel/swarm/raw/8716451c8b9844bbf9ec8e7f9649aca0b622c752/makefile)


