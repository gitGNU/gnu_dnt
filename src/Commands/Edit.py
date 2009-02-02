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
import ID

class SubCommand(Command) :
    def __init__(self) :
        Command.__init__(self, "edit")

    def short_help(self) :
        return "edit a node"

    def authors(self) :
        return [ "Francesco Salvestrini" ]

    def do(self, configuration, arguments) :
        Command.add_option(self,
                           "-i", "--id",
                           action = "store",
                           type   = "string",
                           dest   = "id",
                           help   = "specify node id to edit")
        Command.add_option(self,
                           "-e", "--editor",
                           action = "store",
                           type   = "string",
                           dest   = "editor",
                           help   = "specify editor to use")

        (opts, args) = Command.parse_args(self, arguments)

        # Parameters setup
        if (opts.id == None) :
            raise Exceptions.MissingParameters("node id")

        editor = None
        # Prefer parameter
        if (editor == None) :
            editor = opts.editor
        # Fall-back to configuration
        if (editor == None) :
            try :
                editor = configuration.get(Command.name,
                                           'editor',
                                           raw = True)
            except :
                # No editor found on configuration
                pass
        # Fall-back to the environment
        if (editor == None) :
            editor = os.environ["EDITOR"]
        # Finally bang with error
        if (editor == None) :
            raise MissingParameters("editor")
        debug("Editor will be `" + editor + "'")

        # Work
        id = ID.ID(opts.id)

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
