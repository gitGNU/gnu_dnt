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
import Root
import Entry
import Terminal
import Filter
import Color

#class DumpVisitor(Visitor):
#
#    def __init__(self, colors, verbose, filehandle, width,
#                 indent_format, line_format, unindent_format,
#                 filter) :
#        assert(filehandle != None)
#        assert(type(width) == int)
#
#        assert(indent_format   != None)
#        assert(line_format     != None)
#        assert(unindent_format != None)
#
#        assert(filter != None)
#
#        super(DumpVisitor, self).__init__()
#
#        self.__filehandle      = filehandle
#        self.__width           = width
#        self.__colors          = colors
#        self.__verbose         = verbose
#        self.__indent_format   = indent_format
#        self.__line_format     = line_format
#        self.__unindent_format = unindent_format
#        self.__filter          = filter.function
#        self.__cmap            = {
#            Priority.Priority.PRIORITY_VERYHIGH : bright_red,
#            Priority.Priority.PRIORITY_HIGH     : bright_yellow,
#            Priority.Priority.PRIORITY_MEDIUM   : bright_white,
#            Priority.Priority.PRIORITY_LOW      : normal_cyan,
#            Priority.Priority.PRIORITY_VERYLOW  : normal_blue,
#            }
#
#    def visitEntry(self, e) :
#        assert(e != None)
#
#        if (not self.__filter(e)) :
#            debug("Entry "                 +
#                  "`" + str(e) + "' "      +
#                  "does not match filter " +
#                  "`" + str(self.__filter) + "'")
#            return
#
#        debug("Visiting entry " + str(e))
#
#        if (self.__indent_format != None) :
#            if (self.level_previous() < self.level_current()) :
#                n = self.level_current() - self.level_previous()
#                assert(n > 0)
#                debug("Indenting " + str(n) + " times")
#                for i in range(0, n) :
#                    self.__filehandle.write(self.__indent_format)
#
#        debug("Formatting")
#        if (self.__line_format != None) :
#            text = e.text
#            if (e.start != None) :
#                start = e.start.tostring()
#            else :
#                start = "unknown"
#            if (e.end != None) :
#                end = e.end.tostring()
#            else :
#                end = "unknown"
#            if (e.priority != None) :
#                priority = e.priority.tostring()
#            else :
#                priority = "unknown"
#            if (e.done()) :
#                status = "complete"
#            else :
#                status = "incomplete"
#
#            debug("Handling colors")
#
#            # Handle colors
#            if (self.__colors == True) :
#                color_info  = normal_green
#                color_index = normal_green
#                p           = e.priority.value
#                try :
#                    color_text  = self.__cmap[p]
#                except KeyError :
#                    bug("Unknown key `" + p.tostring() + "'")
#                    color_text = white
#            else :
#                # A bunch of pass-through lambdas
#                color_index = lambda x: x
#                color_text  = lambda x: x
#                color_info  = lambda x: x
#            assert(color_index != None)
#            assert(color_text  != None)
#            assert(color_info  != None)
#
#            debug("Formatting")
#
#            # Perform format substitutions
#            t = self.__line_format
#            debug("input  = `" + t + "'")
#            t = re.sub('%t', color_text(text),     t)
#            t = re.sub('%s', start,                t)
#            t = re.sub('%e', end,                  t)
#            t = re.sub('%p', color_text(priority), t)
#            debug("output = `" + t + "'")
#
#            debug("Building output")
#
#            # Build the output
#            debug("Wrapping entry text to " + str(self.__width))
#            for i in t.split('\n') :
#                if (self.__width != 0) :
#                    lines = textwrap.wrap(i, self.__width)
#                else :
#                    lines = [ i ]
#
#                for j in lines :
#                    self.__filehandle.write(j + "\n")
#
#        if (self.__unindent_format != None) :
#            if (self.level_current() < self.level_previous()) :
#                n = self.level_previous() - self.level_current()
#                assert(n > 0)
#                debug("Unindenting " + str(n) + " times")
#                for i in range(0, n) :
#                    self.__filehandle.write(self.__unindent_format)
#
#        debug("Completed entry")
#
#    def visitRoot(self, r) :
#        assert(r != None)

