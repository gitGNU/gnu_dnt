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
from   Command    import *
import Exceptions

def description() :
    return "reparent node(s)"

def do(configuration, arguments) :
    command = Command("move")
    command.add_option("-s", "--source",
                       action = "store",
                       type   = "string",
                       dest   = "source",
                       help   = "specify source node")
    command.add_option("-d", "--destination",
                       action = "store",
                       type   = "string",
                       dest   = "destination",
                       help   = "specify destination node")

    (opts, args) = command.parse_args(arguments)

    # Parameters setup
    if (opts.source == None) :
        raise Exceptions.MissingParameters("source node")
    source_id = ID(opts.source)
    if (opts.destination == None) :
        raise Exceptions.MissingParameters("destination node")
    destination_id = ID(opts.destination)

    # Work

    return 0

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
