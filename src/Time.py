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

from   Debug      import *
from   Trace      import *
import Exceptions

class Time(object) :
    __time = None

    def __init__(self, t = datetime.datetime.now()) :
        if (type(t) == str) :
            self.fromstring(t)
        elif (type(t) == int) :
            self.fromint(t)
        elif (type(t) == datetime.datetime) :
            self.__time = t
        else :
            bug()
        assert(type(self.__time) == datetime.datetime)

    def __str__(self) :
        assert(self.__time != None)
        return self.tostring()

    def time(self) :
        return self.__time

    def fromstring(self, s) :
        assert(type(s) == str)
        try :
            args = time.strptime(s,"%Y-%m-%d %H:%M:%S")[0:5]
            self.__time = datetime.datetime(*args)
        except :
            raise Exceptions.WrongTimeFormat(s)

    def tostring(self) :
        return self.__time.strftime("%Y-%m-%d %H:%M:%S")

    def fromint(self, i) :
        assert(type(i) == int)
        try :
            self.__time = datetime.datetime.fromtimestamp(i)
        except :
            raise Exceptions.WrongTimeFormat(str(i))

    def toint(self) :
        return int(self.__time.toordinal())

    def __add__(self, other) :
        self.__time = self.__time + other.time()

    def __sub__(self, other) :
        self.__time = self.__time - other.time()

#    def __eq__(self, other) :
#        return (self.__time == other.time())
#
#    def __ne__(self, other) :
#        return (self.__time != other.time())
#
#    def __ge__(self, other) :
#        pass
#
#    def __gt__(self, other) :
#        pass
#
#    def __le__(self, other) :
#        pass
#
#    def __lt__(self, other) :
#        pass

# Test
if (__name__ == '__main__') :
    now = Time()
    debug("Time is = " + str(now))

    now = Time(700000)
    debug("Time is = " + str(now))

    now = Time(datetime.datetime.now())
    debug("Time is = " + str(now))

    now = Time("1980-02-03 10:11:12")
    debug("Time is = " + str(now))
    now.fromstring("1970-4-5 10:00:11")
    debug("Time is = " + str(now))

    t1 = Time("2008-11-2 1:1:1")
    debug("Time is = " + str(t1))

    t2 = Time("2008-11-2 1:1:1")
    debug("Time is = " + str(t2))

#    assert(t2 == t1)
#    assert(t1 == t2)

    debug("Test completed")
    sys.exit(0)
