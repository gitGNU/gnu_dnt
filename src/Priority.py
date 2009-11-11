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

from   Debug       import *
from   Trace       import *
import Exceptions

PRIORITY_VERYHIGH = 5
PRIORITY_HIGH     = 4
PRIORITY_MEDIUM   = 3
PRIORITY_LOW      = 2
PRIORITY_VERYLOW  = 1

__values2names = {
    PRIORITY_VERYHIGH : "veryhigh",
    PRIORITY_HIGH     : "high",
    PRIORITY_MEDIUM   : "medium",
    PRIORITY_LOW      : "low",
    PRIORITY_VERYLOW  : "verylow",
    }

__names2values = {
    "veryhigh" : PRIORITY_VERYHIGH,
    "high"     : PRIORITY_HIGH,
    "medium"   : PRIORITY_MEDIUM,
    "low"      : PRIORITY_LOW,
    "verylow"  : PRIORITY_VERYLOW,
    }

# XXX FIXME: An ugly hack to access __names2values from a Priority object
def names() :
    return __names2values.keys()

def goodname(name) :
    if (name in __names2values) :
        return True
    return False

def name2value(name) :
    if (goodname(name)) :
        return __names2values[string.lower(name)]
    raise Exceptions.UnknownPriorityName(name)

def goodvalue(value) :
    if (value in __values2names) :
        return True
    return False

def value2name(value) :
    if (goodvalue(value)) :
        return __values2names[value]
    raise Exceptions.UnknownPriorityValue(str(value))

def help_text() :
    prios = __names2values.keys()
    tmp   = "Recognized priorities are: "

    tmp = tmp + prios[0]
    for i in prios[1:] :
        tmp = tmp + ", " + i

    return tmp

class Priority(object) :
    def __init__(self, p = PRIORITY_MEDIUM) :
        if (isinstance(p, int)) :
            self.fromint(p)
        elif (isinstance(p, str)) :
            self.fromstring(p)
        else :
            raise Exceptions.WrongPriorityFormat(str(p))
        assert(isinstance(self.__priority, int))

    def fromstring(self, t) :
        if (not isinstance(t, str)) :
            raise Exceptions.WrongPriorityFormat(str(t))
        s = string.strip(t)
        self.__priority = name2value(s)

    def tostring(self) :
        return value2name(self.__priority)

    def fromint(self, t) :
        if (not isinstance(t, int)) :
            raise Exceptions.WrongPriorityFormat(str(t))

        if (goodvalue(t)) :
            self.__priority = t
        else :
            raise Exceptions.UnknownPriorityName(t)

    def toint(self) :
        return self.__priority

    def __value_get(self) :
        return self.__priority

    value = property(__value_get, None, None, None)

    def __priorities_get(self) :
        return names()

    priorities = property(__priorities_get, None, None, None)

    #
    # Comparison operators
    #

    def __eq__(self, other) :
        if (isinstance(other, Priority)) :
            return (self.__priority == other.__priority)
        if (isinstance(other, str) or
            isinstance(other, int)) :
            return (self == Priority(other))
        return False

    def __ne__(self, other) :
        if (isinstance(other, Priority)) :
            return (self.__priority != other.__priority)
        if (isinstance(other, str) or
            isinstance(other, int)) :
            return (self != Priority(other))
        return True

    def __gt__(self, other) :
        if (isinstance(other, Priority)) :
            return (self.__priority > other.__priority)
        if (isinstance(other, str) or
            isinstance(other, int)) :
            return (self > Priority(other))
        raise Exceptions.WrongPriorityFormat(str(other))

    def __ge__(self, other) :
        if (isinstance(other, Priority)) :
            return (self.__priority >= other.__priority)
        if (isinstance(other, str) or
            isinstance(other, int)) :
            return (self >= Priority(other))
        raise Exceptions.WrongPriorityFormat(str(other))

    def __lt__(self, other) :
        if (isinstance(other, Priority)) :
            return (self.__priority < other.__priority)
        if (isinstance(other, str) or
            isinstance(other, int)) :
            return (self < Priority(other))
        raise Exceptions.WrongPriorityFormat(str(other))

    def __le__(self, other) :
        if (isinstance(other, Priority)) :
            return (self.__priority <= other.__priority)
        if (isinstance(other, str) or
            isinstance(other, int)) :
            return (self <= Priority(other))
        raise Exceptions.WrongPriorityFormat(str(other))

