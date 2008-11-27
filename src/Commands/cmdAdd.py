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
    return "add a new node"

def do(configuration, arguments) :
    command = Command("add")
    command.add_option("-t", "--text",
                       action = "store",
                       type   = "string",
                       dest   = "text",
                       help   = "specify node text")
    command.add_option("-p", "--parent-id",
                       action = "store",
                       type   = "string",
                       dest   = "parent",
                       help   = "specify parent node id")

    (opts, args) = command.parse_args(arguments)

    # Parameters setup
    if (opts.text == None) :
        raise Exceptions.MissingParameters("node text")
    if (opts.text == "") :
        raise Exceptions.WrongParameters("node text is empty")
    if (opts.parent == None) :
        warning("Parent id is missing, using root as parent for this node")
        opts.parent = "0"

    parent_id = ID(opts.parent)
    node_text = opts.text

    # Work
    debug("Adding node with:")
    debug("  node-text = " + node_text)
    debug("  parent-id = " + str(parent_id))

    return 0

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
