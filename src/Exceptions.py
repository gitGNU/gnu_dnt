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

import Trace
from   Entry import *

class Base(Exception):
    def __init__(self, value) :
	self.__value = value

    def __str__(self) :
	#return repr(self.__value)
	return self.__value

    __repr__ = __str__

#
# Database related exceptions
#
class Database(Base):
    def __init__(self, value) :
	Base.__init__(self, value)

class MissingDatabase(Database):
    def __init__(self, value) :
	Base.__init__(self, "missing database, try initializing or importing")

class CorruptedDatabase(Database):
    def __init__(self, value) :
	Base.__init__(self, "database `" + value + "' is corrupted")

#
# Database related exceptions
#
class Configuration(Base):
    def __init__(self, value) :
	Base.__init__(self, value)

class UnknownKey(Database):
    def __init__(self, value) :
	Base.__init__(self, "unknown key `" + value + "' in configuration")

#
# Parameters related exceptions
#
class Parameters(Base):
    def __init__(self, value) :
	Base.__init__(self, value)

class MissingParameters(Parameters):
    def __init__(self, value = "parameter(s)") :
	Parameters.__init__(self, "missing " + value)

class TooManyParameters(Parameters):
    def __init__(self) :
	Parameters.__init__(self, "too many parameter(s)")

class UnknownArgument(Parameters):
    def __init__(self) :
	Parameters.__init__(self, "unknown argument")

class UnknownParameter(Parameters):
    def __init__(self, value) :
	Parameters.__init__(self, "unknown parameter `" + value + "'")

class WrongParameters(Parameters):
    def __init__(self, value) :
	s = ""
	if (value != None) :
	    s = ", " + value
	Parameters.__init__(self, "wrong parameters" + s)

class ForceNeeded(Parameters):
    def __init__(self, value) :
	Parameters.__init__(self, value + ", use `--force' to override")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
