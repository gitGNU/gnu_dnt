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

    __legal_priorities = ( PRIORITY_VERYHIGH,
                           PRIORITY_HIGH,
                           PRIORITY_MEDIUM,
                           PRIORITY_LOW,
                           PRIORITY_VERYLOW )

    def __init__(self, p = PRIORITY_MEDIUM) :
        self.__priority = p

    def increase(self) :
        self.__priority = self.__priority + 1
        if (self.__priority > PRIORITY_VERYHIGH) :
            self.__priority = PRIORITY_VERYHIGH

    def decrease(self) :
        self.__priority = self.__priority - 1
        if (self.__priority < PRIORITY_VERYLOW) :
            self.__priority = PRIORITY_VERYLOW

    def fromstring(self, t) :
        if (t == "veryhigh") :
            self.__priority = self.PRIORITY_VERYHIGH
        elif (t == "high") :
            self.__priority = self.PRIORITY_HIGH
        elif (t == "medium") :
            self.__priority = self.PRIORITY_MEDIUM
        elif (t == "low") :
            self.__priority = self.PRIORITY_LOW
        elif (t == "verylow") :
            self.__priority = self.PRIORITY_VERYLOW
        else :
            raise Exceptions.EPriority.UnknownPriority(t)

    def tostring(self) :
        p = self.__priority
        if (p == self.PRIORITY_VERYHIGH) :
            return "veryhigh"
        elif (p == self.PRIORITY_HIGH) :
            return "high"
        elif (p == self.PRIORITY_MEDIUM) :
            return "medium"
        elif (p == self.PRIORITY_LOW) :
            return "low"
        elif (p == self.PRIORITY_VERYLOW) :
            return "verylow"
        else :
            bug()

    def value(self) :
        return self.__priority

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
