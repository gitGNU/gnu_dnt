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

class TimeDiff(object) :
    __time = None

    def __init__(self, t) :
        self.__time = t

    def fromstring(self, s) :
        assert(type(s) == str)
        raise Exceptions.WrongTimeFormat(s)

    def tostring(self) :
        t = self.__time.seconds

        seconds = t % 60
        t       = t / 60

        minutes = t % 60
        t       = t / 60

        hours   = t % 60
        t       = t / 60

        assert(t < 24)

        t       = self.__time.days

        days    = t % 30
        t       = t / 30

        months  = t / 12
        t       = t % 12

        years   = t / 365
        t       = t % 365

        return \
            str(years)   + "y " + \
            str(months)  + "m " + \
            str(days)    + "d " + \
            str(hours)   + "h " + \
            str(minutes) + "m " + \
            str(seconds) + "s"

def help() :
    return "A date-time expressed in YYYY-MM-DD HH:MM:SS"

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
            bug("Wrong constructor parameter for Time")
        assert(type(self.__time) == datetime.datetime)
        debug("Time object initialized to `" + self.tostring() + "'")

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
        return int(time.mktime(self.__time.timetuple()))

    def __add__(self, other) :
        assert(type(other) == Time)
        return TimeDiff(self.__time + other.time())

    def __sub__(self, other) :
        assert(type(other) == Time)
        return TimeDiff(self.__time - other.time())

#    def __eq__(self, other) :
#        return (self.__time == other.time())

#    def __ne__(self, other) :
#        return (self.__time != other.time())

    def __gt__(self, other) :
        return (self.__time > other.time())

    def __ge__(self, other) :
        return (self.__time >= other.time())

    def __lt__(self, other) :
        return (self.__time < other.time())

    def __le__(self, other) :
        return (self.__time <= other.time())

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
