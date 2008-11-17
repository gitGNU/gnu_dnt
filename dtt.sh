#!/usr/bin/python

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
import traceback
import getopt
import pprint

from   Trace import *
from   DB    import *
from   Debug import *
from   Entry import *

def hint(s) :
    print(s)
    print("Use `" + PROGRAM_NAME + " -h' for help")

def usage() :
    print(PROGRAM_NAME + " OPTIONS")
    print("")
    print("  -a | --add        Add node")
    print("  -r | --remove     Remove node (and its children)")
    print("  -e | --edit       Edit node")
    print("  -R | --reparent   Reparent node (and its children)")
    print("  -s | --show       Show")
    print("  -v | --verbose    Enable debug mode")
    print("  -h | --help       This help")
    print("")
    print("Report bugs to <@PACKAGE_BUGREPORT@>")

def version() :
    print(PROGRAM_NAME + " (" + PACKAGE_NAME + ") " + PACKAGE_VERSION)

DEFAULT_SOURCE_FILE = ".todo"

def do_add(args) :
    return 1

def do_remove(args) :
    return 1

def do_edit(args) :
    return 1

def do_reparent(args) :
    return 1

def do_show(args) :
    source = DEFAULT_SOURCE_FILE

    # Load DB
    db   = DB()
    tree = db.load(source)

    tree.dump("  ", "")

    return 0

def main(args) :
    # Parse command line
    try :
	opts, args = getopt.getopt(args[1:],
				   "areRsvh",
				   [ "add",
				     "remove",
				     "edit",
				     "reparent",
				     "show",
				     "help",
				     "version" ])
    except getopt.GetoptError :
	hint("Parameter(s) error")
	return 1

    do_action = do_show
    parms     = []
    for opt, arg in opts :
	if opt in ("-a", "--add") :
	    do_action = do_add ;      parms  = args[2:]
	elif opt in ("-r", "--remove") :
	    do_action = do_remove ;   parms  = args[2:]
	elif opt in ("-e", "--edit") :
	    do_action = do_edit ;     parms  = args[2:]
	elif opt in ("-r", "--reparent") :
	    do_action = do_reparent ; parms  = args[2:]
	elif opt in ("-s", "--show") :
	    do_action = do_show ;     parms  = args[2:]
	elif opt in ("-h", "--help") :
	    usage()
	    return 0
	elif opt in ("-v", "--version") :
	    version()
	    return 0
	else :
	    bug()
    if (do_action == None) :
	hint("Missing parameter(s)")
	return 1

    return do_action(parms)

if (__name__ == '__main__') :
    sys.exit(main(sys.argv))
