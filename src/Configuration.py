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
import Exceptions

class Configuration(object) :
    def __init__(self) :
        self.__dirty  = False
        self.__values = { }

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
        assert(isinstance(section, str))
        s = string.strip(section)
        if (not self.__values.has_key(s)) :
            self.__values[s] = { }

    def remove_section(self, section) :
        assert(isinstance(section, str))
        s = string.strip(section)
        del self.__values[s]

    def sections(self) :
        return self.__values.keys()

    def has_section(self, section) :
        assert(isinstance(section, str))
        s = string.strip(section)
        if (self.__values.has_key(s)) :
            return True
        return False

    def add_option(self, section, option) :
        assert(isinstance(section, str))
        assert(isinstance(option, str))

        s = string.strip(section)
        o = string.strip(option)

        if (not self.__values.has_key(s)) :
            self.__values[s][o] = None

    def remove_option(self, section, option) :
        assert(isinstance(section, str))
        assert(isinstance(option, str))

        s = string.strip(section)
        o = string.strip(option)

        if (self.__values.has_key(s)) :
            del self.__values[s][o]

    def options(self, section) :
        assert(isinstance(section, str))
        s = string.strip(section)
        return self.__values[s].keys()

    def has_option(self, section, option) :
        assert(isinstance(section, str))
        assert(isinstance(option, str))
        s = string.strip(section)
        o = string.strip(option)

        if (self.__values.has_key(s)) :
            if (self.__values[section].has_key(o)) :
                return True
        return False

    def __get_option(self, section, option) :
        assert(isinstance(section, str))
        assert(isinstance(option, str))

        if (not self.__values.has_key(section)) :
            raise Exceptions.UnknownSection("section "           +
                                            "`" + section + "' " +
                                            "not found")

        if (not self.__values[section].has_key(option)) :
            raise Exceptions.UnknownOption("section "           +
                                           "`" + section + "' " +
                                           "has no option "     +
                                           "`" + option + "'")
        return self.__values[section][option]

    def get(self, section, option, datatype, default = None) :
        assert(isinstance(section, str))
        assert(isinstance(option, str))
        assert(datatype != None)

        s = string.strip(section)
        o = string.strip(option)

        try :
            # Look for configuration data from configuration
            tmp = self.__get_option(s, o)
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

    def __set_option(self, section, option, value) :
        assert(isinstance(section, str))
        assert(isinstance(option, str))

        if (not self.__values.has_key(section)) :
            self.__values[section] = { }

        self.__values[section][option] = value

    def set(self, section, option, value) :
        assert(isinstance(section, str))
        assert(isinstance(option, str))

        s = string.strip(section)
        o = string.strip(option)

        self.__set_option(s, o, value)
        self.__dirty = True

    def __clear(self) :
        self.__values.clear()
        self.__dirty = True

    def clear(self) :
        self.__clear()

    def __save(self, filename = None) :
        assert(isinstance(filename, str))

        handle = open(filename, 'w')
        assert(handle != None)

        for section in self.__values.keys() :
            debug("Saving section `" + section + "'")
            handle.write(string.join(("[", section, "]", "\n"),
                                     ""))
            for option in self.__values[section].keys() :
                debug("Saving option `" + option + "'")
                handle.write(option +
                             " = " +
                             str(self.__values[section][option]))
                handle.write('\n')
            handle.write('\n')

        handle.close()

    def save(self, filename) :
        assert(filename != None)
        assert(isinstance(filename, str))
        if (self.__dirty is not True) :
            debug("Configuration is not dirty, there is no need to save it")
            return
        self.__save(filename)
        debug("Configuration saved to `" + filename + "'")

    def __load(self, filename) :
        assert(isinstance(filename, str))

        handle  = open(filename, 'r')
        assert(handle != None)

        lines   = handle.readlines()

        loc     = 0
        section = ""
        value   = ""
        option  = ""
        for l in lines :
            # Purify input string
            l = string.strip(l)

            # Skip comments and empy lines
            if ((l == "") or (l[0] == "#")) :
                continue

            assert(len(l) > 0)

            if (l[0] == "[") :
                loc     = string.find(l, "]")
                section = l[1:loc]
                self.add_section(section)
            elif ((l[0] in string.letters) or
                  (l[0] in string.digits)) :
                loc    = string.find(l, "=")
                option = string.strip(l[0:loc])
                value  = string.strip(l[(loc + 1):])
                # Handling quoted values
                if ((value[0]              == '"' and
                     value[len(value) - 1] == '"') or
                    (value[0]              == "'" and
                     value[len(value) - 1] == "'")) :
                    value = value[1:(len(value) - 1)]
                self.__set_option(section, option, value)

        handle.close()

    def load(self, filename, merging = True) :
        assert(filename != None)
        assert(isinstance(filename, str))
        if (not merging) :
            self.__clear()
        self.__load(filename)
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

#    try :
#        f.add_section("test")
#
#        f.set_option("test", "value1", 1)
#        assert(f.get_option("test", "value1") == 1)
#
#        f.set_option("alfa", "value2", True)
#        assert(f.get_option("alfa", "value2") is True)
#        f.set_option("alfa", "value2", False)
#        assert(f.get_option("alfa", "value2") is False)
#
#        f.set_option("beta", "value3", "string")
#        assert(f.get_option("beta", "value3") == "string")
#        f.set_option("beta", "value3", True)
#        assert(f.get_option("beta", "value3") is True)
#        f.set_option("beta", "value3", "string")
#        assert(f.get_option("beta", "value3") == "string")
#        f.set_option(" gamma ", "value4", "string")
#        assert(f.get_option(" gamma ", "value4") == "string")
#
#        assert(len(f.sections()) == 4)
#        assert(f.has_section("test"))
#        assert(f.has_section("alfa"))
#        assert(f.has_section("beta"))
#        assert(f.has_section(" gamma "))
#
#        f.clear()
#
#        assert(len(f.sections()) == 0)
#        assert(not f.has_section("test"))
#        assert(not f.has_section("alfa"))
#        assert(not f.has_section("beta"))
#        assert(not f.has_section(" gamma "))
#
#    except :
#        sys.exit(1)

    sys.exit(0)