def dump(node,
         colors, verbose,
         cmap,
         filehandle, width,
         indent_format, line_format, unindent_format,
         filter) :

    assert(node            != None)
    assert(type(colors)    == bool)
    assert(type(verbose)   == bool)
    assert(filehandle      != None)
    assert(width           >= 0)
    assert(indent_format   != None)
    assert(line_format     != None)
    assert(unindent_format != None)
    assert(filter          != None)

    # Dump the current node
    if (type(node) == Root.Root) :
        pass
    elif (type(node) == Entry.Entry) :
        e = node

        if (filter.function(e) == False) :
            debug("Entry "                 +
                  "`" + str(e) + "' "      +
                  "does not match filter " +
                  "`" + str(filter) + "'")
        else :
            debug("Visiting entry " + str(e))

            debug("Formatting")

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

            debug("Handling colors")

            # Handle colors
            if (colors == True) :
                color_info  = Color.normal_green
                color_index = Color.normal_green
                p           = e.priority.value
                try :
                    color_text  = cmap[p]
                except KeyError :
                    bug("Unknown key `" + p.tostring() + "'")
            else :
                # A bunch of pass-through lambdas
                color_index = lambda x: x
                color_text  = lambda x: x
                color_info  = lambda x: x
            assert(color_index != None)
            assert(color_text  != None)
            assert(color_info  != None)

            debug("Formatting")

            # Perform format substitutions
            t = line_format
            debug("input  = `" + t + "'")
            t = re.sub('%t', color_text(text),     t)
            t = re.sub('%s', start,                t)
            t = re.sub('%e', end,                  t)
            t = re.sub('%p', color_text(priority), t)
            debug("output = `" + t + "'")

            debug("Building output")

            # Build the output
            debug("Wrapping entry text to " + str(width))
            for i in t.split('\n') :
                if (width != 0) :
                    lines = textwrap.wrap(i, width)
                else :
                    lines = [ i ]

                for j in lines :
                    filehandle.write(j + "\n")
    else :
        bug("Unknown type " + str(type(n)))
        
    # Finally handle node children
    assert(hasattr(node, "children"))
    if (len(node.children()) > 0) :
        debug("Indenting more")
        filehandle.write(indent_format)

        debug("Handling children")
        for j in node.children() :
            dump(j,
                 colors, verbose,
                 cmap,
                 filehandle, width,
                 indent_format, line_format, unindent_format,
                 filter)

        debug("Indenting less")
        filehandle.write(unindent_format)
    else :
        debug("No children to handle")

