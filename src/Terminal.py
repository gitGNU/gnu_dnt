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
import struct
import fcntl
import termios

from   Debug    import *
from   Trace    import *

#
# NOTE:
#     Some tweaks got from:
#         http://pleac.sourceforge.net/pleac_python/userinterfaces.html
#
class Terminal :
    def __init__(self) :
        h = 0
        w = 0
        if (self.interactive()) :
            try :
                s    = struct.pack("HHHH", 0, 0, 0, 0)
                h, w = struct.unpack("HHHH",
                                     fcntl.ioctl(sys.stdout.fileno(),
                                                 termios.TIOCGWINSZ,
                                                 s))[:2]
                debug("Got terminal size")
            except :
                warning("Cannot detect terminal size, using default value")
                # Some (sane ?) default values
                w = 80
                h = 25

        self.__columns = w
        self.__rows    = h
        debug("Terminal size = " +
              "(" + str(self.__columns) + ", " + str(self.__rows) + ")")

    def interactive(self) :
        return (sys.stdin.isatty() and sys.stdout.isatty())

    def rows_get(self) :
        return self.__rows

    rows = property(rows_get, None)

    def columns_get(self) :
        return self.__columns

    columns = property(columns_get, None)

# Test
if (__name__ == '__main__') :
    t = Terminal()

    debug("Test completed")
    sys.exit(0)
