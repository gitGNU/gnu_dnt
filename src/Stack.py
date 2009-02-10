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

from   Debug      import *
from   Trace      import *
import Exceptions

class Stack(object) :
    def __init__(self) :
        self.__stack = []

    def push(self, object) :
        self.__stack.append(object)

    def pop(self) :
        if (len(self.__stack) == 0) :
            raise Exceptions.EmptyStack()
        object = self.__stack[-1]
        del self.__stack[-1]
        return object

    def empty(self) :
        if (len(self.__stack) == 0) :
            return True
        return False

    def len(self) :
        return len(self.__stack)

# Test
if (__name__ == '__main__') :
    s = Stack()

#    if (s.len() != 0) :
#        sys.exit(1)
#
#    s.push("Hi")
#    s.push(12)
#    s.push(3.2)
#
#    if (s.empty()) :
#        sys.exit(1)
#
#    el = s.pop()
#    if (s.empty()) :
#        sys.exit(1)
#    if (el != 3.2) :
#        sys.exit(1)
#
#    el = s.pop()
#    if (s.empty()) :
#        sys.exit(1)
#    if (el != 12) :
#        sys.exit(1)
#
#    el = s.pop()
#    if (s.empty()) :
#        sys.exit(1)
#    if (el != "Hi") :
#        sys.exit(1)
#
#    if (not(s.empty())) :
#        sys.exit(1)

    debug("Test completed")
    sys.exit(0)
