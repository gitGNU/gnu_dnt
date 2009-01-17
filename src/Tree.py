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

from   Debug    import *
from   Trace    import *
from   ID       import *
from   Node     import *

def _find_recursive(node, l) :
    assert(node != None)
    assert(len(l) > 0)

    if (l[0] == 0) :
        # Caller is looking for this node ...
        assert(len(l) == 1)
        return node

    debug("Looking for element `" + str(l) + "' into node `" + str(node) + "'")

    tmp = node
    i   = l[0] - 1

    if ((i < 0) or (i >= len(tmp.children()))) :
        return None

    try :
        debug("Descending into node `" + str(i) + "' in `" + str(tmp) + "'")
        tmp = (tmp.children())[i]
    except IndexError :
        debug("Child `" + str(i) + "' is missing in `" + str(tmp) + "'")
        return None
    except Exception, e:
        bug(str(e))

    l.pop(0)
    if (len(l) == 0) :
        return tmp
    else :
        return _find_recursive(tmp, l)

def find(node, id) :
    assert(node != None)
    assert(id   != None)

    debug("Looking for id `" + str(id) + "' into node `" + str(node) + "'")

    l = id.tolist()
    assert(len(l) > 0)

    debug("Splitted id is " + str(l))

    n = _find_recursive(node, l)
    debug("Got `" + str(n) + "'")
    return n

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
