#!/usr/bin/python

import os
import sys
import traceback
import getopt
import pprint
import re
from   Entry import *
from   Trace import *
from   DB    import *
from   Debug import *

def hint(s) :
    print(s)
    print("Use `" + PROGRAM_NAME + " -h' for help")

def usage() :
    print(PROGRAM_NAME + " OPTIONS")
    print("")
    print("  -v | --verbose    Enable debug mode")
    print("  -h | --help       This help")
    print("")
    print("Report bugs to <@PACKAGE_BUGREPORT@>")

def version() :
    print(PROGRAM_NAME + " (" + PACKAGE_NAME + ") " + PACKAGE_VERSION)

def main(args) :
    # Parse command line
    try :
	opts, args = getopt.getopt(args[1:],
				   "a:r:e:R:svh",
				   [ "add=",
				     "remove=",
				     "edit=",
				     "reparent=",
				     "show",
				     "help",
				     "version" ])
    except getopt.GetoptError :
	hint("Parameter(s) error")
	return 1

    action      = "show"
    source      = ".todo"
    destination = ".dtt"
    for opt, arg in opts :
	if opt in ("-a", "--add") :
	    action = "add" ;      parms  = ("")
	elif opt in ("-r", "--remove") :
	    action = "remove" ;   parms  = ("") ;
	elif opt in ("-e", "--edit") :
	    action = "edit" ;     parms  = ("")
	elif opt in ("-r", "--reparent") :
	    action = "reparent" ; parms  = ("")
	elif opt in ("-s", "--show") :
	    action = "show" ;     parms  = ("")
	elif opt in ("-h", "--help") :
	    usage()
	    return 0
	elif opt in ("-v", "--version") :
	    version()
	    return 0
	else :
	    bug()
    if (action == None) :
	hint("Missing parameter(s)")
	return 1

    # Load DB
    db   = DB()
    tree = db.load(source)

#    tree.dump(" ")

    # Save DB
    db.save(destination, tree)

if __name__ == '__main__' :
    sys.exit(main(sys.argv))