class SubCommand(Command) :
    def __init__(self) :
        Command.__init__(self,
                         name   = "dump",
                         footer = [
                "INDENT_FORMAT and UNINDENT_FORMAT are applied " + \
                    "when indentation is needed",
                "FORMAT  controls the output for each entry " + \
                    "dumped. Interpreted sequences are:",
                "",
                "  %t  text",
                "  %s  start time",
                "  %e  end time",
                "  %p  priority",
                "",
                "WIDTH   An integer >= 0, 0 means no text wrapping",
                "FILTER  " + Filter.help()
                ])

    def short_help(self) :
        return "dump the database in a friendly format"

    def authors(self) :
        return [ "Francesco Salvestrini" ]

    def do(self, configuration, arguments) :
        #
        # Parameters setup
        #
        Command.add_option(self,
                           "-o", "--output",
                           action = "store",
                           type   = "string",
                           dest   = "output",
                           help   = "specify output file name")
        Command.add_option(self,
                           "-l", "--line-format",
                           action = "store",
                           type   = "string",
                           dest   = "line_format",
                           help   = "specify line dump format")
        Command.add_option(self,
                           "-i", "--indent-format",
                           action = "store",
                           type   = "string",
                           dest   = "indent_format",
                           help   = "specify indent line dump format")
        Command.add_option(self,
                           "-u", "--unindent-format",
                           action = "store",
                           type   = "string",
                           dest   = "unindent_format",
                           help   = "specify line dump format")
        Command.add_option(self,
                           "-w", "--width",
                           action = "store",
                           type   = "string",
                           dest   = "width",
                           help   = "specify maximum text width")
        Command.add_option(self,
                           "-F", "--filter",
                           action = "store",
                           type   = "string",
                           dest   = "filter",
                           help   = "specify selection filter")

        (opts, args) = Command.parse_args(self, arguments)
        if (len(args) > 0) :
            raise Exceptions.UnknownParameter(args[0])

        try :
            width = configuration.get(PROGRAM_NAME, 'width', raw = True)
        except :
            t     = Terminal.Terminal()
            width = t.columns
            debug("No width related configuration, default to " +
                  str(width))
        assert(width != None)

        if (opts.width != None) :
            width = int(opts.width)
        assert(type(width) == int)
        if (width < 0) :
            raise Exceptions.WrongParameter("width must be greater or equal "
                                            "than 0")
        assert(width >= 0)

        filehandle = sys.stdout
        if (opts.output != None) :
            try :
                filehandle = open(opts.output, 'w')
            except :
                raise Exceptions.CannotWrite(ofn)
        assert(filehandle != None)
        debug("Output file will be `" + filehandle.name + "'")

        try :
            colors = configuration.get(PROGRAM_NAME, 'colors', raw = True)
        except :
            colors = False
            debug("No colors related configuration, default to " +
                  str(colors))
        assert(colors != None)

        try :
            verbose = configuration.get(PROGRAM_NAME, 'verbose', raw = True)
        except :
            verbose = False
            debug("No verboseness related configuration, default to " +
                  str(verbose))
        assert(verbose != None)

        #
        # NOTE:
        #     verbose has no meaning when the user specifies its own
        #     formatting tules. We will use a different format for quiet and
        #     verbose mode however ...
        #
        if (verbose == True) :
            indent_format   = ""
            line_format     = "* %t\n  (%s, %e, %p)\n"
            unindent_format = ""
        else :
            indent_format   = ""
            line_format     = "* %t\n"
            unindent_format = ""

        if (opts.indent_format != None) :
            indent_format = opts.indent_format
        assert(indent_format != None)
        debug("Indent-format is:   `" + indent_format + "'")

        if (opts.line_format != None) :
            line_format = opts.line_format
        assert(line_format != None)
        debug("Line-format is:     `" + line_format + "'")

        if (opts.unindent_format != None) :
            unindent_format = opts.unindent_format
        assert(unindent_format != None)
        debug("Unindent-format is: `" + unindent_format + "'")

        # Build the filter
        filter_text = "all"
        if (opts.filter != None) :
            filter_text = opts.filter
        filter = Filter.Filter(filter_text)
        assert(filter != None)

        #
        # Load database from file
        #
        db_file = configuration.get(PROGRAM_NAME, 'database')
        assert(db_file != None)
        db      = DB.Database()
        tree    = db.load(db_file)
        assert(tree != None)

        #
        # Work
        #

        #v = DumpVisitor(colors, verbose, filehandle, width,
        #                indent_format, line_format, unindent_format,
        #                filter)
        #tree.accept(v)

        cmap = {
            Priority.Priority.PRIORITY_VERYHIGH : Color.bright_red,
            Priority.Priority.PRIORITY_HIGH     : Color.bright_yellow,
            Priority.Priority.PRIORITY_MEDIUM   : Color.bright_white,
            Priority.Priority.PRIORITY_LOW      : Color.normal_cyan,
            Priority.Priority.PRIORITY_VERYLOW  : Color.normal_blue,
            }

        filehandle.write(indent_format)
        dump(tree,
             colors, verbose,
             cmap,
             filehandle, width,
             indent_format, line_format, unindent_format,
             filter)
        filehandle.write(unindent_format)

        # Avoid closing precious filehandles
        if ((filehandle != sys.stdout) and (filehandle != sys.stderr)) :
            debug("Closing file `" + filehandle.name + "'")
            filehandle.close()

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
