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
import DB
import Entry

def description() :
    return "initialize the database"

def help() :
    print("Usage: " + PROGRAM_NAME + " init [OPTION]...")
    print("")
    print("  -f, --force    force operation")
    print("")
    print("Report bugs to <" + PACKAGE_BUGREPORT + ">")
    return 0

def do(configuration, args) :
    try :
	opts, args = getopt.getopt(args[0:],
				   "f",
				   [ "force" ])
    except getopt.GetoptError :
	raise Exceptions.UnknownParameter("")
	return 1

    force = False
    for opt, arg in opts :
	if opt in ("-f", "--force") :
	    force = True
	else :
	    raise UnknownParameter(opt)

    if (not force) :
	if (os.path.isfile(DEFAULT_DB_FILE)) :
	    raise Exceptions.WrongParameters("File `" + DEFAULT_DB_FILE + "' already present, use --force to override")
	    return 1

    # We are in force mode or the db file is not present ...
    debug("Creating db file")
    db = DB.Database()
    tree = Entry.Entry("missing text")
    db.save(DEFAULT_DB_FILE, tree)
    
    return 0

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
