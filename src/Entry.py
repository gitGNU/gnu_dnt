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

import sys  # Useless
import datetime
import string

from   Debug import *
from   Trace import *
from   Node  import *
from   Color import *

class Entry(Node) :
    __text     = ""
    __priority = ""
    __time     = ""

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

    def __init__(self, t = "", p = PRIORITY_MEDIUM, d = datetime.date.today()) :
	Node.__init__(self)
	self.text_set(t)
	self.priority_set(p)
	self.time_set(d)

    def text_get(self) :
	return self.__text
    def text_set(self, t) :
	assert(type(t) == str)
        if (t == "") :
            raise ValueError("empty string")
	# Remove leading and trailing whitespaces from input string
	self.__text = string.rstrip(string.lstrip(t))

    text = property(text_get, text_set)

    def priority_get(self) :
	return self.__priority
    def priority_set(self, p) :
        assert(type(p) == int)
        if (p not in self.__legal_priorities) :
            raise ValueError("not a legal priority")
	self.__priority = p

    priority = property(priority_get, priority_set)

    def time_get(self) :
	return self.__time
    def time_set(self, t) :
	self.__time = t

    time = property(time_get, time_set)

    # XXX FIXME: Move color related code elsewhere
    def dump(self, indent, header) :
        p = self.priority_get()
        if (p == Entry.PRIORITY_VERYHIGH) :
            color = red
        elif (p == Entry.PRIORITY_HIGH) :
            color = yellow
        elif (p == Entry.PRIORITY_MEDIUM) :
            color = white
        elif (p == Entry.PRIORITY_LOW) :
            color = cyan
        elif (p == Entry.PRIORITY_VERYLOW) :
            color = blue
        else :
            bug()

	print(indent + header + "" + color(self.__text))

	indent = indent + "    "
	i      = 1
	for j in self.children() :
	    j.dump(indent, green(str(i) + "."))
	    i = i + 1

# Test
if (__name__ == '__main__') :
    root = Entry("root")
    e1   = Entry("e1")
    e11  = Entry("e11")
    e12  = Entry("e12")
    e2   = Entry("e2")

    e1.child(0, e12)
    e1.child(0, e11)
    root.child(0, e1)
    root.child(1, e2)

    root.dump(" ", "")

    debug("Test completed")
    sys.exit(0)
