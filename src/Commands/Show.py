#
# Copyright (C) 2008, 2009 Francesco Salvestrini
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
import Enum

def show(level,
         node,
         colors, verbose,
         cmap,
         filehandle, width,
         indent_fill, line_format, unindent_fill, level_fill,
         hide_collapsed) :

    assert(node          != None)
    assert(isinstance(colors, bool))
    assert(isinstance(verbose, bool))
    assert(filehandle    != None)
    assert(width         >= 0)
    assert(indent_fill   != None)
    assert(line_format   != None)
    assert(unindent_fill != None)
    assert(level_fill    != None)

    # Dump the current node
    if (isinstance(node, Root.Root)) :
        pass
    elif (isinstance(node, Entry.Entry)) :
        e = node

        if not (('visible' in e.flags)   or
                ('collapsed' in e.flags)) :
            debug("Entry "                 +
                  "`" + str(e) + "' "      +
                  "does not match any flag")
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

            #
            # NOTE: 'done' get not substituted, yet ...
            #
            #if (e.done) :
            #    status = "complete"
            #else :
            #    status = "incomplete"

            if (e.comment != None) :
                comment = e.comment
            else :
                comment = ""

            depth = str(e.depth)

            id_temp = e.id
            id_absolute = str(id_temp)
            # Remove leading '0.' (we don't print anything related
            # to the Root node)
            id_absolute = re.sub('^0\.', '', id_absolute)

            try :
                id_list     = id_temp.tolist()
                id_relative = str(id_list[len(id_list) - 1])
            except:
                id_relative = "0"

            debug("Handling colors")

            # Handle colors
            if ((filehandle.isatty()) and (colors is True)) :
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
            t = re.sub('%c', comment,                   t)
            t = re.sub('%d', depth,                     t)
            # Always substitute text at last in order to avoid re-substitutions
            # if text contains %i, %s, %e, %p, %c and so on
            #
            # If line is set as "collapsed", substitute text with "..."
            if ('collapsed' in e.flags) :
                # XXX FIXME: Awful hack
                if (hide_collapsed) :
                    t = ''
                else :
                    t = re.sub('%t', color_text('...'), t)
            else :
                t = re.sub('%t', color_text(text),  t)

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

                dump = [ ]
                for i in t.split('\n') :
                    if (width != 0) :
                        w = width - (len(level_fill) * level)

                        if (w <= 0) :
                            dump = [ ]
                            raise Exceptions.WidthTooSmall(i)

                        dump.extend(ANSI.ansi_textwrap(t, w))
                    else :
                        dump.append(i)

                for j in dump :
                    filehandle.write(level_fill * level + j + "\n")
            else :
                debug("Empty output, skipping ...")
    else :
        bug("Unknown type " + str(type(node)))

    # Finally handle node children
    assert(hasattr(node, "children"))
    if ((len(node.children) > 0)      and
        (('visible' in node.flags)    or
         ('collapsed' in node.flags))) :
        debug("Indenting more")
        filehandle.write(indent_fill)

        debug("Handling children")
        for j in node.children :
            show(level + 1,
                 j,
                 colors, verbose,
                 cmap,
                 filehandle, width,
                 indent_fill, line_format,
                 unindent_fill, level_fill,
                 hide_collapsed)

        debug("Indenting less")
        filehandle.write(unindent_fill)
    else :
        debug("No children to handle")

def mark(node, filter) :
    assert(node != None)
    assert(filter != None)

    marked = 0
    node.flags = []

    if (len(node.children) > 0) :
        debug("Marking " + str(len(node.children)) + " children")

        for i in node.children :
            m       = 0
            node, m = mark(i, filter)
            marked  = marked + m

        node = node.parent_get()

    if (marked > 0) :
        debug("Entry `" +  str(node)   +
              "' has "  +  str(marked) +
              " children that match filter")

    if (isinstance(node, Root.Root)) :
        if (marked > 0) :
            debug("Entry `"                               + str(node)   +
                  "' has children those matches filter `" + str(filter) +
                  "' marking it as collapsed")
            node.flags = ['collapsed']

    elif (isinstance(node, Entry.Entry)) :
        match = filter.evaluate(node)

        if ((marked > 0) and (match is False)) :
            debug("Entry `"                               + str(node)   +
                  "' has children those matches filter `" + str(filter) +
                  "' marking it as collapsed")
            node.flags = ['collapsed']

        if (match is True) :
            debug("Entry `"            +  str(node)  +
                  "' matches filter `" + str(filter) +
                  "', marking it as visible")
            node.flags = ['visible']
            marked = marked + 1

    else :
        bug("Unknown type " + str(type(node)))

    return node, marked

