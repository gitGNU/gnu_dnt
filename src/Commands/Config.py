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
import ConfigParser

from   Debug      import *
from   Trace      import *
from   Command    import *
import Exceptions

import DB
import Entry
from   ID         import *

def description() :
    return "manage current configuration"

def _get_section(s) :
    assert(s != None)

    regexp = re.compile('^[ \t]*(.*\.).*$')
    return regexp.match(s).group(1)

def do(configuration, arguments) :
    command = Command("config")

    # Parameters setup
    command.add_option("-s", "--set",
		       action = "store_true",
		       dest   = "set",
		       help   = "set a (local) configuration key value")
    command.add_option("-g", "--get",
		       action = "store_true",
		       dest   = "get",
		       help   = "get a configuration key value")
    command.add_option("-S", "--show",
		       action = "store_true",
		       dest   = "show",
		       help   = "show all configuration values")

    command.add_option("-k", "--key",
		       action = "store",
		       dest   = "key",
		       help   = "specify key to get/set")
    command.add_option("-v", "--value",
		       action = "store",
		       dest   = "value",
		       help   = "specify value to set")

    # Parameters parsing
    (opts, args) = command.parse_args(arguments)

    # Parameters checks
    if (opts.set != True and opts.get != True and opts.show != True) :
	raise Exceptions.MissingParameters()
    if (opts.set == True and opts.get == True) :
	raise Exceptions.TooManyParameters()
    if ((opts.set == True or opts.get == True) and opts.show == True) :
	raise Exceptions.WrongParameters()

    if (opts.set == True) :
	if (opts.key == None) :
	    raise Exceptions.MissingParameters("key in order to set a "
					       "configuration entry")
	if (opts.value == None) :
	    raise Exceptions.MissingParameters("value in order to set a "
					       "configuration entry")
    if (opts.get == True) :
	if (opts.key == None) :
	    raise Exceptions.MissingParameters("key in order to get a "
					       "configuration entry")

    # Work
    section = 'GLOBAL'

    try :
	if (opts.get == True) :
	    assert(opts.key != None)
            section = _section(opts.key)
	    debug("Getting key `" + opts.key + "'")
	    print(configuration.get(section, opts.key))

	if (opts.set == True) :
	    assert(opts.key   != None)
	    assert(opts.value != None)
	    debug("Setting key `" + opts.key + "' to `" + opts.value + "'")
	    configuration.set(section, opts.key, opts.value)

	if (opts.show == True) :
	    debug("Showing all key/value pairs")
	    # Compute maximum key length
	    l = 0
	    for s in configuration.sections() :
                for o in configuration.options(section) :
                    l = max(l, len(s + "." + o))

	    # Write all key-value pairs
	    for s in configuration.sections() :
                for o in configuration.options(section) :
                    print(("%-" + str(l) + "s = %s")
                          %(s + "." + o,  configuration.get(s, o)))

    except ConfigParser.Error, e :
	error(e)
	return 1
    except :
	bug()

    return 0

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
