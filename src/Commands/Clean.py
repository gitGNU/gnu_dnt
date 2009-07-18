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

from   Debug      import *
from   Trace      import *
from   Command    import *
import Exceptions

class SubCommand(Command) :
    def __init__(self) :
        Command.__init__(self,
                         name   = "clean",
                         footer = [])

    def short_help(self) :
        return "remove the database"

    def authors(self) :
        return [ "Francesco Salvestrini" ]

    def do(self, configuration, arguments) :
        #
        # Parameters setup
        #
        (opts, args) = Command.parse_args(self, arguments)
        if (len(args) > 0) :
            raise Exceptions.UnknownParameter(args[0])

        db_file = configuration.get(PROGRAM_NAME, 'database')
        assert(db_file != None)

        #
        # Work
        #
        try :
            os.stat(db_file)
        except OSError :
            warning("Nothing to do, directory already clean")
            return
        except :
            bug("Unhandled exception calling os.stat() on db")

        try :
            os.unlink(db_file)
        except IOError :
            raise Exceptions.CannotRemove(db_file)
        except :
            bug("Unhandled exception unlinking db file `" + db_file + "'")

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
