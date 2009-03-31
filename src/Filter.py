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

from   Debug      import *
from   Trace      import *
import Entry
import Exceptions

def help() :
    return "Recognized filters are: all, done, not-done"

class Filter(object) :
    def __init__(self, s = None) :
        filter = None
        if (s == None) :
            filter = lambda x: True
        else :
            tmp = None
            for i in s.split(",") :
                assert(tmp == None)
                debug("Handling filter `" + i + "'")
                # Filter is != None
                if (i == "all") :
                    tmp = lambda x: True
                elif (i == "done") :
                    tmp = lambda x: x.done()
                elif (i == "not-done") :
                    tmp = lambda x: not(x.done())
                else :
                    raise Exceptions.UnknownFilter(s)
            filter = tmp
        assert(filter != None)
        self.__function = filter

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

    debug("Test completed")
    sys.exit(0)
