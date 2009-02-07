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
import string

from   Debug      import *
from   Trace      import *
import Exceptions

class ID(object) :
    def __init__(self, s = "") :
        assert(s != None)
        assert(type(s) == str)

        if (s == "") :
            raise Exceptions.MalformedId("passed id is empty")

        x = []
        try :
            for n in string.split(s, ".") :
                x.append(int(n))
        except :
            raise Exceptions.MalformedId("id `" + s + "' is malformed")

        assert(len(x) > 0)

        self.__id = x

    def __str__(self) :
        s = ""
        for i in range(0, len(self.__id)) :
            if (i != 0) :
                s = s + "."
            s = s + str(self.__id[i])
        return s

    def tolist(self) :
        # Give the caller a copy of our internal data ...
        return list(self.__id)

    def parent(self) :
        # XXX FIXME: Should it be better to return None ?
        if (len(self.__id) <= 1) :
            raise Exceptions.Parentless(self.__str__())

        s = ""
        for i in range(0, len(self.__id) - 1) :
            if (i != 0) :
                s = s + "."
            s = s + str(self.__id[i])
        return ID(s)

# Test
if (__name__ == '__main__') :
    def proc_node(i) :
        assert(type(i) == str)
        node = ID(i)
        assert(i == str(node))
        debug(i + " node   = " + str(node))

    def proc_parent(i) :
        assert(type(i) == str)
        node = ID(i)
        assert(i == str(node))
        parent = node.parent()
        debug(i + " parent = " + str(parent))

    ok = False
    try :
        proc_parent("")
    except :
        ok = True
    if (not ok) :
        sys.exit(1)

    proc_node("0")
    proc_node("0.1")
    proc_node("0.1.2")
    proc_node("0.1.2.3")
    proc_node("1.2.3.4")
    proc_node("4.3.2")
    proc_node("7.2")

    ok = False
    try :
        proc_parent("0")
    except :
        ok = True
    if (not ok) :
        sys.exit(1)

    proc_parent("0.1")
    proc_parent("0.1.2")
    proc_parent("0.1.2.3")
    proc_parent("1.2.3.4")
    proc_parent("4.3.2")
    proc_parent("7.2")

    try :
        x = ID()
        sys.exit(1)
    except :
        pass

    debug("Test completed")
    sys.exit(0)
