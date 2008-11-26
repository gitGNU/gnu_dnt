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

from   ID         import *

def description() :
    return "remove node(s)"

def do(configuration, arguments) :
    command = Command("remove")

    command.add_option("-i", "--id",
		       action = "store",
		       type   = "string",
		       dest   = "id",
		       help   = "specify node id to remove")
    command.add_option("-r", "--recursive",
		       action = "store_true",
		       dest   = "recursive",
		       help   = "remove node and its children recursively")

    (opts, args) = command.parse_args(arguments)

    # Parameters setup
    if (opts.id == None) :
	raise Exceptions.MissingParameters("node id")

    id = ID(opts.id)

    # Work

    return 0

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
