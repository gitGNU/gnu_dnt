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

import sys  # Useless

from   Debug import *
from   Trace import *

def help() :
    pass

def do(configuration, args) :
    print("Usage: " + PROGRAM_NAME + " [FLAG]... [COMMAND]")
    print("")
    print("Flags:")
    print("       --colors            use colors")
    print("       --no-colors         do not use colors")
    print("       --no-configs        do not use config files")
    print("       --database=FILE     change the database from the default "
          "(" + DEFAULT_DB_FILE + ")")
    print("                           to the filename specified")
    print("       --verbose           display verbosely when showing, report verbosely")
    print("                           during other commands")
    print("       --debug             enable debug mode")
    print("")
    print("Commands:")
    print("  -a | --add               add a new node")
    print("  -e | --edit              edit a node")
    print("  -m | --move              reparent nodes")
    print("  -r | --remove            remove a node (and its children)")
    print("  -s | --show              display nodes")
    print("  -V | --version           print version number")
    print("  -h | --help              print this help")
    print("")
    print("See `" + PROGRAM_NAME + " --help COMMAND' for more information about a specific command.")
    print("The programs looks for configuration files in the following order:")
    print("")
    for i in CFG_SEARCH_PATHS :
        # Do not use os.path.expandvars() here, we must preserve the vars name
        print("  " + i)
    print("")
    print("Report bugs to <@PACKAGE_BUGREPORT@>")

    return 0

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
