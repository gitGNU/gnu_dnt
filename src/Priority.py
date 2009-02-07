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

from   Debug       import *
from   Trace       import *
import Exceptions

class Priority(object) :
    PRIORITY_VERYHIGH = 5
    PRIORITY_HIGH     = 4
    PRIORITY_MEDIUM   = 3
    PRIORITY_LOW      = 2
    PRIORITY_VERYLOW  = 1

    __priority_to_string = {
        PRIORITY_VERYHIGH : "veryhigh",
        PRIORITY_HIGH     : "high",
        PRIORITY_MEDIUM   : "medium",
        PRIORITY_LOW      : "low",
        PRIORITY_VERYLOW  : "verylow",
        }

    __string_to_priority = {
        "veryhigh" : PRIORITY_VERYHIGH,
        "high"     : PRIORITY_HIGH,
        "medium"   : PRIORITY_MEDIUM,
        "low"      : PRIORITY_LOW,
        "verylow"  : PRIORITY_VERYLOW,
        }

    def __init__(self, p = PRIORITY_MEDIUM) :
        self.__priority = p

    def fromstring(self, t) :
        try :
            self.__priority = self.__string_to_priority[t]
        except :
            raise Exceptions.UnknownPriority(t)

    def tostring(self) :
        try :
            return self.__priority_to_string[self.__priority]
        except :
                bug()

    def value(self) :
        return self.__priority

# Test
if (__name__ == '__main__') :
    q = Priority()

    p = Priority()
    p.fromstring("veryhigh")
    assert(p != None)
    s = p.tostring()
    assert(s == "veryhigh")

    p = Priority()
    p.fromstring("high")
    assert(p != None)
    s = p.tostring()
    assert(s == "high")

    p = Priority()
    p.fromstring("medium")
    assert(p != None)
    s = p.tostring()
    assert(s == "medium")

    p = Priority()
    p.fromstring("low")
    assert(p != None)
    s = p.tostring()
    assert(s == "low")

    p = Priority()
    p.fromstring("verylow")
    assert(p != None)
    s = p.tostring()
    assert(s == "verylow")

    debug("Test completed")
    sys.exit(0)
