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

import sys  # Useless

from   Debug import *
from   Trace import *
import Exceptions

def description() :
    return "edit a node"

def help() :
    print("Usage: " + PROGRAM_NAME + " edit")
    print("")
    print("Report bugs to <" + PACKAGE_BUGREPORT + ">")
    return 0

def do(configuration, args) :
    id = None

    # Find node
    node = None
    if (node == None) :
	raise Exceptions.Parameters("node `" + id +"' not found")

    # Edit it now

    return 0

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
