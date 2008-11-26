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
from   elementtree.ElementTree import ElementTree

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
	raise Exceptions.Database("unknown element")

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
    assert(tree != None)
    assert(xml != None)

    print xml

    debug("Tree -> XML completed")

    return xml

class Database :
    def __init__(self) :
	debug("Creating empty DB")

    def load(self, name) :
	assert(name != None)
	debug("Loading DB from `" + name + "'")

	try :
	    x = ElementTree(name)
            all = x.parse()
            print all
	except IOError :
	    raise Exceptions.Database("problems reading database " +
				      "`" + name + "'")
	except Exception, e :
	    raise Exceptions.Database("problems parsing input database " +
				      "`" + name + "' (" + str(e) + ")")
	except :
	    bug()

	if (all == None) :
	    raise Exceptions.Database("missing root in input file " +
				      "`" + name + "'")
	xml = all.getroot()

	return fromxml(xml)

    def save(self, name, tree) :
	assert(name != None)
	debug("Saving DB into `" + name + "'")

	try :
	    et = ElementTree()
            #xml = ET.SubElement(et.getroot(), "note")
            #xml.text = "1.2.0"
	    #toxml(tree, xml)
	    #assert(xml != None)

	    debug("Writing XML file")
	    et.write(name)
	except IOError :
	    raise Exceptions.Database("problems writing database " +
				      "`" + name + "'")
	except Exception, e :
	    raise Exceptions.Database("problems formatting database " +
				      "`" + name + "' (" + str(e) + ")")
	except :
	    bug()

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
