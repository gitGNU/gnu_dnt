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
import re

from   Debug      import *
from   Trace      import *
import Entry
import Exceptions

def help() :
    return "Recognized filters are: all, done, not-done"

class Filter(object) :
    def __init__(self, s = None) :
        if (s == None) :
            s = "all"
        self.__function = self._parse(s)
        assert(self.__function != None)

    def _parse(self, s) :
        assert(s != None)

        t = s
        debug("Filter is `" + str(s) + "'")

        # Replace ',' with 'and'
        t = t.replace(",", " and ")
        # Replace '&' with 'and'
        t = t.replace("&", " and ")
        # Replace '|' with 'or'
        t = t.replace("|", " or ")
        debug("Filter is now `" + str(t) + "'")

        # Remove useless spaces
        t = re.sub(r'\s+', ' ', t)

        # Then split using ' '
        t = t.split(" ")
        debug("Filter is now `" + str(t) + "'")

        tmp = None
        for i in t :
            debug("Handling filter `" + i + "'")
            if (i == "all") :
                tmp = lambda x: True
            elif (i == "done") :
                tmp = lambda x: x.done()
            elif (i == "not-done") :
                tmp = lambda x: not(x.done())
            elif (i == "and") :
                tmp = lambda x, y: x and y
            elif (i == "or") :
                tmp = lambda x, y: x or y
            else :
                raise Exceptions.UnknownFilter(s)
        assert(tmp != None)

        return tmp

    def function_get(self) :
        assert(self.__function != None)
        return self.__function

    function = property(function_get, None)

# Test
if (__name__ == '__main__') :
    v = Filter("all")
    assert(v != None)
    v = Filter("done")
    assert(v != None)
    v = Filter("not-done")
    assert(v != None)
    v = Filter("all,done,not-done")
    assert(v != None)
    v = Filter("all, done, not-done")
    assert(v != None)
    v = Filter("all ,done ,not-done")
    assert(v != None)
    v = Filter("all , done , not-done")
    assert(v != None)
    v = Filter("all  ,  done  ,  not-done")
    assert(v != None)
    v = Filter("all   ,   done   ,   not-done")
    assert(v != None)
    v = Filter("all    ,    done    ,    not-done")
    assert(v != None)

    debug("Test completed")
    sys.exit(0)
