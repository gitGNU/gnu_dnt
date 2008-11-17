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

import datetime
import string

from Debug import *
from Trace import *
from Node  import *
from Color import *

class Entry(Node) :
    __text     = ""
    __priority = ""
    __time     = ""

    def __init__(self, t = "", p = "", d = datetime.date.today()) :
	Node.__init__(self)
	self.text_set(t)
	self.priority_set(p)
	self.time_set(d)

    def text_get(self) :
	return self.__text
    def text_set(self, t) :
	assert(t != None)
	# Remove leading and trailing whitespaces from input string
	self.__text = string.rstrip(string.lstrip(t))

    text = property(text_get, text_set)

    def priority_get(self) :
	return self.__priority
    def priority_set(self, p) :
	self.__priority = p

    priority = property(priority_get, priority_set)

    def time_get(self) :
	return self.__time
    def time_set(self, t) :
	self.__time = t

    time = property(time_get, time_set)

    def dump(self, indent, header) :
	i      = 1
	print(indent + header + "" + white(self.__text))

	indent = indent + "    "
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
