# -*- python -*-

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

class Configuration(object) :
    def __init__(self) :
        self.__dirty    = False
        self.__ini      = INI.File()

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
                raise Exceptions.BadValue("got while converting "  +
                                          "`" + str(value) + "'"   +
                                          " to "                   +
                                          "boolean")
        else :
            try :
                v = datatype(value)
            except :
                raise Exceptions.BadValue("got while casting "     +
                                          "`" + str(value) + "'"   +
                                          " to "                   +
                                          "`" + str(datatype) + "'")
            return v

    def add_section(self, section) :
        self.__ini.add_section(section)

    def remove_section(self, section) :
        self.__ini.remove_section(section)

    def sections(self) :
        return self.__ini.sections()

    def has_section(self, section) :
        return self.__ini.has_section(section)

    def options(self, section) :
        return self.__ini.options(section)

    def has_option(self, section, option) :
        return self.__ini.has_option(section, option)

    def set(self, section, option, value) :
        assert(isinstance(section, str))
        assert(isinstance(option, str))

        #if (not self.__ini.has_section(section)) :
        #    raise Exceptions.UnknownSection(section)

        self.__ini.set_option(section, option, value)
        self.__dirty = True

    def get(self, section, option, datatype, default = None) :
        assert(isinstance(section, str))
        assert(isinstance(option, str))
        assert(datatype != None)

        #if (not self.__ini.has_section(section)) :
        #    raise Exceptions.UnknownSection(section)

        try :
            # Look for configuration data from configuration
            tmp = self.__ini.get_option(section, option)
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

    def save(self, filename) :
        assert(filename != None)
        assert(isinstance(filename, str))
        if (self.__dirty is not True) :
            debug("Configuration is not dirty, there is no need to save it")
            return
        self.__ini.save(filename)
        debug("Configuration saved to `" + filename + "'")

    def load(self, filename) :
        assert(filename != None)
        assert(isinstance(filename, str))
        self.__ini.load(filename)
        self.__dirty = False
        debug("Configuration loaded from `" + filename + "'")

    def __dirty_get(self) :
        return self.__dirty

    def __dirty_set(self, value) :
        assert(isinstance(value, bool))
        self.__dirty = value

    dirty = property(__dirty_get, __dirty_set, None, None)

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
        assert(c.get("test21", "value21", bool) is True)
        assert(c.get("test31", "value31", str)  == "string")

        c.add_section("  test12")
        c.add_section(" test22")
        c.add_section("test32")

        c.set("test12  ", "value12", 1)
        c.set(" test22 ", "value22", True)
        c.set("  test32", "value32", "string")

        assert(c.get("  test12", "value12", int)  == 1)
        assert(c.get(" test22 ", "value22", bool) is True)
        assert(c.get("test32  ", "value32", str)  == "string")

        c.add_section("test13  ")
        c.add_section(" test23 ")
        c.add_section("  test33")

        c.set("test13  ", "value13", 1)
        c.set(" test23 ", "value23", True)
        c.set("  test33", "value33", "string")

        assert(c.get("test13", "value13   ", int)  == 1)
        assert(c.get("test23", " value23  ", bool) is True)
        assert(c.get("test33", "   value33", str)  == "string")

    except :
        sys.exit(1)

    assert(c.dirty is True)

    sys.exit(0)