class SubCommand(Command) :
    def __init__(self) :
        Command.__init__(self,
                         name   = "show",
                         footer = [
                "INDENT_FILL and UNINDENT_FILL are applied " + \
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
                "  %c  comment",
                "  %d  depth",
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
                           "-i", "--id",
                           action = "store",
                           type   = "string",
                           dest   = "id",
                           help   = "specify starting node")

        Command.add_option(self,
                           "-l", "--line-format",
                           action = "store",
                           type   = "string",
                           dest   = "line_format",
                           help   = "specify line format")
        Command.add_option(self,
                           "-I", "--indent-fill",
                           action = "store",
                           type   = "string",
                           dest   = "indent_fill",
                           help   = "specify indent fill string")
        Command.add_option(self,
                           "-U", "--unindent-fill",
                           action = "store",
                           type   = "string",
                           dest   = "unindent_fill",
                           help   = "specify unindent fill string")
        Command.add_option(self,
                           "-L", "--level-fill",
                           action = "store",
                           type   = "string",
                           dest   = "level_fill",
                           help   = "specify level fill string")

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
        Command.add_option(self,
                           "-H", "--hide-collapsed",
                           action = "store_true",
                           dest   = "hide",
                           help   = "hide collapsed entries")

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

        # Override width with parameters (if present)
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

        assert(isinstance(width, int))
        assert(width >= 0)

        debug("Output width is " + str(width))

        # Handle hide-collapsed
        hide_collapsed = None

        # Get hide-collapsed from configuration (if present)
        try :
            hide_collapsed = configuration.get(PROGRAM_NAME,
                                               'hide-collapsed',
                                               raw = True)
        except :
            debug("No hide-collapsed configuration found")

        # Override hide-collapsed with parameters (if present)
        try :
            if (opts.hide != None) :
                hide_collapsed = bool(opts.hide)
        except :
            raise Exceptions.WrongParameter("hide-collapsed must be boolean")


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
        if (verbose is True) :
            indent_fill   = ""
            line_format     = "%i %t\n  [%c]\n  (%s, %e, %p)\n"
            unindent_fill = ""
            level_fill    = "    "
        else :
            indent_fill   = ""
            line_format     = "%i %t\n"
            unindent_fill = ""
            level_fill    = "    "

        if (opts.indent_fill != None) :
            indent_fill = opts.indent_fill
        assert(indent_fill != None)
        debug("Indent-fill is:   `" + indent_fill + "'")

        if (opts.line_format != None) :
            line_format = opts.line_format
        assert(line_format != None)
        debug("Line-format is:     `" + line_format + "'")

        if (opts.unindent_fill != None) :
            unindent_fill = opts.unindent_fill
        assert(unindent_fill != None)
        debug("Unindent-fill is: `" + unindent_fill + "'")

        if (opts.level_fill != None) :
            level_fill = opts.level_fill

        assert(level_fill != None)
        debug("Level-fill is: `" + level_fill + "'")

        # Build the filter
        filter_text = "not done"
        if (opts.filter != None) :
            filter_text = opts.filter
        filter_obj = Filter.Filter(filter_text)
        assert(filter_obj != None)

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
            Priority.PRIORITY_VERYHIGH : ANSI.bright_red,
            Priority.PRIORITY_HIGH     : ANSI.bright_yellow,
            Priority.PRIORITY_MEDIUM   : ANSI.bright_white,
            Priority.PRIORITY_LOW      : ANSI.normal_cyan,
            Priority.PRIORITY_VERYLOW  : ANSI.normal_blue,
            }

        # Marking nodes that match filters
        m = 0
        node, m = mark(node, filter_obj)
        debug("Found " + str(m) + " entries matching filters")

        #filehandle.write(indent_fill)
        show(0,
             node,
             colors, verbose,
             cmap,
             filehandle, width,
             indent_fill, line_format, unindent_fill, level_fill,
             hide_collapsed)
        #filehandle.write(unindent_fill)

        # Avoid closing precious filehandles
        if ((filehandle != sys.stdout) and (filehandle != sys.stderr)) :
            debug("Closing file `" + filehandle.name + "'")
            filehandle.close()

        debug("Success")


# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
