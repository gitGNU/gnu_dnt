#
# Copyright (C) 2008 Francesco Salvestrini
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

import datetime
from   Trace import *

class Node :
    def __init__(self, id) :
        self.__id       = id
	self.__children = []
	self.__index    = 0
	debug("Node " + str(self) + " created successfully")

    def __repr__(self) :
	return '<Node %#x, id=`%s\'>' %(id(self), self.__id)

    # Iterator related methods
    def __iter__(self):
	#debug("Initializing iterator for node " + str(self))
	return self

    def next(self):
	i = self.__index
	debug("  Calling next on node " + str(self) +
	      ", index = "              + str(i) +
	      ", len = "                + str(len(self.__children)))
	if (i >= len(self.__children)) :
	    debug("  No more 'next' on node " + str(self))
	    raise StopIteration
	tmp = self.__children[self.__index]
	self.__index = i + 1
	return tmp

    def children(self) :
	return self.__children

    def child(self, i, node) :
	assert(i >= 0)
	if (node == None) :
	    debug("Removing node "  + str(node) +
		  " from position " + str(i)    +
		  " of node "       + str(self))
	    self.__children.remove(i)
	else :
	    debug("Inserting node " + str(node) +
		  " in position "   + str(i)    +
		  " of node "       + str(self))
	    self.__children.insert(i, node)
	debug(str(self) + ": " + str(self.__children))

    def dump(self) :
	debug("Dumping " + str(self))
	for j in self.__children :
	    j.dump()

class Entry(Node) :
    def __init__(self,
		 title    = "",
		 note     = "",
		 priority = "",
		 time     = datetime.date.today()) :
	Node.__init__(self, title)
	self.__title    = title
	self.__note     = note
	self.__priority = priority
	self.__time     = time
	debug("Entry " + str(self) + " created successfully !!!!")

    def __repr__(self) :
	return '<Entry %#x>' %(id(self))

    def title(self) :
	return self.__title
    def title(self, title) :
	# Remove leading and trailing whitespaces
	#        assert(p != None)
	#	self.title_ = re.match(r'^[ \t]*(.*)[ \t]*$', p).group(1)
	self.__title = title

    def note(self) :
	return self.__note
    def note(self, note) :
	# Remove leading and trailing whitespaces
	#        assert(p != None)
	#	self.title_ = re.match(r'^[ \t]*(.*)[ \t]*$', p).group(1)
	self.__note = note

    def priority(self) :
	return self.__priority
    def priority(self, priority) :
	self.__priority = priority

    def time(self) :
	return self.__time
    def time(self, time) :
	self.__time = time

    def dump(self) :
	debug("Dumping " + str(self) + ": " + self.__title)
	for j in self.children() :
	    j.dump()

if (__name__ == '__main__') :
    root = Node("root")
    e1   = Node("e1")
    e11  = Node("e11")
    e12  = Node("e12")
    e2   = Node("e2")

    e1.child(0, e12)
    e1.child(0, e11)
    root.child(0, e1)
    root.child(1, e2)

    root.dump()
#
#    dump("!!!!!!! AAAA")
#
#    root = Node("root", [ Node("e1",
#                               [ Node("e11"), Node("e12") ]),
#                          Node("e2") ])
#    root.dump()
    pass
