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
import Entry
import Root

class Visitor(object) :
    def __init__(self, level_current = 0, index = 0, level_previous = 0) :
        self.__level_current  = level_current
        self.__level_previous = level_previous
        self.__index          = index
        debug("Visitor initialized")

    # The following method must be provided by the derived class
    def visitEntry(self, node) :
        bug("No visitEntry() method provided by the derived class " +
            "(while visiting " + str(node) + ")")

    # The following method must be provided by the derived class
    def visitRoot(self, node) :
        bug("No visitRoot() method provided by the derived class " +
            "(while visiting " + str(node) + ")")

    def level_previous(self) :
        return self.__level_previous

    def level_current(self) :
        return self.__level_current

    def index(self) :
        return self.__index

    def visit(self, n) :
        debug("Visiting " + str(n))

        if (isinstance(n, Root.Root)) :
            self.visitRoot(n)
        elif (isinstance(n, Entry.Entry)) :
            self.visitEntry(n)
        else :
            bug("Unknown type " + str(type(n)) + " for Visitor")

        assert(hasattr(n, "children"))

        old_level             = self.__level_current
        self.__level_previous = self.__level_current
        self.__level_current  = self.__level_current + 1
        index                = 0
        for j in n.children :
            index        = index + 1
            self.__index = index
            # Please, re-accept myself ;-)
            j.accept(self)
        self.__level_current = old_level

# Test
if (__name__ == '__main__') :
    class V(Visitor) :
        def __init__(self, data) :
            super(V, self).__init__()
            self.__data = data

        def visitRoot(self, e) :
            debug("Visiting Root " + str(e))
            self.__data.append(self.level_previous())
            self.__data.append(self.level_current())

        def visitEntry(self, e) :
            debug("Visiting Entry " + str(e))
            self.__data.append(self.level_previous())
            self.__data.append(self.level_current())

    debug("Running")
    root = Entry.Entry("root")
    e1   = Entry.Entry("e1")
    e11  = Entry.Entry("e11")
    e12  = Entry.Entry("e12")
    e2   = Entry.Entry("e2")

    debug("Building tree")
    root.add(e1)
    e1.add(e11)
    e1.add(e12)
    root.add(e2)

    debug(str(root))

    debug("Visiting")
    l = []
    v = V(l)
    debug(str(v))
    debug(type(v))

    debug("Accepting")
    root.accept(v)

    # [0, 0, 0, 1, 0, 2, 0, 2, 0, 1]
    t = [0, 0, 0, 1, 1, 2, 2, 2, 2, 1]

    debug(l)
    debug(t)

    if (t != l) :
        debug("failed")
        sys.exit(1)

    sys.exit(0)
    debug("Test completed")
