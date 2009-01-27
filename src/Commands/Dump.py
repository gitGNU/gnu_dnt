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
import re

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
    def __init__(self, filehandle, width, format) :
        assert(filehandle != None)
        assert(type(width) == int)
        assert(format != None)

        Visitor.__init__(self)

        self.__filehandle = filehandle
        self.__width      = width
        self.__format     = format

    def visitEntry(self, e) :
        assert(e != None)

        if (self.__format != None) :
            text = e.text
            if (e.start != None) :
                start = e.start.tostring()
            else :
                start = "unknown"
            if (e.end != None) :
                end = e.end.tostring()
            else :
                end = "unknown"
            if (e.priority != None) :
                priority = e.priority.tostring()
            else :
                priority = "unknown"
            if (e.done()) :
                status = "complete"
            else :
                status = "incomplete"

            t = self.__format
            debug("input  = `" + t + "'")
            t = re.sub('%t', text,     t)
            t = re.sub('%s', start,    t)
            t = re.sub('%e', end,      t)
            t = re.sub('%p', priority, t)
            debug("output = `" + t + "'")

            for i in t.split('\n') :
                if (self.__width != 0) :
                    lines = textwrap.wrap(i, self.__width)
                else :
                    lines = i

                for j in lines :
                    self.__filehandle.write(j + "\n")

            self.__filehandle.write("\n")

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
            width = int(opts.width)
        assert(type(width) == int)
        if (width < 0) :
            raise Exceptions.WrongParameter("width must be greater or equale "
                                            "than 0")
        assert(width >= 0)
        debug("Width will be " + str(width))

        filehandle = sys.stdout
        if (opts.output != None) :
            try :
                filehandle = open(opts.output, 'w')
            except :
                raise Exceptions.CannotWrite(ofn)
        assert(filehandle != None)
        debug("Output file will be `" + filehandle.name + "'")

        format = "* %t\n  (%s, %e, %p)"
        if (opts.format != None) :
            format = opts.format
        assert(format != None)
        debug("Format is `" + format + "'")

        # Work

        # Load DB
        db_file = configuration.get(PROGRAM_NAME, 'database')
        assert(db_file != None)

        db   = DB.Database()
        tree = db.load(db_file)
        assert(tree != None)

        v = DumpVisitor(filehandle, width, format)
        tree.accept(v)

        # Avoid closing precious filehandles
        if ((filehandle != sys.stdout) and (filehandle != sys.stderr)) :
            debug("Closing file `" + filehandle.name + "'")
            filehandle.close()

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
