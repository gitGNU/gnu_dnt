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
    return "export a foreign database format"

def do(configuration, arguments) :
    command = Command("import")
    command.add_option("-f", "--file",
		       action = "store",
		       dest   = "file",
		       help   = "specify file to import")
    command.add_option("-t", "--type",
		       action = "store",
		       dest   = "type",
		       help   = "specify type")

    (opts, args) = command.parse_args(arguments)

    # Parameters setup
    if (opts.file == None) :
        raise Exceptions.MissingParameters("output file name")
    if (opts.type == None) :
        raise Exceptions.MissingParameters("output file type")

    # Work

    return 0

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
