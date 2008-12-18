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

def find(node, id) :
    assert(node != None)
    assert(id != None)

    debug("Looking for id `" + str(id) + "' into node `" + str(node) +"'")
    l = id.tolist()
    assert(len(l) > 0)

    tmp = node
    for i in l :
        if (i == 0) :
            continue

        assert(i >= 1)
        try :
            debug("Looking for child "
                  "`" + str(i) + "' "
                  "in node "
                  "`" + str(tmp) + "'")
            tmp = (tmp.children())[i - 1]
        except IndexError :
            debug("Child `" + str(i) + "' "
                  "is missing in node "
                  "`" + str(tmp) +"'")
            return None
        except :
            bug()

        if (tmp == None) :
            return tmp

    return tmp

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
