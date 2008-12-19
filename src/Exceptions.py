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

from   Trace import *

class EBase(Exception):
    def __init__(self, value) :
        self.__value = value

    def __str__(self) :
        #return repr(self.__value)
        return self.__value

    __repr__ = __str__

#
# OS related exceptions
#
class EOS(EBase):
    def __init__(self, value) :
        EBase.__init__(self, value)

#
# Priority related exceptions
#
class EPriority(EBase):
    def __init__(self, value) :
        assert(value != None)
        EBase.__init__(self, value)

class UnknownPriority(EPriority):
    def __init__(self, value) :
        assert(value != None)
        EPriority.__init__(self, "unknown priority `" + value + "'")

#
# Database related exceptions
#
class EDatabase(EBase):
    def __init__(self, value) :
        assert(value != None)
        EBase.__init__(self, value)

class UnknownElement(EDatabase):
    def __init__(self, value) :
        assert(value != None)
        EDatabase.__init__(self, "unknown element `" + value + "'")

class MissingDatabase(EDatabase):
    def __init__(self, value) :
        assert(value != None)
        EDatabase.__init__(self,
                           "missing database "
                           "`" + value + "' "
                           ", try initializing or importing")

class MalformedDatabase(EDatabase):
    def __init__(self, value = None) :
        tmp = ""
        if (value != None) :
            tmp = " `" + value + "'"
        EDatabase.__init__(self, "malformed database" + tmp)

class CorruptedDatabase(EDatabase):
    def __init__(self, value) :
        assert(value != None)
        EDatabase.__init__(self,
                           "database "
                           "`" + value + "' "
                           "is corrupted")

class ProblemsReading(EDatabase):
    def __init__(self, name, value) :
        assert(name != None)
        tmp = ""
        if (value != None) :
            tmp = ", " + value
            EDatabase.__init__(self,
                               "problems reading database "
                               "`" + name+ "'" + tmp)

class ProblemsWriting(EDatabase):
    def __init__(self, name, value) :
        assert(name != None)
        tmp = ""
        if (value != None) :
            tmp = ", " + value
            EDatabase.__init__(self,
                               "problems writing database "
                               "`" + name+ "'" + tmp)

#
# ID related exceptions
#
class EID(EBase):
    def __init__(self, value) :
        EBase.__init__(self, value)

class MalformedId(EID):
    def __init__(self, value) :
        EIDBase.__init__(self, value)

class Parentless(EID):
    def __init__(self, value) :
        EIDBase.__init__(self, "node `" + value + "' is parentless")

#
# Configuration related exceptions
#
class EConfiguration(EBase):
    def __init__(self, value) :
        EBase.__init__(self, value)

class UnknownSection(EConfiguration):
    def __init__(self, value) :
        EConfiguration.__init__(self,
                                "unknown section "
                                "`" + value + "' "
                                "in configuration")

class MissingSection(EConfiguration):
    def __init__(self, value) :
        EConfiguration.__init__(self, "missing section")

class MissingKey(EConfiguration):
    def __init__(self, value) :
        EConfiguration.__init__(self, "missing key")

class UnknownKey(EConfiguration):
    def __init__(self, value) :
        EConfiguration.__init__(self,
                                "unknown key "
                                "`" + value + "' "
                                "in configuration")

#
# Parameters related exceptions
#
class EParameters(EBase):
    def __init__(self, value) :
        EBase.__init__(self, value)

class MissingParameters(EParameters):
    def __init__(self, value = "parameter(s)") :
        EParameters.__init__(self, "missing " + value)

class TooManyParameters(EParameters):
    def __init__(self) :
        EParameters.__init__(self, "too many parameter(s)")

class UnknownArgument(EParameters):
    def __init__(self) :
        EParameters.__init__(self, "unknown argument")

class UnknownParameter(EParameters):
    def __init__(self, value) :
        EParameters.__init__(self, "unknown parameter `" + value + "'")

class WrongParameters(EParameters):
    def __init__(self, value = None) :
        s = ""
        if (value != None) :
            s = ", " + value
        EParameters.__init__(self, "wrong parameters" + s)

class ForceNeeded(EParameters):
    def __init__(self, value) :
        EParameters.__init__(self, value + ", use `--force' to override")

#
# Tree related exceptions
#
class TreeBase(EBase):
    def __init__(self, value) :
        EBase.__init__(self, value)

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
