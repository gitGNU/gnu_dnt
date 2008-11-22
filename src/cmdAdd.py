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
import getopt

from   Debug import *
import Exceptions
from   Trace import *

def help() :
    print("Usage: " + PROGRAM_NAME + " add [OPTION]...")
    print("")
    print("Options:")
    print("  -t, --text=TEXT    specify the node text")
    print("  -p, --parent=ID    specify the node parent id")
    print("")
    print("Report bugs to <" + PACKAGE_BUGREPORT + ">")
    return 0

def do(configuration, args) :
    # Parse command line
    try :
	opts, args = getopt.getopt(args[0:],
				   "p:t:",
				   [ "parent",
                                     "text" ])
    except getopt.GetoptError :
	raise Exceptions.UnknownArgument()

    node_text = ""
    parent_id = "0"
    for opt, arg in opts :
	if opt in ("-p", "--parent") :
	    parent_id = arg
        elif opt in ("-t", "--text") :
            node_text = arg
        else : 
            raise Exceptions.UnknownParameter(opt)

    debug("Adding node with:")
    debug("  node-text = " + node_text)
    debug("  parent-id = " + parent_id)

    return 0

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
