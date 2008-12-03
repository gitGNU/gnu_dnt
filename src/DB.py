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

    if (xml.tag == "entry") :
	text     = xml.text
        try :
            priority = string_to_priority(xml.attrib['priority'])
        except :
            priority = Entry.PRIORITY_MEDIUM
        try :
            time     = xml.attrib['time']
        except :
            time     = datetime.date.today()
    else :
	raise Exceptions.Database("unknown element `" + xml.tag + "'")

    entry = Entry(text, priority, time)

    j = 0
    for x in xml.getchildren() :
	#debug("Working with child")
	tmp = fromxml(x)
	if (tmp != None) :
	    entry.child(j, tmp)
	    j = j + 1

    #debug("Returning " + str(entry))
    return entry

def toxml(node, xml) :
    debug("Tree -> XML for node `" + str(node) + "' in progress")
    assert(xml != None)

    if (node == None) :
	debug("Node `" + str(node) + "'has no children")
	return

    child = ET.SubElement(xml,
                          tag = "entry")
#    ,
#                          attrib = {
#            'priority' : string_to_priority(node.priority),
#            'time'     : node.time })
    assert(child != None)

    child.text = node.text

    for i in node.children() :
	debug("Navigating node `" + str(i) + "'")
	toxml(i, child)

    debug("Child `" + str(node) + "' navigation completed")

class Database :
    def __init__(self) :
	debug("Creating empty DB")

    def load(self, name) :
	assert(name != None)
	debug("Loading DB from `" + name + "'")

	try :
	    xml  = ET.parse(name)
            assert(xml != None)
	    root = xml.getroot()
            assert(root != None)
            if (len(root) > 1) :
                raise Exceptions.Database("malformed database format " +
                                          "in file `" + name + "')")
            root = root[0]

            #ET.dump(root)

	except IOError, e :
	    raise Exceptions.Database("problems reading database " +
				      "`" + name + "' (" + str(e) + ")")
	except Exception, e :
	    raise Exceptions.Database("problems parsing input database " +
				      "`" + name + "' (" + str(e) + ")")
	except :
	    bug()

	assert(xml != None)

	return fromxml(root)

    def save(self, name, tree) :
	assert(name != None)
	debug("Saving DB into `" + name + "'")

	try :
	    xml = ET.Element(tree.text)
            assert(xml != None)
	    toxml(tree, xml)
            assert(tree != None)

            #ET.dump(xml)

	    root = ET.ElementTree(xml)
	    root.write(name)

	except IOError, e :
	    raise Exceptions.Database("problems writing database " +
				      "`" + name + "' (" + str(e) + ")")
	except Exception, e :
	    raise Exceptions.Database("problems formatting database " +
				      "`" + name + "' (" + str(e) + ")")
	except :
	    bug()

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
