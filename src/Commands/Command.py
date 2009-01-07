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
from   optparse   import OptionParser, IndentedHelpFormatter
import textwrap

from   Trace      import *
from   Debug      import *
import Exceptions

class Command(OptionParser) :
    # NOTE: An empty string is an allowed name (main uses it)
    def __init__(self, name, format = "[OPTION]...", footer = "") :
        assert(name != None)
        assert(type(name) == str)
        assert(format != None)
        assert(type(format) == str)
        assert(footer != None)
        assert(type(footer) == str)

        self.__name   = name
        self.__footer = footer

        # XXX FIXME: This is really awful ...
        if (self.__name == "") :
            usage_format   = "Usage: %prog " + format
            version_format = "%prog " + \
                "(" + PACKAGE_NAME + " " + PACKAGE_VERSION + ")"
        else :
            usage_format   = "Usage: %prog " + self.__name + " " + format
            version_format = "%prog " + self.__name + " " + \
                "(" + PACKAGE_NAME + " " + PACKAGE_VERSION + ")"

        OptionParser.__init__(self,
                              prog    = PROGRAM_NAME,
                              usage   = usage_format,
                              version = version_format,
                              #epilog  = footer
                              )
        OptionParser.disable_interspersed_args(self)

    # Override OptParse print_version() method
    def print_version(self, file = None) :
        OptionParser.print_version(self, file)

        assert(hasattr(self, "authors"))
        assert(callable(self.authors))
        assert(type(self.authors()) == list)

        print >> file, ""
        j = 0
        for i in self.authors() :
            if (j == 0) :
                header = "Copyright (C) 2008 "
            else :
                header = "                   "
            print >> file, header + i
            j = j + 1
        print >> file, ""

        print >> file, "This is free software.  You may redistribute copies of it under the terms of"
        print >> file, "the GNU General Public License <http://www.gnu.org/licenses/gpl.html>."
        print >> file, "There is NO WARRANTY, to the extent permitted by law."


    def name_get(self) :
        return self.__name
    def name_set(self, n) :
        assert(type(n) == str)
        assert(n != "")
        assert(n != None)
        assert(n == string.rstrip(string.lstrip(n)))

        self.__name = n

    name = property(name_get, name_set)

    # Override OptParse print_help() method
    def print_help(self, file = None) :
        # Force output to stdout
        OptionParser.print_help(self, sys.stdout)
        sys.stdout.write("\n")
        if (self.__footer != "") :
            sys.stdout.write(self.__footer)
            sys.stdout.write("\n")
        sys.stdout.write("Report bugs to <" + PACKAGE_BUGREPORT + ">\n")

    # Override OptParse error() method
    def error(self, msg) :
        raise EParameters(msg)

    def exit(self, status = 0, msg = None):
        debug("Explicit exit called from command")
        try :
            OptionParser.exit(self, status, msg)
        except SystemExit, e:
            # Wrapping SistemExit exception with our own exception
            raise Exceptions.ExplicitExit(e, e.code)
        except :
            bug("Unhandled exception in option parser")

    ## This method should be provided by the subclass
    #def description(self) :
    #    bug()

    ## This method must be provided by the subclass
    #def authors(self) :
    #    bug()

    ## This method should be provided by the subclass
    #def do(self, configuration, arguments) :
    #    bug()

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
