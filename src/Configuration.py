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
import os
import string

from   Debug             import *
from   Trace             import *
from   Autoconfiguration import *
import Exceptions
import INI

_DB_FILE_TPL      = PROGRAM_NAME + ".db"
_CFG_FILE_TPL     = PROGRAM_NAME + ".cfg"

DEFAULT_DB_FILE   = "." + _DB_FILE_TPL
DEFAULT_CFG_FILE  = "." + _CFG_FILE_TPL

# Search paths we look into for the configuration files
CFG_SEARCH_PATHS  = [ SYSCONFDIR + '/' +       _CFG_FILE_TPL,
                      '$HOME'    + '/' + '.' + _CFG_FILE_TPL ]

class Configuration(INI.File) :
    class Error(Exception) :
        pass

    class ParsingError(Error) :
        def __init__(self, message) :
            assert(message != None)
            assert(isinstance(message, str))
            self.__message = message

        def __str__(self) :
            return self.__message

        __repr__ = __str__

    def __init__(self) :
        self.__dirty = False
        super(Configuration, self).__init__()

    def cast(self, value, datatype) :
        assert(value    != None)
        assert(datatype != None)
        if ((datatype == bool) and (isinstance(value, str))) :
            mapping = { "true"  : True,
                        "yes"   : True,
                        "y"     : True,
                        "1"     : True,
                        "false" : False,
                        "no"    : False,
                        "n"     : False,
                        "0"     : False }
            t = string.lower(value)
            if (t in mapping) :
                return mapping[t]
            else :
                raise BadValue("got while converting "  +
                               "`" + str(value) + "'"   +
                               " to "                   +
                               "boolean")
        else :
            try :
                v = datatype(value)
            except :
                raise BadValue("got while casting "     +
                               "`" + str(value) + "'"   +
                               " to "                   +
                               "`" + str(datatype) + "'")
            return v

    def set_raw(self, section, option, value) :
        assert(isinstance(section, str))
        assert(isinstance(option, str))

        super(Configuration, self).set_raw(section, option, value)
        self.__dirty = True

    def get_raw(self, section, option) :
        assert(isinstance(section, str))
        assert(isinstance(option, str))
        return super(Configuration, self).get_raw(section, option)

    def set(self, section, option, value) :
        assert(isinstance(section, str))
        assert(isinstance(option, str))

        super(Configuration, self).set_raw(section, option, value)

        self.__dirty = True

    def get(self, section, option, datatype, default = None) :
        assert(isinstance(section, str))
        assert(isinstance(option, str))
        assert(datatype != None)

        try :
            # Look for configuration data from configuration
            tmp = super(Configuration, self).get_raw(section, option)
            return self.cast(tmp, datatype)
        except :
            # ... but we cannot get configuration data ...
            if (default != None) :
                # Then use the provided default
                assert(isinstance(default, datatype))
                return self.cast(default, datatype)
            else :
                # Fallback to None if everything else fail
                tmp = None
        return tmp

    # This is a wrapper, please remove ASAP
    def read(self, filenames) :
        assert(isinstance(filenames, list))

        debug("Reading configuration from " + str(filenames))

        read_files = [ ]
        for i in filenames :
            debug("Trying `" + i + "'")
            if (os.path.isfile(i)) :
                try :
                    super(Configuration, self).load(i)
                    debug("Configuration loaded from `" + i + "'")
                    read_files.append(i)
                except Exception, e :
                    raise self.ParsingError(str(e) + " " + i)
            else :
                debug("Couldn't load configuration from `" + i + "'")

        return read_files

    def dirty_get(self) :
        return self.__dirty

    def dirty_set(self, value) :
        assert(isinstance(value, bool))
        self.__dirty = value

    dirty = property(dirty_get, dirty_set, None, None)

# Test
if (__name__ == '__main__') :
    c = Configuration()

    assert(c.dirty is False)

    try :
        c.add_section("test11")
        c.add_section("test21")
        c.add_section("test31")

        c.set("test11", "value11", 1)
        c.set("test21", "value21", True)
        c.set("test31", "value31", "string")

        assert(c.get("test11", "value11", int)  == 1)
        assert(c.get("test21", "value21", bool) == True)
        assert(c.get("test31", "value31", str)  == "string")

        c.add_section("  test12")
        c.add_section(" test22")
        c.add_section("test32")

        c.set("test12  ", "value12", 1)
        c.set(" test22 ", "value22", True)
        c.set("  test32", "value32", "string")

        assert(c.get("  test12", "value12", int)  == 1)
        assert(c.get(" test22 ", "value22", bool) == True)
        assert(c.get("test32  ", "value32", str)  == "string")

        c.add_section("test13  ")
        c.add_section(" test23 ")
        c.add_section("  test33")

        c.set("test13  ", "value13", 1)
        c.set(" test23 ", "value23", True)
        c.set("  test33", "value33", "string")

        assert(c.get("test13", "value13   ", int)  == 1)
        assert(c.get("test23", " value23  ", bool) == True)
        assert(c.get("test33", "   value33", str)  == "string")

    except :
        sys.exit(1)

    assert(c.dirty is True)

    sys.exit(0)
