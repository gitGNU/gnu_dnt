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

import DB
import Entry
from   ID         import *

def description() :
    return "dump current configuration"

def do(configuration, arguments) :
    command = Command("config")

    command.add_option("-s", "--set",
		       action = "store",
		       dest   = "set",
		       help   = "set a (local) configuration parameter value")
    command.add_option("-g", "--get",
		       action = "store",
		       dest   = "get",
		       help   = "get a configuration parameter value")
    command.add_option("-S", "--show",
		       action = "store_true",
		       dest   = "show",
		       help   = "show all configuration values")

    (opts, args) = command.parse_args(arguments)

    # Parameters setup

    # Work

    # Compute maximum configuration key length
    m = 0
    for i in configuration.keys() :
	m = max(m, len(str(configuration[i])) + 1)
    # Write all key-value pairs
    for i in configuration.keys() :
	print(("%-" + str(m) + "s = %s") %(i, str(configuration[i])))

    return 0

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
