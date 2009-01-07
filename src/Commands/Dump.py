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

import ID

class SubCommand(Command) :
    def __init__(self) :
        Command.__init__(self, "dump")

    def short_help(self) :
        return "dump the database in a friendly format"

    def authors(self) :
        return [ "Francesco Salvestrini" ]

    def do(self, configuration, arguments) :
        Command.add_option(self,
                           "-o", "--output",
                           action = "store",
                           type   = "string",
                           dest   = "output",
                           help   = "specify output file name")
        Command.add_option(self,
                           "-p", "--pager",
                           action = "store",
                           type   = "string",
                           dest   = "pager",
                           help   = "specify pager to use")

        (opts, args) = Command.parse_args(self, arguments)

        # Parameters setup
        if (opts.output == None) :
            raise Exceptions.MissingParameters("output file name")

        pager = None
        # Prefer parameter
        if (pager == None) :
            pager = opts.pager
        # Fall-back to configuration
        if (pager == None) :
            try :
                pager = configuration.get(command.name, 'pager', raw = True)
            except :
                # No pager found on configuration
                pass
        # Fall-back to the environment
        if (pager == None) :
            pager = os.environ["PAGER"]
        # Finally bang with error
        if (pager == None) :
            raise MissingParameters("pager")

        # Work

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
