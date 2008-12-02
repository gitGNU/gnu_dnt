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
from   xml.etree   import ElementTree as ET

import Trace
from   Entry       import *
import Exceptions

#
# XXX FIXME:
#     Please rearrange using SAX instead of DOM
#

def string_to_priority(p) :
    assert(type(p) == str)
    t = string.lower(p)
    if (t == "veryhigh") :
	return Entry.PRIORITY_VERYHIGH
    elif (t == "high") :
	return Entry.PRIORITY_HIGH
    elif (t == "medium") :
	return Entry.PRIORITY_MEDIUM
    elif (t == "low") :
	return Entry.PRIORITY_LOW
    elif (t == "verylow") :
	return Entry.PRIORITY_VERYLOW
    else :
	raise Exceptions.Database("unknown priority " + p)

# Internal use (XML->Tree)
def fromxml(xml) :
    debug("XML -> Tree in progress")

    #debug("Handling node tag " + xml.tag)

    if (xml.tag == "note") :
	text     = xml.text # XXX FIXME: Could be None
	priority = string_to_priority(xml.attrib['priority'])
	time     = xml.attrib['time']
    elif (xml.tag == "todo") :
	text     = "root"
	priority = string_to_priority("medium")
	time     = ""
    else :
	raise Exceptions.Database("unknown element `" + xml.tag + "'")

    entry = Entry(text, priority, time)
    #debug("Created node " + str(entry))

    j = 0
    for x in xml.getchildren() :
	#debug("Working with child")
	tmp = fromxml(x)
	if (tmp != None) :
	    entry.child(j, tmp)
	    j = j + 1

    #debug("Returning " + str(entry))
    return entry

def toxml(tree, xml) :
    debug("Tree -> XML in progress")
    assert(xml != None)

    if (tree == None) :
        return

    child = ET.Element(tree)
    child.text = tree.text

    for i in tree.children() :
        toxml(i, child)

class Database :
    def __init__(self) :
	debug("Creating empty DB")

    def load(self, name) :
	assert(name != None)
	debug("Loading DB from `" + name + "'")

	xml  = None
        root = None
	try :
	    xml  = ET.parse(name)
            root = xml.getroot()
	except IOError, e :
	    raise Exceptions.Database("problems reading database " +
				      "`" + name + "' (" + str(e) + ")")
	except Exception, e :
	    raise Exceptions.Database("problems parsing input database " +
				      "`" + name + "' (" + str(e) + ")")
	except :
	    bug()

	if (xml == None) :
	    raise Exceptions.Database("missing root in input file " +
				      "`" + name + "'")

        # Operation completed successfully
        assert(xml != None)
	#ET.dump(xml)

	return fromxml(root)

    def save(self, name, tree) :
	assert(name != None)
	debug("Saving DB into `" + name + "'")

        xml = None
	try :
	    xml  = ET.Element('xml')
	    root = ET.ElementTree(xml)

            toxml(tree, root)

	    root.write(name)
	except IOError, e :
	    raise Exceptions.Database("problems writing database " +
				      "`" + name + "' (" + str(e) + ")")
	except Exception, e :
	    raise Exceptions.Database("problems formatting database " +
				      "`" + name + "' (" + str(e) + ")")
	except :
	    bug()

        # Operation completed successfully
        assert(xml != None)
        #ET.dump(xml)

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
