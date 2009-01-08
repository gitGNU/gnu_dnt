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
import datetime
import time

from   Debug import *
from   Trace import *

class Time(object) :
    __time = None

    def __init__(self, t = datetime.datetime.now()) :
        self.__time = t

    def __str__(self) :
        assert(self.__time != None)
        return self.tostring()

    # XXX FIXME: Add try/except here ...
    def fromstring(self, s) :
        assert(self.__time != None)
        a = s.split(" ")
        d = a.split("-")
        t = a.split(":")
        year    = d[0]
        month   = d[1]
        day     = d[2]
        hour    = t[0]
        minutes = t[1]
        secs    = t[2]
        self.__time = datetime.datetime(year, month, day, hour, minutes, secs)

    def tostring(self) :
        assert(self.__time != None)
        return  self.__time.strftime("%Y-%m-%d %H:%M:%S")

# Test
if (__name__ == '__main__') :
    t = Time()
    debug("Time is = " + str(t))
    debug("Test completed")
    sys.exit(0)
