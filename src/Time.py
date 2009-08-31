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
#import string
import datetime
import time
import re

from   Debug      import *
from   Trace      import *
import Exceptions

class TimeDiff(object) :
    __time = None

    def __init__(self, t) :
        self.__time = t

#    def fromstring(self, s) :
#        assert(isinstance(s, str))
#        raise Exceptions.WrongTimeFormat(s)

    def tostring(self) :
        t = self.__time.seconds

        seconds = t % 60
        t       = t / 60
        assert(seconds < 60)

        minutes = t % 60
        t       = t / 60
        assert(minutes < 60)

        hours   = t % 60
        t       = t / 60
        assert(hours < 24)

        t       = self.__time.days

        days    = t % 30
        t       = t / 30
        assert(days < 31)

        months  = t / 12
        t       = t % 12
        assert(months < 12)

        years   = t / 365
        t       = t % 365

        return \
            str(years)   + "y " + \
            str(months)  + "m " + \
            str(days)    + "d " + \
            str(hours)   + "h " + \
            str(minutes) + "m " + \
            str(seconds) + "s"

def help_text() :
    return "A date-time expressed in YYYY-MM-DD [HH:MM:SS]"

class Time(object) :
    __time = None

    def __init__(self, t = datetime.datetime.now()) :
        if (isinstance(t, str)) :
            self.fromstring(t)
        elif (isinstance(t, int)) :
            self.fromint(t)
        elif (isinstance(t, datetime.datetime)) :
            self.__time = t
        else :
            raise Exceptions.WrongTimeFormat(str(t))
        assert(isinstance(self.__time, datetime.datetime))
        debug("Time object initialized to `" + self.tostring() + "'")

    def __str__(self) :
        assert(self.__time != None)
        return self.tostring()

    def time(self) :
        return self.__time

    def fromstring(self, t) :
        assert(isinstance(t, str))

        # Splitting text
        d = filter(None, re.split(r'\s+', t))

        # Default date values (year, month, day, hour,
        # minutes, seconds), year is set to None as
        # control item
        date = [ None, # Year
                 "01", # Month
                 "01", # Day
                 "00", # Hour
                 "00", # Minutes
                 "00"  # Seconds
                 ]

        for i in d :
            # Matching date string
            if re.match(r'^\d{1,4}\-', i) :
                x = filter(None, i.split('-'))

                try :
                    assert(len(x) <= 3)
                except :
                    raise Exceptions.WrongTimeFormat(t)

                # Fill array date elements
                c = 0

                for j in x :
                    date[c] = j
                    c += 1

            # Matching time string
            elif re.match(r'^\d{1,2}:', i) :
                x = filter(None, i.split(':'))

                try :
                    assert(len(x) <= 3)
                except :
                    raise Exceptions.WrongTimeFormat(t)

                # Fill array time elements
                c = 3

                for j in x :
                    date[c] = j
                    c += 1

            # Single digit token, handling as year token
            elif re.match(r'^\d{1,4}$', i) :

                if date[0] != None :
                    raise Exceptions.WrongTimeFormat(t)

                # Fill array year element
                date[0] = i
            else :
                # Invalid input
                raise Exceptions.WrongTimeFormat(t)

        # Building date string
        if date[0] == None :
            # If date is not passed (year value is not
            # passed) then we'll take today
            s = time.strftime("%Y-%m-%d") + ' ' + \
                date[3] + ':' + date[4] + ':' + date[5]
        else :
            s = date[0] + '-' + date[1] + '-' + date[2] + ' ' + \
                date[3] + ':' + date[4] + ':' + date[5]

        try :
            args = time.strptime(s, "%Y-%m-%d %H:%M:%S")[0:6]
            self.__time = datetime.datetime(*args)
        except :
            raise Exceptions.WrongTimeFormat(t)

        assert(self.__time != None)
        debug("Time object set to `" + str(self.__time) + "'")

    def tostring(self) :
        return self.__time.strftime("%Y-%m-%d %H:%M:%S")

    def fromint(self, i) :
        assert(isinstance(i, int))
        try :
            self.__time = datetime.datetime.fromtimestamp(i)
        except :
            raise Exceptions.WrongTimeFormat(str(i))

    def toint(self) :
        return int(time.mktime(self.__time.timetuple()))

    def __add__(self, other) :
        assert(isinstance(self, other))
        return TimeDiff(self.__time + other.time())

    def __sub__(self, other) :
        assert(isinstance(self, other))
        return TimeDiff(self.__time - other.time())

    #
    # Comparison operators
    #

    def __eq__(self, other) :
        if (isinstance(other, Time)) :
            return (self.__time == other.time())
        if (isinstance(other, str)) :
            return (self == Time(other))
        return False

    def __ne__(self, other) :
        if (isinstance(other, Time)) :
            return (self.__time != other.time())
        if (isinstance(other, str)) :
            return (self != Time(other))
        return True

    def __gt__(self, other) :
        if (isinstance(other, Time)) :
            return (self.__time > other.time())
        if (isinstance(other, str)) :
            return (self > Time(other))
        raise Exceptions.WrongTimeFormat(str(other))

    def __ge__(self, other) :
        if (isinstance(other, Time)) :
            return (self.__time >= other.time())
        if (isinstance(other, str)) :
            return (self >= Time(other))
        raise Exceptions.WrongTimeFormat(str(other))

    def __lt__(self, other) :
        if (isinstance(other, Time)) :
            return (self.__time < other.time())
        if (isinstance(other, str)) :
            return (self < Time(other))
        raise Exceptions.WrongTimeFormat(str(other))

    def __le__(self, other) :
        if (isinstance(other, Time)) :
            return (self.__time <= other.time())
        if (isinstance(other, str)) :
            return (self <= Time(other))
        raise Exceptions.WrongTimeFormat(str(other))

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
    assert(t2 == t1)

    t2 = Time("2008-11-2 1:1:2")
    assert(t1 != t2)
    assert(t1 <= t2)
    assert(t2 >= t1)
    t2 = Time("2008-11-2 1:2:1")
    assert(t1 != t2)
    assert(t1 <= t2)
    assert(t2 >= t1)
    t2 = Time("2008-11-2 2:1:1")
    assert(t1 != t2)
    assert(t1 <= t2)
    assert(t2 >= t1)
    t2 = Time("2008-11-3 1:1:1")
    assert(t1 != t2)
    assert(t1 <= t2)
    assert(t2 >= t1)
    t2 = Time("2008-12-2 2:1:1")
    assert(t1 != t2)
    assert(t1 <= t2)
    assert(t2 >= t1)
    t2 = Time("2009-11-2 2:1:1")
    assert(t1 != t2)
    assert(t1 <= t2)
    assert(t2 >= t1)

    t2 = t1
    assert(t1 == t2)
    assert(t1 <= t2)
    assert(t2 >= t1)

    t1 = Time("2008-11-2 1:1:1")
    t2 =      "2009-11-2 2:1:1"
    assert(t1 != t2)
    assert(t1 <= t2)
    assert(t2 >= t1)
    assert(t1 <  t2)
    assert(t2 >  t1)

    t1 = Time("2008")
    t2 =      "2009"
    assert(t1 != t2)
    assert(t1 <= t2)
    assert(t2 >= t1)
    assert(t1 <  t2)
    assert(t2 >  t1)

    t1 = Time("2008")
    t2 =      "2008-02"
    assert(t1 != t2)
    assert(t1 <= t2)
    assert(t2 >= t1)
    assert(t1 <  t2)
    assert(t2 >  t1)

    t1 = Time(time.strftime("%Y-%m-%d") + ' 12:00:00')
    t2 =      "12:00:01"
    assert(t1 != t2)
    assert(t1 <= t2)
    assert(t2 >= t1)
    assert(t1 <  t2)
    assert(t2 >  t1)

    debug("Test completed")
    sys.exit(0)
