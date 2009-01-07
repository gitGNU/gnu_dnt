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

from   Debug            import *
from   Trace            import *
from   Commands.Command import *
import Exceptions

import ID

class SubCommand(Command) :
    def __init__(self) :
        Command.__init__(self, "touch")

    def description(self) :
        return "touch node start and/or end date"

    def authors(self) :
        return [ "Francesco Salvestrini" ]

    def do(self, configuration, arguments) :
        Command.add_option(self,
                           "-s", "--start",
                           action = "store",
                           type   = "string",
                           dest   = "start",
                           help   = "specify start time")
        Command.add_option(self,
                           "-e", "--end",
                           action = "store",
                           type   = "string",
                           dest   = "end",
                           help   = "specify end time")

        (opts, args) = Command.parse_args(self, arguments)

        # Parameters setup

        # Work

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
