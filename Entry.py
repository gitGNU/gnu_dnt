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
    def __init__(self, c = []) :
	debug("Node " + str(self) + " created successfully !!!!")
	self.__children = c
	self.__index    = 0

    def __repr__(self) :
	return '<Node %#x>' %(id(self))

    # Iterator related methods
    def __iter__(self):
        #debug("Initializing iterator for node " + str(self))
	return self
    def next(self):
	#debug("Calling next on node " + str(self))
	if (self.__index == len(self.__children)) :
            #debug("No more 'next'")
	    raise StopIteration
	tmp = self.__children[self.__index]
	self.__index = self.__index + 1
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
	debug("Node "     + str(self)                 +
	      " has now " + str(len(self.__children)) +
	      " children")
        debug(str(self) + ": " + str(self.__children))

class Entry(Node) :
    def __init__(self,
		 title    = "",
		 note     = "",
		 priority = "",
		 time     = datetime.date.today()) :
	Node.__init__(self)
	self.__title    = title
	self.__note     = note
	self.__priority = priority
	self.__time     = time
	debug("Entry " + str(self) + " created successfully !!!!")

    def __repr__(self) :
	return '<Entry %#x>' %(id(self))

    def title(self) :
	return self.__title
    def title(self, p) :
	# Remove leading and trailing whitespaces
	#        assert(p != None)
	#	self.title_ = re.match(r'^[ \t]*(.*)[ \t]*$', p).group(1)
	self.__title = p

    def note(self) :
	return self.__note
    def note(self, p) :
	# Remove leading and trailing whitespaces
	#        assert(p != None)
	#	self.title_ = re.match(r'^[ \t]*(.*)[ \t]*$', p).group(1)
	self.__note = p

    def priority(self) :
	return self.__priority
    def priority(self, p) :
	self.__priority = p

    def time(self) :
	return self.__time
    def time(self, p) :
	self.__time = p

    def dump(self, indent) :
	debug(indent + self.__title)
#	debug(indent + self.__note)
#	debug(indent + self.__priority)
#	debug(indent + self.__time)

	k = indent + indent
	for j in self :
	    j.dump(k)

if (__name__ == '__main__') :
    e1 = Entry("e1")
    e2 = Entry("e2")
    e3 = Entry("e3")
    e4 = Entry("e4")

    e1.dump(" ")
    e2.dump(" ")
    e3.dump(" ")
    e4.dump(" ")

    e1.child(0, e2)
    e2.child(0, e3)
    e3.child(0, e4)

    e1.dump(" ")

#    e1.child(0, None)
#    e2.child(0, None)
#    e3.child(0, None)
