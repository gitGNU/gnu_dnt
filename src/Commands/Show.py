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
import ANSI
import DB
import Tree
import Priority
import ID
import Root
import Entry
import Terminal
import Filter
import ANSI

def show(node,
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

            id_temp = e.id
            id_absolute = str(id_temp)
            try :
                id_list     = id_temp.tolist()
                id_relative = str(id_list[len(id_list) - 1])
            except:
                id_relative = "0"

            debug("Handling colors")

            # Handle colors
            if ((filehandle.isatty()) and (colors == True)) :
                color_info  = ANSI.normal_green
                color_index = ANSI.normal_green
                p           = e.priority.value
                try :
                    color_text  = cmap[p]
                except KeyError :
                    bug("Unknown key `" + p.tostring() + "'")
            else :
                # A bunch of pass-through lambdas
                color_text  = lambda x: x
                color_index = lambda x: x
                color_info  = lambda x: x
            assert(color_index != None)
            assert(color_text  != None)
            assert(color_info  != None)

            debug("Formatting")

            # Perform format substitutions
            t = line_format
            debug("input  = `" + t + "'")
            t = re.sub('%I', color_index(id_absolute),  t)
            t = re.sub('%i', color_index(id_relative),  t)
            t = re.sub('%s', start,                     t)
            t = re.sub('%e', end,                       t)
            t = re.sub('%p', color_text(priority),      t)
            # Always substitute text at last in order to avoid re-substitutions
            # if text contains %i, %s, %e, %p, %c and so on
            t = re.sub('%t', color_text(text),          t)
            debug("output = `" + t + "'")

            if (t != '') :
                debug("Building output")

                #
                # Build the output
                #
                debug("Wrapping entry text to " + str(width))

                # Remove trailing whitespaces (newlines will be added later)
                t = t.rstrip()

                # Dump each line
                for i in t.split('\n') :
                    if (width != 0) :
                        lines = textwrap.wrap(i, width)
                    else :
                        lines = [ i ]

                    for j in lines :
                        filehandle.write(j + "\n")
            else :
                debug("Empty output, skipping ...")
    else :
        bug("Unknown type " + str(type(n)))

    # Finally handle node children
    assert(hasattr(node, "children"))
    if (len(node.children()) > 0) :
        debug("Indenting more")
        filehandle.write(indent_format)

        debug("Handling children")
        for j in node.children() :
            show(j,
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
                         name   = "show",
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
                "  %I  index (absolute)",
                "  %i  index (relative)",
                "",
                "FILTER  " + Filter.help(),
                "ID      " + ID.help(),
                "WIDTH   An integer >= 0, 0 means no formatting"
                ])

    def short_help(self) :
        return "display node(s)"

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
                           "-I", "--id",
                           action = "store",
                           type   = "string",
                           dest   = "id",
                           help   = "specify starting node")

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

        starting_id = opts.id
        if (starting_id == None) :
            starting_id = "0"
        node_id = ID.ID(starting_id)

        # Open output file
        filehandle = sys.stdout
        if (opts.output != None) :
            try :
                filehandle = open(opts.output, 'w')
            except :
                raise Exceptions.CannotWrite(opts.output)
        assert(filehandle != None)
        debug("Output file will be `" + filehandle.name + "'")

        # Handle width ...
        width = -1

        # Get width from configuration (if present)
        try :
            width = configuration.get(PROGRAM_NAME, 'width', raw = True)
        except :
            debug("No width configuration found")

        # Ovveride width with parameters (if present)
        try :
            if (opts.width != None) :
                width = int(opts.width)
        except :
            raise Exceptions.WrongParameter("width must be greater or equal "
                                            "than 0")

        # If no width available, try detecting it
        if (width < 0) :
            t     = Terminal.Terminal(stream_out = filehandle)
            width = t.columns

        assert(type(width) == int)
        assert(width >= 0)

        debug("Output width is " + str(width))

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
            indent_format   = "  "
            line_format     = "%i %t\n  (%s, %e, %p)\n"
            unindent_format = ""
        else :
            indent_format   = "  "
            line_format     = "%i %t\n"
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

        node = Tree.find(tree, node_id)
        if (node == None) :
            raise Exceptions.NodeUnavailable(str(node_id))

        #
        # Work
        #

        cmap = {
            Priority.Priority.PRIORITY_VERYHIGH : ANSI.bright_red,
            Priority.Priority.PRIORITY_HIGH     : ANSI.bright_yellow,
            Priority.Priority.PRIORITY_MEDIUM   : ANSI.bright_white,
            Priority.Priority.PRIORITY_LOW      : ANSI.normal_cyan,
            Priority.Priority.PRIORITY_VERYLOW  : ANSI.normal_blue,
            }

        #filehandle.write(indent_format)
        show(tree,
             colors, verbose,
             cmap,
             filehandle, width,
             indent_format, line_format, unindent_format,
             filter)
        #filehandle.write(unindent_format)

        # Avoid closing precious filehandles
        if ((filehandle != sys.stdout) and (filehandle != sys.stderr)) :
            debug("Closing file `" + filehandle.name + "'")
            filehandle.close()

        debug("Success")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
