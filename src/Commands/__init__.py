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

from   Trace import *

try :
    import Add
    import Clean
    import Config
    import Done
    import NotDone
    import Edit
    import Fix
    import Init
    import Move
    import Remove
    import Show
except ImportError :
    # XXX FIXME: Add better error reporting ....
    print("Cannot import package's commands ...")
    sys.exit(-1)

commands = {
    'add'      : Add       . SubCommand(),
    'clean'    : Clean     . SubCommand(),
    'config'   : Config    . SubCommand(),
    'done'     : Done      . SubCommand(),
    'not-done' : NotDone   . SubCommand(),
    'edit'     : Edit      . SubCommand(),
    'fix'      : Fix       . SubCommand(),
    'init'     : Init      . SubCommand(),
    'move'     : Move      . SubCommand(),
    'remove'   : Remove    . SubCommand(),
    'show'     : Show      . SubCommand(),
    }

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
