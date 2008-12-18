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
import Color
import DB
import Priority
from   Entry      import *

def description() :
    return "display node(s)"

class ShowVisitor :
    def __init__(self, colors, be_verbose) :
        self.__colors  = colors
        self.__verbose = be_verbose
        self.__indent  = ""
        self.__index   = 0
        self.__cmap    = {
            Priority.Priority.PRIORITY_VERYHIGH : red,
            Priority.Priority.PRIORITY_HIGH     : yellow,
            Priority.Priority.PRIORITY_MEDIUM   : white,
            Priority.Priority.PRIORITY_LOW      : cyan,
            Priority.Priority.PRIORITY_VERYLOW  : blue,
            }

    def visit(self, e) :
        assert(e != None)

        #debug("Visiting entry " + str(e))

        if (self.__colors) :
            color_index = green
            p           = e.priority_get()
            try :
                color_text  = self.__cmap[p]
            except KeyError :
                color_text = white
        else :
            color_index = lambda x: x # pass-through
            color_text  = lambda x: x # pass-through

        assert(color_index != None)
        assert(color_text != None)

        print(self.__indent                 +
              color_index(str(self.__index) + ".") +
              color_text(e.text))
        if (self.__verbose) :
            l    = " " * (len(str(self.__index)) + len("."))
            flag = False
            if (e.start != None) :
                print(self.__indent + l + "start = " + e.start.tostring())
                flag = True
            if (e.end != None) :
                print(self.__indent + l + "end   = " + e.end.tostring())
                flag = True
            if (flag == True) :
                print("")

        old_indent = self.__indent
        old_index  = self.__index

        self.__indent = self.__indent + "    "
        self.__index  = 0
        for j in e.children() :
            self.__index = self.__index + 1
            j.accept(self) # Re-accept myself

        self.__indent = old_indent
        self.__index  = old_index

def do(configuration, arguments) :
    command = Command("show")

    (opts, args) = command.parse_args(arguments)

    # Parameters setup

    # Work

    # Load DB
    db_file = configuration.get(PROGRAM_NAME, 'database')
    assert(db_file != None)

    db   = DB.Database()
    tree = db.load(db_file)
    assert(tree != None)

    try :
        colors = configuration.get(PROGRAM_NAME, 'colors', raw = True)
    except :
        debug("No colors related configuration, default to false")
        colors = False
    try :
        verbose = configuration.get(PROGRAM_NAME, 'verbose', raw = True)
    except :
        debug("No verboseness related configuration, default to false")
        verbose = False

    v = ShowVisitor(colors, verbose)
    tree.accept(v)

    debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
