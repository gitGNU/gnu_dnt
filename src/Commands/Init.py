#
# Copyright (C) 2008, 2009 Francesco Salvestrini
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
import os

from   Debug         import *
from   Trace         import *
from   Command       import *
import Exceptions
import DB
import Root

class SubCommand(Command) :
    def __init__(self) :
        Command.__init__(self,
                         name   = "init",
                         footer = [])

    def short_help(self) :
        return "initialize the database"

    def authors(self) :
        return [ "Francesco Salvestrini" ]

    def do(self, configuration, arguments) :
        #
        # Parameters setup
        #
        Command.add_option(self,
                           "-f", "--force",
                           action = "store_true",
                           dest   = "force",
                           help   = "force operation")
        Command.add_option(self,
                           "-n", "--name",
                           action = "store",
                           dest   = "name",
                           help   = "specify root node name")

        (opts, args) = Command.parse_args(self, arguments)
        if (len(args) > 0) :
            raise Exceptions.UnknownParameter(args[0])

        if (opts.name != None) :
            name = opts.name
        else :
            cfg_name = configuration.get(self.name,
                                         'name',
                                         str,
                                         "Nameless "  +
                                         PROGRAM_NAME +
                                         " database")
            name = str(cfg_name)

        db_file = configuration.get(PROGRAM_NAME, 'database', str)
        assert(db_file != None)

        if (opts.force is not True) :
            debug("Force mode disabled")
            assert(db_file != None)
            if (os.path.isfile(db_file)) :
                raise Exceptions.ForceNeeded("database file "
                                             "`" + db_file + "' "
                                             "already exists")

        #
        # Work
        #

        # We are in force mode (which means we must write the DB whatsover)
        # or the DB file is not present at all ...

        db = DB.Database()

        # Create an empty tree
        tree = Root.Root(name)
        assert(tree != None)

        #
        # Save database back to file
        #
        db.save(db_file, tree)

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
