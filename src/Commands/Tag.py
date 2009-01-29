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
import DB

class SubCommand(Command) :
    def __init__(self) :
        Command.__init__(self, "tag")

    def short_help(self) :
        return "tag node(s)"

    def authors(self) :
        return [ "Francesco Salvestrini" ]

    def do(self, configuration, arguments) :
        Command.add_option(self,
                           "-i", "--id",
                           action = "store",
                           type   = "string",
                           dest   = "id",
                           help   = "specify node id")
        Command.add_option(self,
                           "-a", "--add",
                           action = "store",
                           type   = "string",
                           dest   = "add",
                           help   = "add a tag")
        Command.add_option(self,
                           "-r", "--remove",
                           action = "store",
                           type   = "string",
                           dest   = "remove",
                           help   = "remove a tag")

        (opts, args) = Command.parse_args(self, arguments)

        # Parameters setup
        if ((opts.add == None) and (opts.remove == None)) :
            raise Exceptions.MissingParameter("Missing operation")
        if ((opts.add != None) and (opts.remove != None)) :
            raise Exceptions.TooManyParameters()
        if (opts.add != None) :
            tag = opts.add
        elif (opts.remove != None) :
            tag = opts.remove
        else :
            raise Exceptions.MissingParameter("Missing tag name")

        # Work
        db   = DB.Database()
        tree = db.load(db_file)
        assert(tree != None)

        node = Tree.find(tree, id)
        if (id == None) :
            raise Exceptions.NodeUnavailable(str(id))
        assert(node != None)

        if (opts.add != None) :
            debug("Tagging node `" + str(id) + "'")
            node.tag(tag)
        elif (opts.remove != None) :
            debug("De-tagging node `" + str(id) + "'")
            node.untag(tag)
        else :
            bug()

        # Save database back to file
        db.save(db_file, tree)

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
