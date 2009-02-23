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

import os
import sys

from   Debug      import *
from   Trace      import *
from   Command    import *
import Exceptions
import DB
import ID
import Entry
import Tree
import Time
import Priority
import Console

class SubCommand(Command) :
    def __init__(self) :
        Command.__init__(self,
                         name   = "edit",
                         footer = [
                "ID        " + ID.help(),
                "PRIORITY  " + Priority.help(),
                "START     " + Time.help(),
                "END       " + Time.help()
                ])

    def short_help(self) :
        return "edit a node"

    def authors(self) :
        return [ "Francesco Salvestrini" ]

    def do(self, configuration, arguments) :
        #
        # Parameters setup
        #
        Command.add_option(self,
                           "-i", "--id",
                           action = "store",
                           type   = "string",
                           dest   = "id",
                           help   = "specify node id to edit")
        Command.add_option(self,
                           "-t", "--text",
                           action = "store",
                           type   = "string",
                           dest   = "text",
                           help   = "specify node text")
        Command.add_option(self,
                           "-p", "--priority",
                           action = "store",
                           type   = "string",
                           dest   = "priority",
                           help   = "specify node priority")
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
                           "-I", "--interactive",
                           action = "store_true",
                           dest   = "interactive",
                           help   = "edit information interactively")
#        Command.add_option(self,
#                           "-E", "--editor",
#                           action = "store",
#                           type   = "string",
#                           dest   = "editor",
#                           help   = "specify editor to use")

        (opts, args) = Command.parse_args(self, arguments)
        if (len(args) > 0) :
            raise Exceptions.UnknownParameter(args[0])

        if (opts.id == None) :
            raise Exceptions.MissingParameters("node id")

        if ((opts.text        == None) and
            (opts.priority    == None) and
            (opts.start       == None) and
            (opts.end         == None) and
            (opts.interactive == None)) :
            raise Exceptions.MissingParameters()

#        editor = None
#        # Prefer parameter
#        if (editor == None) :
#            editor = opts.editor
#        # Fall-back to configuration
#        if (editor == None) :
#            try :
#                editor = configuration.get(Command.name,
#                                           'editor',
#                                           raw = True)
#            except :
#                # No editor found on configuration
#                pass
#        # Fall-back to the environment
#        if (editor == None) :
#            editor = os.environ["EDITOR"]
#        # Finally bang with error
#        if (editor == None) :
#            raise MissingParameters("editor")
#        debug("Editor will be `" + editor + "'")

        node_id = ID.ID(opts.id)
        debug("Editing node:")
        debug("  id = " + str(node_id))

        #
        # Load database from file
        #
        db_file = configuration.get(PROGRAM_NAME, 'database')
        assert(db_file != None)
        db      = DB.Database()
        tree    = db.load(db_file)
        assert(tree != None)

        #
        # Work
        #
        debug("Looking for node `" + str(node_id) + "'")
        node = Tree.find(tree, node_id)
        if (node == None) :
            raise Exceptions.WrongParameter("unknown node " +
                                            "`" + str(node_id) + "'")

        # Set the starting values
        text     = None
        priority = None
        start    = None
        end      = None

        # Look for all the values
        if (opts.text != None) :
            text = opts.text
            debug("Got text value from user")
        else :
            text = node.text
            if (text != None) :
                debug("Got text value from node")

        if (opts.priority != None) :
            priority = opts.priority
            debug("Got priority value from user")
        else :
            o = node.priority
            if (o != None) :
                priority = o.tostring()
                debug("Got priority value from node")

        if (opts.start != None) :
            start = opts.start
            debug("Got start value from user")
        else :
            o = node.start
            if (o != None) :
                start = o.tostring()
                debug("Got start value from node")

        if (opts.end != None) :
            end = opts.end
            debug("Got end value from user")
        else :
            o = node.end
            if (o != None) :
                end = o.tostring()
                debug("Got end value from node")

        # Use str() in order to avoid problems with None values
        debug("Got values from user")
        debug("text     = `" + str(text)     + "'")
        debug("priority = `" + str(priority) + "'")
        debug("start    = `" + str(start)    + "'")
        debug("end      = `" + str(end)      + "'")

        if (opts.interactive == True) :
            console = Console.Console()
            assert(console != None)

            tmp = text
            if (tmp == None) :
                tmp = ""
            tmp = console.interact("text> ", tmp)
            if (tmp != text) :
                text = tmp
            del tmp

            tmp = priority
            if (tmp == None) :
                tmp = "medium"
            tmp = console.interact("priority> ",
                                   tmp,
                                   Priority.Priority().priorities)
            if (tmp != priority) :
                priority = tmp
            del tmp

            tmp = start
            if (tmp == None) :
                tmp = ""
            tmp = console.interact("start> ", tmp)
            if (tmp != start) :
                start = tmp
            del tmp

            tmp = end
            if (tmp == None) :
                tmp = ""
            tmp = console.interact("end> ", tmp)
            if (tmp != end) :
                end = tmp
            del tmp

        # Update only non-empty fields
        if (text != None) :
            node.text = text
            debug("Wrote node text")

        if (priority != None) :
            p = Priority.Priority()
            assert(p != None)
            p.fromstring(priority)
            node.priority = p
            debug("Wrote node priority")

        if (start != None) :
            t = Time.Time()
            assert(t != None)
            t.fromstring(start)
            node.start = t
            debug("Wrote node start")

        if (end != None) :
            t = Time.Time()
            assert(t != None)
            t.fromstring(end)
            node.end = t
            debug("Wrote node end")

        debug("Wrote node values")

        # XXX FIXME: We should work recursively (for start and end ...)

        # Save database back to file
        db.save(db_file, tree)

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
