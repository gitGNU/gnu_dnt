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

import sys

import Debug
from   Trace import *
import Exceptions

class Node(object) :
    def __init__(self) :
	self.__children = []
	self.__index    = 0
        self.__parent   = None

    def parent_get(self) :
	return self.__parent
    def parent_set(self, node) :
	self.__parent = node

    parent = property(parent_get, parent_set)

    def children(self) :
	return self.__children

    # Add/Remove a node based on id
    def child(self, i = 0, node = None) :
#	assert(i >= 0)
#        if (i == 0) :
#            raise Exceptions.Tree("cannot add/remove root")
	if (node == None) :
            debug("Removing child "
                  "`" + str(i) + "' "
                  "from node "
                  "`" + str(self) + "'")
	    self.__children.remove(i)
	else :
            debug("Adding child "
                  "`" + str(i) + "' "
                  "to node "
                  "`" + str(self) + "'")
	    self.__children.insert(i, node)
        node.parent = self

    # Add a child node based on object
    def add(self, node) :
        assert(node != None)
        i     = 0
        found = False
        for j in self.__children :
            if (j == node) :
                found = True
                break
            i = i + 1
        assert(found == False)
        self.child(i, node)

    # Remove a child node based on object
    def remove(self, node) :
        assert(node != None)
        i     = 0
        found = False
        for j in self.__children :
            if (j == node) :
                found = True
                break
            i = i + 1
        assert(found == True)
        self.child(i, None)

    # Iterator related methods
    def __iter__(self):
	return self

    def next(self):
	i = self.__index
	if (i >= len(self.__children)) :
	    raise StopIteration
	tmp = self.__children[self.__index]
	self.__index = i + 1
	return tmp

    def dump(self, prefix) :
        debug(prefix + "Dumping node `" + str(self) + "'")
        for i in self.__children :
            i.dump(prefix + " ")

# Test
if (__name__ == '__main__') :
    root = Node()
    e1   = Node()
    e11  = Node()
    e12  = Node()
    e2   = Node()

    e1.child(0, e12)
    e1.child(0, e11)
    root.child(0, e1)
    root.child(1, e2)

    debug("Test completed")
    sys.exit(0)
