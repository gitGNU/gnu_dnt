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
import datetime

from   Debug      import *
from   Trace      import *
from   Command    import *
import Exceptions
import ID
import DB
import Entry
import Tree
import Time

class SubCommand(Command) :
    def __init__(self) :
        Command.__init__(self, "done")

    def short_help(self) :
        return "mark node (and its children) as done"

    def authors(self) :
        return [ "Francesco Salvestrini" ]

    def do(self, configuration, arguments) :
        Command.add_option(self,
                           "-i", "--id",
                           action = "store",
                           type   = "string",
                           dest   = "id",
                           help   = "specify node")

        (opts, args) = Command.parse_args(self, arguments)

        # Parameters setup
        if (opts.id == None) :
            raise Exceptions.MissingParameter("node id")

        db_file   = configuration.get(PROGRAM_NAME, 'database')
        assert(db_file != None)
        id = ID.ID(opts.id)

        # Work
        debug("Marking node `" + str(id) + "' as done")

        db   = DB.Database()
        tree = db.load(db_file)
        assert(tree != None)

        node = Tree.find(tree, id)
        if (id == None) :
            raise Exceptions.NodeUnavailable(str(id))
        assert(node != None)

        node.end = Time.Time(datetime.datetime.now())

        # Save database back to file
        db.save(db_file, tree)

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
