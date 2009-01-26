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
import textwrap

from   Debug      import *
from   Trace      import *
from   Command    import *
import Exceptions
import DB
import Priority
from   Visitor    import *
from   Root       import *
from   Entry      import *

class DumpVisitor(Visitor) :
    def __init__(self, filehandle, width) :
        assert(filehandle != None)
        assert(type(width) == int)
        Visitor.__init__(self)
        self.__filehandle = filehandle
        self.__width      = width

    def visitEntry(self, e) :
        assert(e != None)

        text = e.text
        lines = textwrap.wrap(text, self.__width)
        i     = 0
        for line in lines :
            if (i == 0) :
                self.__filehandle.write("- " + line + "\n")
            else :
                self.__filehandle.write("  " + line + "\n")
                i = i + 1

        if (e.done()) :
            t = "complete"
        else :
            t = "incomplete"

        text = "(" + \
            "added "     + str(e.start) + ", " + \
            t + ", " + \
            "priority " + e.priority.tostring() + ")\n" + \
            "\n"
        lines = textwrap.wrap(text, self.__width)
        for line in lines :
            self.__filehandle.write("  " + line + "\n")

        self.__filehandle.write("\n")

#	 self.__filehandle.write("- ")
#        self.__filehandle.write(e.text + "\n")
#        self.__filehandle.write("  (" +
#                                "added "     + str(e.start) + ", " +
#                                t + ", " +
#                                "priority " + e.priority.tostring() + ")\n")
#        self.__filehandle.write("\n")

    def visitRoot(self, r) :
        assert(r != None)

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
                           "-f", "--format",
                           action = "store",
                           type   = "string",
                           dest   = "format",
                           help   = "specify dump format")
        Command.add_option(self,
                           "-w", "--width",
                           action = "store",
                           type   = "string",
                           dest   = "width",
                           help   = "specify maximum text width")

        (opts, args) = Command.parse_args(self, arguments)

        # Parameters setup
        width = 70
        if (opts.width != None) :
            width = opts.width
        if (width <= 0) :
            raise Exceptions.WrongParameter("width must be greater than 0")
        assert(width > 0)

        ofh = sys.stdout
        if (opts.output != None) :
            ofn = opts.output
            debug("Output file will be `" + ofn + "'")
            try :
                ofh = open(ofn, 'w')
            except :
                raise Exceptions.CannotWrite(ofn)
        assert(ofh != None)

        # Work

        # Load DB
        db_file = configuration.get(PROGRAM_NAME, 'database')
        assert(db_file != None)

        db   = DB.Database()
        tree = db.load(db_file)
        assert(tree != None)

        v = DumpVisitor(ofh, width)
        tree.accept(v)

        ofh.close()

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
