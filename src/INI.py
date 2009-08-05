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
import string

from   Debug      import *
from   Trace      import *
import Exceptions

class File(object) :
    def __init__(self, filename = None) :
        debug("Initializing INI file instance")
        self.__values = { }
        if (filename != None) :
            debug("Passed INI filename")
            self.__filename = filename
            self.load()

    def add_section(self, section) :
        assert(isinstance(section, str))
        if (not self.__values.has_key(section)) :
            self.__values[section] = { }

    def remove_section(self, section) :
        assert(isinstance(section, str))
        del self.__values[section]

    def get(self, section, option) :
        try:
            return self.__values[section][option]
        except KeyError, e:
            raise Exceptions.KeyNotFound(str(e))

    def set(self, section, option, value) :
        assert(value != None)

        if (not self.__values.has_key(section)) :
            self.__values[section] = { }
        self.__values[section][option] = value

    # XXX: To be removed ASAP
    def read(self, filename) :
        self.load(filename)

    # XXX: To be removed ASAP
    def write(self, handle) :
        self.save(handle.name())

    def load(self, filename = None) :
        if (filename != None) :
            self.__filename = filename

        if (self.__filename == None) :
            raise Exceptions.MissingFilename()

        assert(isinstance(self.__filename, str))

        debug("Loading INI data from `" + self.__filename + "'")
        handle  = open(self.__filename, 'r')
        assert(handle != None)

        lines   = handle.readlines()

        loc     = 0
        section = ""
        value   = ""
        option  = ""
        for l in lines :
            l = string.strip(l)
            if (len(l) > 0) :
                if (l[0] == "[") :
                    loc     = string.find(l, "]")
                    section = l[1:loc]
                    self.add_section(section)
                elif ((l[0] in string.letters) or
                      (l[0] in string.digits)) :
                    loc    = string.find(l, "=")
                    option = l[0:loc]
                    value  = l[(loc + 1):]
                    self.set(section, option, value)

        handle.close()

    def save(self, filename = None) :
        if (filename != None) :
            self.__filename = filename

        if (self.__filename == None) :
            raise Exceptions.MissingFilename()

        assert(isinstance(self.__filename, str))

        debug("Saving INI data to `" + self.__filename + "'")
        handle = open(self.__filename, 'w')
        assert(handle != None)

        for section in self.__values.keys() :
            handle.write(string.join(("[", section, "]", "\n"),""))
            for option in self.__values[section].keys() :
                handle.write(string.join((option, "=",
                                          self.__values[section][option],
                                          "\n"),
                                         ""))
            handle.write('\n')

        handle.close()

# Test
if (__name__ == '__main__') :

    f = File()
    assert(f != None)

    try :
        f.add_section("test")

        f.set("test", "value1", 1)
        assert(f.get("test", "value1") == 1)

        f.set("test", "value2", True)
        assert(f.get("test", "value2") == True)

        f.set("test", "value3", "string")
        assert(f.get("test", "value3") == "string")
    except :
        sys.exit(1)

    print("X")
    debug("Test completed")
    sys.exit(0)
