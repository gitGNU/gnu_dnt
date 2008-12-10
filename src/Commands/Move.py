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

from   Debug         import *
from   Trace         import *
from   Command       import *
import Exceptions
from   Configuration import *
import DB
from   ID            import *
import Entry

def description() :
    return "reparent node(s)"

def do(configuration, arguments) :
    command = Command("move")
    command.add_option("-n", "--node-id",
                       action = "store",
                       type   = "string",
                       dest   = "node",
                       help   = "specify target node id")
    command.add_option("-p", "--parent-id",
                       action = "store",
                       type   = "string",
                       dest   = "parent",
                       help   = "specify destination parent node id")

    (opts, args) = command.parse_args(arguments)

    # Parameters setup
    if (opts.node == None) :
        raise Exceptions.MissingParameters("node id")
    node_id = ID(opts.node)
    if (opts.parent == None) :
        raise Exceptions.MissingParameters("parent id")
    parent_id = ID(opts.parent)

    # Work
    db_file   = configuration.get(PROGRAM_NAME, 'database')
    assert(db_file != None)

    debug("Moving node:")
    debug("  node-id   = " + str(node_id))
    debug("  parent-id = " + str(parent_id))

    db = DB.Database()

    # Load database from file
    tree = db.load(db_file)
    assert(tree != None)

    debug("Looking for node `" + str(parent_id) + "'")
    parent = Entry.find(tree, parent_id)
    if (parent == None) :
        raise Exceptions.WrongParameters("unknown node "
                                         "`" + str(parent_id) + "'")

    debug("Looking for node `" + str(node_id) + "'")
    node = Entry.find(tree, node_id)
    if (node == None) :
        raise Exceptions.WrongParameters("unknown node "
                                     "`" + str(node_id) + "'")

    # Remove parent subtree link
    node_parent = node.parent
    if (node_parent == None) :
        bug()
    node_parent.remove(node)

    # Link node subtree into parent substree
    parent.add(node)

    #tree.dump("")

    # Save database back to file
    db.save(db_file, tree)

    debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
