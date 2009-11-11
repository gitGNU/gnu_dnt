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

from   Debug      import *
from   Trace      import *
import Exceptions

class Enum(object) :
    __initialized = False

    def __init__(self, *args, **kw) :
        self.__names = args
        self.__dict  = {}

        value = 0
        for name in args :
            if (kw.has_key(name)) :
                value = kw[name]
            self.__dict[name] = value
            value = value + 1

        self.__initialized = True

    def __getitem__(self, item) :
        assert(self.__initialized)
        name = self.__names[item]
        return getattr(self, name)

    def __getattr__(self, name) :
        assert(self.__initialized)
        return self.__dict[name]

#    def __setattr__(self, name, value) :
#        if (not self.__initialized) :
#            self.__dict[name] = value
#        else :
#            raise Exceptions.ReadOnlyEnum(name)

    def __call__(self, name_or_value) :
        assert(self.__initialized)
        if (isinstance(name_or_value, int)) :
            for name in self.__names :
                if (getattr(self, name) == name_or_value) :
                    return name
                else :
                    raise Exceptions.UnknownEnum(str(name_or_value))
        else :
            return getattr(self, name_or_value)

    def __repr__(self) :
        assert(self.__initialized)
        result = []
        for name in self.__names :
            result.append("%s=%d" % (name, getattr(self, name)))
        return '<Enum ' + string.join(result) + '>'

# Test
if (__name__ == '__main__') :
    color = Enum('red', 'yellow', 'green', 'blue', 'black',
                 yellow = 10, green = 20)

    print color
    print color.red
    print color.yellow
    print color.green
    print color.blue

    alfa  = color.red
    beta  = color.green
    gamma = color.red

    if (alfa != gamma) :
        sys.exit(1)

    if (alfa == beta) :
        sys.exit(1)

    test = Enum('test')

    debug("Test completed")
    sys.exit(0)
