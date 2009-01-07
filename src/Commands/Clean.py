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

from   Debug            import *
from   Trace            import *
from   Commands.Command import *
import Exceptions

class SubCommand(Command) :
    def __init__(self) :
        Command.__init__(self, "clean")

    def short_help(self) :
        return "remove the database"

    def authors(self) :
        return [ "Francesco Salvestrini" ]

    def do(self, configuration, arguments) :
        (opts, args) = Command.parse_args(self, arguments)

        # Parameters setup
        db_file = configuration.get(PROGRAM_NAME, 'database')
        assert(db_file != None)

        # Work
        try :
            os.stat(db_file)
        except OSError, e:
            warning("Nothing to do, directory already clean")
            return
        except :
            bug()

        try :
            os.unlink(db_file)
        except IOError, e:
            raise Exceptions.EOS("Cannot remove `" + db_file + "'")
        except :
            bug()

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
