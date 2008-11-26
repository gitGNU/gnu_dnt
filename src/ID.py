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
import string

import Debug
from   Trace import *

class ID :
    def __init__(self, s = "0") :
        assert(type(s) == str)

        x = []
        for n in string.split(s, ".") :
            x.append(int(n))
        self.__id = x

    def __str__(self) :
	s = ""
	for i in range(0, len(self.__id)) :
	    if (i != 0) :
		s = s + "."
	    s = s + str(self.__id[i])
	return s

# Test
if (__name__ == '__main__') :
    def proc(i) :
        id = ID(i)
        assert(i == str(id))
        debug(i + " = " + str(id))

    proc("0")
    proc("0.1")
    proc("0.1.2")
    proc("0.1.2.3")
    proc("1.2.3.4")
    proc("4.3.2")
    proc("7.2")

    debug("Test completed")
    sys.exit(0)
