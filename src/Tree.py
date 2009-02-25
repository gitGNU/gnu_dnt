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

from   Debug      import *
from   Trace      import *
import Node
import ID
import Exceptions

def _find_recursive(node, l) :
    assert(node != None)
    assert(len(l) > 0)

    debug("Looking recursively for node " + str(l))

    if (l[0] == 0) :
        # 0 means 'this node'

        if (len(l) > 1) :
            l.pop(0)
            return _find_recursive(node, l)

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
    if (len(l) <= 0) :
        raise Exceptions.MalformedId("id `" + id + "` is empty")

    debug("Splitted id is " + str(l))

    n = _find_recursive(node, l)
    debug("Got `" + str(n) + "'")
    return n

# Test
if (__name__ == '__main__') :
    root = Node.Node()
    e1   = Node.Node()
    e11  = Node.Node()
    e12  = Node.Node()
    e2   = Node.Node()

    e1.child(0, e12)
    e1.child(0, e11)
    root.child(0, e1)
    root.child(1, e2)

    n = find(root, ID.ID("0"))
    assert(n != None)
    n = find(root, ID.ID("0.1"))
    assert(n != None)
    n = find(root, ID.ID("0.2"))
    assert(n != None)
    n = find(root, ID.ID("0.1.1"))
    assert(n != None)
    n = find(root, ID.ID("0.1.2"))
    assert(n != None)

    n = find(root, ID.ID("1"))
    assert(n != None)
    n = find(root, ID.ID("2"))
    assert(n != None)
    n = find(root, ID.ID("1.1"))
    assert(n != None)
    n = find(root, ID.ID("1.2"))
    assert(n != None)

    n = find(root, ID.ID("1.0"))
    assert(n != None)
    n = find(root, ID.ID("2.0"))
    assert(n != None)
    n = find(root, ID.ID("1.1.0"))
    assert(n != None)
    n = find(root, ID.ID("1.2.0"))
    assert(n != None)

    n = find(root, ID.ID("1.0.0"))
    assert(n != None)
    n = find(root, ID.ID("2.0.0"))
    assert(n != None)
    n = find(root, ID.ID("1.0.1.0"))
    assert(n != None)
    n = find(root, ID.ID("1.2.0.0"))
    assert(n != None)

    debug("Test completed")
    sys.exit(0)
