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

import Debug
import Trace
import Color
import DB
from   Entry import *

def help() :
    print("Usage: " + PROGRAM_NAME + " show")
    print("")
    print("Report bugs to <" + PACKAGE_BUGREPORT + ">")
    return 0

class ShowVisitor :
    def __init__(self, colors, be_verbose) :
	self.__colors  = colors
	self.__verbose = be_verbose
	self.__indent  = ""
	self.__index   = 0

    def visit(self, e) :
	assert(e != None)

	#debug("Visiting entry " + str(e))

	if (self.__colors) :
	    color_index = green
	    p           = e.priority_get()
	    if (p == Entry.PRIORITY_VERYHIGH) :
		color_text = red
	    elif (p == Entry.PRIORITY_HIGH) :
		color_text = yellow
	    elif (p == Entry.PRIORITY_MEDIUM) :
		color_text = white
	    elif (p == Entry.PRIORITY_LOW) :
		color_text = cyan
	    elif (p == Entry.PRIORITY_VERYLOW) :
		color_text = blue
	    else :
		color_text = white
	else :
	    color_index = lambda x: x # pass-through
	    color_text  = lambda x: x # pass-through

	assert(color_index != None)
	assert(color_text != None)

	print(self.__indent                 +
	      color_index(str(self.__index) + ".") +
	      color_text(e.text))

	old_indent = self.__indent
	old_index  = self.__index

	self.__indent = self.__indent + "    "
	self.__index  = 0
	for j in e.children() :
	    self.__index = self.__index + 1
	    j.accept(self) # Re-accept myself

	self.__indent = old_indent
	self.__index  = old_index

def do(configuration, args) :
    # Load DB
    db   = DB.Database()
    tree = db.load(configuration['database'])

    v = ShowVisitor(configuration['colors'], configuration['verbose'])
    tree.accept(v)

    return 0

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
