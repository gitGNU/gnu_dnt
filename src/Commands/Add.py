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
import ID
import Time
import Priority
import Entry
import Tree

class SubCommand(Command):
    def __init__(self) :
        Command.__init__(self,
                         name   = "add",
                         footer = "")

    def short_help(self) :
        return "add a new node"

    def authors(self) :
        return [ "Francesco Salvestrini" ]

    def do(self, configuration, arguments) :
        Command.add_option(self,
                           "-t", "--text",
                           action = "store",
                           type   = "string",
                           dest   = "text",
                           help   = "specify node text")
        Command.add_option(self,
                           "-i", "--parent-id",
                           action = "store",
                           type   = "string",
                           dest   = "parent",
                           help   = "specify parent node id")
        Command.add_option(self,
                           "-s", "--start",
                           action = "store",
                           type   = "string",
                           dest   = "start",
                           help   = "specify node start time")
        Command.add_option(self,
                           "-e", "--end",
                           action = "store",
                           type   = "string",
                           dest   = "end",
                           help   = "specify node end time")
        Command.add_option(self,
                           "-p", "--priority",
                           action = "store",
                           type   = "string",
                           dest   = "priority",
                           help   = "specify node priority")

        (opts, args) = Command.parse_args(self, arguments)

        # Parameters setup
        debug("Handling text")
        node_text = opts.text
        if (node_text == None) :
            raise Exceptions.MissingParameters("node text")
        if (node_text == "") :
            raise Exceptions.WrongParameter("node text is empty")

        debug("Handling parent")
        node_parent = opts.parent
        if (node_parent == None) :
            node_parent = "0"

        debug("Handling start")
        node_start = Time.Time()
        if (opts.start != None) :
            node_start.fromstring(opts.start)

        debug("Handling end")
        node_end = None
        if (opts.end != None) :
            node_end.fromstring(opts.end)

        debug("Handling priority")
        node_priority = Priority.Priority()
        if (opts.priority != None) :
            node_priority.fromstring(opts.priority)

        db_file   = configuration.get(PROGRAM_NAME, 'database')
        assert(db_file != None)
        parent_id = ID.ID(node_parent)

        # Work
        debug("Adding node:")
        debug("  node-text = " + node_text)
        debug("  parent-id = " + str(parent_id))
#        debug("  priority  = " + str(node_priority))
#        debug("  start     = " + str(node_start))
#        debug("  end       = " + str(node_end))

        db = DB.Database()
        tree = db.load(db_file)
        assert(tree != None)

        debug("Looking for node `" + str(parent_id) + "'")
        parent = Tree.find(tree, parent_id)
        if (parent == None) :
            raise Exceptions.NodeUnavailable(str(parent_id))

        debug("Parent node for "
              "`" + str(parent_id) + "' "
              "is "
              "`" + str(parent) +"'")

        entry = Entry.Entry(text     = node_text,
                            priority = node_priority,
                            start    = node_start,
                            end      = node_end)
        assert(entry)

        parent.add(entry)

        # Save database back to file
        db.save(db_file, tree)

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
