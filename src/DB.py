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

from   Trace       import *
from   Entry       import *
import Time
import Priority
import Exceptions

#
# XXX FIXME:
#     Please rearrange using SAX instead of DOM
#

# Internal use (XML->Tree)
def fromxml(xml) :
    debug("XML -> Tree in progress")

    #debug("Handling node tag " + xml.tag)

    if (xml.tag == "entry") :
        text     = xml.text

        try :
            priority = priority.fromstring(xml.attrib['priority'])
        except :
            priority = Priority.Priority()

        try :
            start    = Time.Time().fromstring(xml.attrib['start'])
        except :
            warning("No start time for entry, using default")
            start    = Time.Time()

        try :
            end      = Time.Time().fromstring(xml.attrib['end'])
        except :
            warning("No end time for entry, using default")
            end      = Time.Time()

    else :
        raise Exceptions.EDatabase.UnknownElement(xml.tag)

    entry = Entry(text, priority, start, end)

    j = 0
    for x in xml.getchildren() :
        debug("Working with child `" + str(x) + "'")
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
                          tag = "entry",
                          attrib = {
            'priority' : node.priority.tostring(),
            'start'    : node.start.tostring(),
            'end'      : node.end.tostring() })
    assert(child != None)

    child.text = node.text

    for i in node.children() :
        debug("Navigating node `" + str(i) + "'")
        toxml(i, child)

    debug("Child `" + str(node) + "' navigation completed")

class Database(object) :
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
                raise Exceptions.MalformedDatabase(name)
            root = root[0]

            #ET.dump(root)

        except IOError, e :
            raise Exceptions.ProblemsReading(name, str(e))
        except Exception, e :
            raise Exceptions.ProblemsReading(name, str(e))
        except :
            bug()

        assert(xml != None)

        tree = fromxml(root)
        assert(tree != None)

        debug("DB `" + name + " ' loaded successfully")

        return tree

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
            raise Exceptions.ProblemsWriting(name, str(e))
        except Exception, e :
            bug() #raise Exceptions.ProblemsWriting(name, str(e))
        except :
            bug()

        debug("DB `" + name + " ' saved successfully")

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
