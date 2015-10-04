title: " Clustering items by tag "
date: 2013-01-01
tags:
- Data Exploration
---


I write notes in axpress, my still private web front end to a triple store.  The notes have a body and a set of tags.  Most notes are thoughts about problems I encounter while programming, explanations of design decisions.  They have come in handy as a reference a few times, but the information in them is often hard to find, even with tags.  I also find writing tags tedious.  I've decided to look through the various set of tagged items, my notes and my bookmarks to start, to see what kind of patterns I can find.

I used [graphviz](http://www.graphviz.org/ "graphviz") to get a quick visualization of the relationships between each tag.  Each tag is a node.  Each node is labeled by the tag name and the number of notes it appears in.  The closer two nodes, the more often they occurred in the same notes.  Only tags which were connected to more than 1 other tag were included in the visualization to reduce the complexity.

From here, some basic patterns can be seen.some basic subgraphs can be seen.  "trade", "local" and "books" all stem from "economy" only.  "economy" is probably a good tag to classify that group of notes where "trade", "local" and "books" are sub tags.  A similar pattern can be seen coming from the express tag (which is the old name of this project).  Coming from it are some tags which I don't seem to note any more.

Only visualizing pairs of tags which occurred more than 3 times, show which (common) tags are used with which other (common) tags, but not how often.  It is interesting to see which tags are independent of others.  "axpress" and "express" do not occur together often.  It might be possible to use this type of graph to find a set of tags which partition the entire set of notes efficiently.  This, hopefully small, set of tags could be used as a starting point for drilling down to find a note you are looking for.

For this next graph I wanted to see how 'thick' the connections between each node was.  That is, from "axpress" how many links are there to "case"?  How many to "design"?  Are there any tags which occur with nearly every instance of "axpress" or are they uniformly distributed?  The darker a node is, the more occurences of that tag there are (color corresponds linearly to number in the label).  The color on the end of each link correspond to the relative number of connections represented by that link.  For example coming from "code" is a dark green node to "axpress" and a lighter cyan to "case".  This is because there are twice as many connections from "code" to "axpress" as to "case".  From most tags, it seems that there is a relatively uniform number of connections to each other tag.

This set is rather limited, so I am considering a few different next steps.  I could use the text of the note in a similar kind of analysis - increasing the number of tags, leaving the number of tagged items alone.  Or I could use data from delicious (either my own, or a small set of users) to increase the number of tagged items while leacing the number of tags relatively small.  What would you like to see done next?  Something else entirely?


