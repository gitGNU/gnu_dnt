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
from   Root        import *
from   Entry       import *
import Time
import Priority
import Exceptions

#
# XXX FIXME:
#     Please rearrange using SAX instead of DOM
#

#
# NOTE:
#     Root/Entry mix is allowed (at the moment)
#

def fromxml(xml) :
    debug("XML -> Tree in progress")

    #debug("Handling tag " + xml.tag)
    node = None

    if (xml.tag == "root") :
        text = xml.text
        if (text == None) :
            warning("Database has no name, using default one")
            text = "Default DB name"

        # Build a root node
        node = Root(text)

    elif (xml.tag == "entry") :
        text = xml.text
        if (text == None) :
            raise Exceptions.MalformedDatabase()

        priority = Priority.Priority()
        try :
            priority.fromstring(xml.attrib['priority'])
        except Exception, e :
            #debug(str(e))
            warning("No priority for entry `" + text + "', using default")

        start = Time.Time()
        try :
            start.fromstring(xml.attrib['start'])
        except Exception, e:
            #debug(str(e))
            warning("No start time for entry `" + text + "', using default")

        end = Time.Time()
        try :
            end.fromstring(xml.attrib['end'])
        except Exception, e:
            #debug(str(e))
            warning("No end time for entry `" + text +"', using default")

        # Build an entry node
        node = Entry(text, priority, start, end)

    else :
        raise Exceptions.EDatabase.UnknownElement(xml.tag)

    assert(node != None)

    j = 0
    for x in xml.getchildren() :
        debug("Working with child `" + str(x) + "'")
        tmp = fromxml(x)
        if (tmp != None) :
            node.child(j, tmp)
            j = j + 1

    #debug("Returning " + str(entry))
    return node

def toxml(node, xml) :
    debug("Tree -> XML for node `" + str(node) + "' in progress")
    assert(xml != None)

    if (node == None) :
        debug("Node `" + str(node) + "'has no children")
        return

    tag        = ""
    attributes = { }
    if (type(node) == Root) :
        debug("Creating root XML element");
        tag = "root"
    elif (type(node) == Entry) :
        debug("Creating entry XML element");
        if (node.priority != None) :
            attributes['priority'] = node.priority.tostring()
        if (node.start    != None) :
            attributes['start']    = node.start.tostring()
        if (node.end      != None) :
            attributes['end']      = node.end.tostring()
        tag = "entry"

    child      = ET.Element(tag, attributes)
    child.text = node.text

    #print(str(xml) + " (" + str(type(xml)) + ") = " + str(dir(xml)))

    if (hasattr(xml, "_setroot")) :
        xml._setroot(child)
    elif (hasattr(xml, "append")):
        xml.append(child)
    else :
        bug()

    for i in node.children() :
        debug("Navigating node `" + str(i) + "'")
        toxml(i, child)

    debug("Child `" + str(node) + "' navigation completed")

class Database(object) :
    def __init__(self) :
        debug("DB `" + str(self) + "' created successfully")

    def load(self, name) :
        assert(name != None)
        debug("Loading DB from `" + name + "'")

        try :
            debug("Parsing XML file")
            xml  = ET.parse(name)
            assert(xml != None)
            debug("XML file parsing completed successfully")

            xmlroot = xml.getroot()
            assert(xmlroot != None)
            debug("Got root node")

            #ET.dump(xmlroot)

            root = xmlroot

        except IOError, e :
            raise Exceptions.ProblemsReading(name, str(e))
        except Exception, e :
            raise Exceptions.ProblemsReading(name, str(e))
        except :
            bug()

        assert(xml != None)

        debug("XML transformation in progress")
        tree = fromxml(root)
        assert(tree != None)

        debug("DB `" + name + " ' loaded successfully")

        return tree

    def save(self, name, tree) :
        assert(name != None)
        debug("Saving DB into `" + name + "'")

        try :
            #xml = ET.Element(tree.text)
            xml = ET.ElementTree()
            assert(xml != None)
            toxml(tree, xml)
            assert(tree != None)

            #ET.dump(xml)

            #root = ET.ElementTree(xml)
            #root.write(name)
            xml.write(name, encoding = "")

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
