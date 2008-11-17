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

from Trace import *

class Options :
    __opts = {}

    def __init__(self, opts) :
        for i in opts :
            self.__opts[i] = None

    def set(self, name, value) :
        opts[name] = value

    def dump(self) :
        debug("Options:")
        for i in self.__opts :
            t = self.__opts[i]
            assert(t != None)
            debug("  " + i + " = " + str(t))

# Test
if (__name__ == '__main__') :
    options = Options([ 'alfa', 'beta', 'gamma' ])

    options.set(alfa)
    options.dump()
    debug("Test completed")