# Test
if (__name__ == '__main__') :
    q = Priority()

    a = q.priorities
    for i in __names2values.keys() :
        assert(i in a)

    for s in __names2values.keys() :
        p = Priority()
        p.fromstring(s)
        t = p.tostring()
        assert(s == t)

    for s in __names2values.keys() :
        p = Priority(s)
        t = p.tostring()
        assert(s == t)

    for s in __values2names.keys() :
        p = Priority(s)
        t = p.toint()
        assert(s == t)

    for s in __names2values.keys() :
        p = Priority()
        p.fromstring(s)
        a = p.toint()
        p.fromint(a)
        b = p.tostring()
        assert(b == s)

    a = Priority("verylow")
    b = Priority("low")
    c = Priority("medium")
    d = Priority("high")
    e = Priority("veryhigh")

    assert(a != None)
    assert(b != None)
    assert(c != None)
    assert(d != None)
    assert(e != None)

    assert(a.toint() == PRIORITY_VERYLOW)
    assert(b.toint() == PRIORITY_LOW)
    assert(c.toint() == PRIORITY_MEDIUM)
    assert(d.toint() == PRIORITY_HIGH)
    assert(e.toint() == PRIORITY_VERYHIGH)

    assert(a != b)
    assert(b != c)
    assert(c != d)
    assert(d != e)

    assert(a <  b)
    assert(b <  c)
    assert(c <  d)
    assert(d <  e)

    assert(a <= b)
    assert(b <= c)
    assert(c <= d)
    assert(d <= e)

    a = Priority("veryhigh")
    b = Priority("high")
    c = Priority("medium")
    d = Priority("low")
    e = Priority("verylow")

    assert(a != None)
    assert(b != None)
    assert(c != None)
    assert(d != None)
    assert(e != None)

    assert(a != b)
    assert(b != c)
    assert(c != d)
    assert(d != e)

    assert(a >  b)
    assert(b >  c)
    assert(c >  d)
    assert(d >  e)

    assert(a >= b)
    assert(b >= c)
    assert(c >= d)
    assert(d >= e)

    a = Priority(PRIORITY_VERYLOW)
    b = Priority(PRIORITY_LOW)
    c = Priority(PRIORITY_MEDIUM)
    d = Priority(PRIORITY_HIGH)
    e = Priority(PRIORITY_VERYHIGH)

    assert(a != None)
    assert(b != None)
    assert(c != None)
    assert(d != None)
    assert(e != None)

    assert(a != b)
    assert(b != c)
    assert(c != d)
    assert(d != e)

    assert(a <  b)
    assert(b <  c)
    assert(c <  d)
    assert(d <  e)

    assert(a <= b)
    assert(b <= c)
    assert(c <= d)
    assert(d <= e)

    a = Priority(PRIORITY_VERYHIGH)
    b = Priority(PRIORITY_HIGH)
    c = Priority(PRIORITY_MEDIUM)
    d = Priority(PRIORITY_LOW)
    e = Priority(PRIORITY_VERYLOW)

    assert(a != None)
    assert(b != None)
    assert(c != None)
    assert(d != None)
    assert(e != None)

    assert(a != b)
    assert(b != c)
    assert(c != d)
    assert(d != e)

    assert(a >  b)
    assert(b >  c)
    assert(c >  d)
    assert(d >  e)

    assert(a >= b)
    assert(b >= c)
    assert(c >= d)
    assert(d >= e)

    debug("Test completed")
    sys.exit(0)
