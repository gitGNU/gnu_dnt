# -*- python -*-

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
import string

from   Debug  import *
from   Trace  import *
import Node
import Time

class Root(Node.Node) :
    def __init__(self, t = "") :
        super(Root, self).__init__()
        self.__text_set(t)
        debug("Root `" + str(self) + "' created successfully")

    def __text_get(self) :
        return self.__text
    def __text_set(self, t) :
        # Use basestring to perform the test, we could have to deal with
        # unicode characters coming as user-input
        assert(isinstance(t, basestring))
        assert(t != "")

        # Remove leading and trailing whitespaces from input string
        self.__text = string.strip(t)

    text = property(__text_get, __text_set, None, None)

    def __str__(self) :
        return '<Root #%x>' % (id(self))

    def accept(self, visitor) :
        assert(visitor != None)
        debug("Root " + str(self) + " accepted visitor " + str(visitor))
        visitor.visit(self)

    def find(self, node, id) :
        assert(node != None)
        assert(id != None)

        debug("Looking for id `" + str(id) + "' into node `" + str(node) +"'")
        l = id.tolist()
        assert(len(l) > 0)

        tmp = node
        for i in l :
            if (i == 0) :
                continue

            assert(i >= 1)
            try :
                debug("Looking for child "
                      "`" + str(i) + "' "
                      "in node "
                      "`" + str(tmp) + "'")
                tmp = tmp.children[i - 1]
            except IndexError :
                debug("Child `" + str(i) + "' "
                      "is missing in node "
                      "`" + str(tmp) +"'")
                return None
            except :
                bug("Unhandled exception while looking for " +
                    "node in Root.find()")

            if (tmp == None) :
                return tmp

        return tmp

# Test
if (__name__ == '__main__') :
    root = Root("root")

    debug("Test completed")
    sys.exit(0)
