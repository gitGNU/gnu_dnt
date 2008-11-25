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

import Debug
from   Trace import *

class ID :
    def __init__(self) :
        self.__id = ()
        pass

    def fromstring(self, s) :
        pass

    def tostring(self) :
        s = "0"
        for i in range(0, len(self.__id)) :
            s = s + "." + str(self._id[i])
        return s

# Test
if (__name__ == '__main__') :
    id = ID()
    id.fromstring("0")
    debug("0 = " + id.tostring())

    id.fromstring("0.1")
    debug("0.1 = " + id.tostring())

    id.fromstring("0.1.2")
    debug("0.1.2 = " + id.tostring())

    debug("Test completed")
    sys.exit(0)
