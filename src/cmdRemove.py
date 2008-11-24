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
    return "remove node(s) (and children)"

def do(configuration, arguments) :
    command = Command("remove")

    command.add_option("-i", "--id",
                       action = "store",
                       type   = "string",
                       dest   = "source",
                       help   = "specify node to remove")

    (opts, args) = command.parse_args(arguments)

    filter = None
    # Parse filter here
    if (filter == None) :
	raise Exceptions.Parameters("filter is empty")

    id = None
    # Find node
    node = None
    if (node == None) :
	raise Exceptions.Parameters("node `" + id +"' not found")

    return 0

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
