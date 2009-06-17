#
# Copyright (C) 2008, 2009 Francesco Salvestrini
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

from   Debug      import *
from   Trace      import *
import Exceptions
import ID
import Enum

class Node(object) :
    def __init__(self) :
        self.__children  = []
#        self.__iterator  = 0
        self.__parent    = None
        self.__allflags  = Enum.Enum('visible', 'collapsed')
        self.__flags     = []
        self.__depth     = 0

        debug("Node `" + str(self) + "' created successfully")

    def parent_get(self) :
        return self.__parent
    def parent_set(self, node) :
        self.__parent = node

    parent = property(parent_get, parent_set)

    def depth_get(self) :
        return self.__depth

    depth = property(depth_get, None)

    def children(self) :
        return self.__children

#    # Add/Remove a node based on id
#    def child(self, i = 0, node = None) :
#       assert(i >= 0)
##        if (i == 0) :
##            raise Exceptions.Tree("cannot add/remove root")
#       if (node == None) :
#           debug("Removing child "
#                 "`" + str(i) + "' "
#                 "from node "
#                 "`" + str(self) + "'")
#           self.__children.remove(i)
#           node.__index = -1
#       else :
#           debug("Adding child "
#                 "`" + str(i) + "' "
#                 "to node "
#                 "`" + str(self) + "'")
#           self.__children.insert(i, node)
#           node.__index = i
#       node.parent = self

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
        self.__children.append(node)
        node.__parent = self
        node.__depth  = self.__depth + 1
        debug("Node `" + str(node) + "' added to node `" + str(self) + "'")

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
        self.__children.remove(node)
        node.__parent = None
        node.__depth  = 0
        debug("Node `" + str(node) + "' removed to node `" + str(self) + "'")

    # Iterator related methods
    def __iter__(self):
        return self

#    def next(self):
#        i = self.__iterator
#        if (i >= len(self.__children)) :
#            raise StopIteration
#        tmp = self.__children[self.__iterator]
#        self.__iterator = i + 1
#        return tmp

    def dump(self, prefix) :
        debug(prefix + "Dumping node `" + str(self) + "'")
        for i in self.__children :
            i.dump(prefix + " ")

    def id_get(self) :
        debug("Building node id")

        n = self
        s = ""

        while (n.__parent != None) :
            try :
                k = str(n.__parent.__children.index(n) + 1)
            except :
                break
            s = "." + k + s
            n = n.__parent

        s  = "0" + s

        i = ID.ID(s)
        debug("Node id is `" + str(i) + "'")
        return i

    id = property(id_get, None)

    def flags_get(self) :
        return self.__flags

    def flags_set(self, flags) :
        assert(type(flags) == list)

        for f in flags :
            try:
                self.__allflags(f)
            except:
                raise Exceptions.UnknownEnum(str(f))
        self.__flags = flags

    flags = property(flags_get, flags_set)

# Test
if (__name__ == '__main__') :
    root = Node()
    e1   = Node()
    e11  = Node()
    e12  = Node()
    e121 = Node()
    e13  = Node()
    e2   = Node()
    e21  = Node()

    root.add(e1)
    e1.add(e11)
    e1.add(e12)
    e12.add(e121)
    e1.add(e13)
    root.add(e2)
    e2.add(e21)

    print(str(root.id))
    assert(root.id == ID.ID("0"))
    assert(root.depth == 0)

    print(str(e1.id))
    assert(e1.id   == ID.ID("0.1"))
    assert(e1.depth == 1)

    print(str(e11.id))
    assert(e11.id  == ID.ID("0.1.1"))
    assert(e11.depth == 2)

    print(str(e12.id))
    assert(e12.id  == ID.ID("0.1.2"))
    assert(e12.depth == 2)

    print(str(e121.id))
    assert(e121.id == ID.ID("0.1.2.1"))
    assert(e121.depth == 3)

    print(str(e13.id))
    assert(e13.id  == ID.ID("0.1.3"))
    assert(e13.depth == 2)

    print(str(e2.id))
    assert(e2.id   == ID.ID("0.2"))
    assert(e2.depth == 1)

    print(str(e21.id))
    assert(e21.id  == ID.ID("0.2.1"))
    assert(e21.depth == 2)

    assert(e21.id  == ID.ID("0.2.1"))
    assert(e2.id   == ID.ID("0.2"))
    assert(e13.id  == ID.ID("0.1.3"))
    assert(e121.id == ID.ID("0.1.2.1"))
    assert(e12.id  == ID.ID("0.1.2"))
    assert(e11.id  == ID.ID("0.1.1"))
    assert(e1.id   == ID.ID("0.1"))
    assert(root.id == ID.ID("0"))

    # XXX FIXME:
    #     We should add some regression tests for depth related issues when
    #     adding/removing nodes ...

    root.flag = True
    assert(root.flag == True)
    root.flag = False
    assert(root.flag == False)

    root.flags = [ 'visible', 'collapsed' ]
    assert(root.flags == [ 'visible', 'collapsed' ])
    assert(root.flags != [ ])

    root.flags = [ 'visible' ]
    assert(root.flags == [ 'visible' ])
    assert(root.flags != [ ])

    root.flags = [ 'collapsed' ]
    assert(root.flags != [ ])

    debug("Test completed")
    sys.exit(0)
