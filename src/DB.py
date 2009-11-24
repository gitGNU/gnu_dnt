# -*- python -*-

#
# Copyright (C) 2008, 2009 Francesco Salvestrini
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
from   xml.dom.minidom import *

from   Debug           import *
from   Trace           import *
import Root
import Entry
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

def fromxml(input_node) :
    #debug("XML -> Tree in progress")

    #debug("Handling tag " + xml.tag)
    node = None

    if (input_node.nodeType == 1) :
        text     = None
        priority = None
        start    = None
        end      = None
        comment  = None
        children = [ ]

       # Collecting entry and comment children and node text data
        for child in input_node.childNodes :
            if (child.nodeType == 1) :
                if (child.nodeName == "entry") :
                    children.append(child)
                elif (child.nodeName == "comment") :
                    # Collecting comment string
                    for i in child.childNodes :
                        assert(i.nodeType == 3)

                        if (comment == None) :
                            comment = i.data
                        else :
                            comment = comment + i.data
                    comment = comment.strip()
                else :
                    raise Exceptions.MalformedDatabase("Unknown tag `" +
                                                       child.nodeName +
                                                       "'")
            elif (child.nodeType == 3) :
                if (not child.data.isspace()) :
                    if (text == None) :
                        text = child.data
                    else :
                        text = text + child.data

                    text = text.strip()
            elif ((child.nodeType == 2) or (4 <= child.nodeType <= 10)) :
                # Skip unused nodes
                pass
            else :
                raise Exceptions.UnknownElement(child)

       # If we are on root node, build it and skip attributes processing
        if (input_node.nodeName == "root") :
            if (text == None) :
                warning("Database has no name, using default one")
                text = "Default DB name"
            node = Root.Root(text)
#            raise Exceptions.MalformedDatabase("Missing database name")
        elif (input_node.nodeName == "entry") :
            if (text == None) :
                raise Exceptions.MalformedDatabase()

            # Looking for priority attribute
            # debug("Priority is:      `" + input_node.getAttribute("start") +
            #       "'")
            priority = Priority.Priority()
            if (not input_node.hasAttribute("priority")) :
                warning("No priority for entry `" + text + "', using default")
            else :
                priority.fromstring(str(input_node.getAttribute("priority")))

            # Looking for start attribute
            value = None

            if (input_node.hasAttribute("start")) :
                value = input_node.getAttribute("start")
                try :
                    start = Time.Time(int(value))
                    debug("Start time value: `" + str(value) + "'")
                # Our exceptions first
                except Exceptions, e :
                    error("Wrong start time format for entry " +
                          "`" + text +"' (" + str(e) + ")")
                    raise Exceptions.MalformedDatabase()
                except ValueError :
                    error("Wrong start time for entry " +
                          "`" + text +"'")
                    raise Exceptions.MalformedDatabase()
                except Exception, e :
                    bug(str(e))
            else :
                raise Exceptions.MalformedDatabase("Missing start time " +
                                                   "for entry "          +
                                                   "`" + text + "'")

            # Looking for end time attribute
            value = None

            if (input_node.hasAttribute("end")) :
                value = input_node.getAttribute("end")
                try :
                    end   = Time.Time(int(value))
                    debug("End time value: `" + str(value) + "'")
                # Our exceptions first
                except Exceptions, e :
                    error("Wrong end time format for entry " +
                          "`" + text +"' (" + str(e) + ")")
                    raise Exceptions.MalformedDatabase()
                except ValueError :
                    error("Wrong end time for entry " +
                          "`" + text +"'")
                    raise Exceptions.MalformedDatabase()
                except Exception, e :
                    bug(str(e))
            else :
                # debug("No end time for entry `" + text + "'")
                pass

            if (comment != None) :
                comment.strip(' \t\n\v\b\r')

            # Build an entry node
            node = Entry.Entry(text, priority, start, end, comment)

        else :
            raise Exceptions.MalformedDatabase("Invalid child node name " +
                                               "`" + child.nodeName + "'")

        # Processing children
        for child in children :
            tmp = fromxml(child)
            assert(tmp != None)

            node.add(tmp)

    else :
        raise Exceptions.UnknownElement(input_node.nodeType)

    # debug("Returning " + str(entry))
    return node

def toxml(node, xml_document, xml_element) :
    # debug("Tree -> XML for node `" + str(node) + "' in progress")
    assert(xml_document != None)

    if (node == None) :
        # debug("Node `" + str(node) + "'has no children")
        return

    element    = None
    tag        = ""
    attributes = { }
    text       = None

    if (isinstance(node, Root.Root)) :
        assert(xml_element == None)

        # debug("Creating root XML element");
        tag = "root"
    elif (isinstance(node, Entry.Entry)) :
        assert(xml_element != None)

        # debug("Creating entry XML element");
        if (node.priority != None) :
            attributes['priority'] = node.priority.tostring()
        if (node.start    != None) :
            attributes['start']    = str(node.start.toint())
        if (node.end      != None) :
            attributes['end']      = str(node.end.toint())
        tag = "entry"

    element = xml_document.createElement(tag)
    assert(element != None)

    text = xml_document.createTextNode(node.text)
    assert(text != None)
    element.appendChild(text)

    if ((isinstance(node, Entry.Entry)) and (node.comment  != None)) :
        comment_tag        = "comment"
        subelement         = xml_document.createElement(comment_tag)
        subelement_text    = xml_document.createTextNode(node.comment)

        subelement.appendChild(subelement_text)
        element.appendChild(subelement)

    if len(attributes) > 0 :

        for name in attributes :
            element.setAttribute(name, attributes[name])


    for i in node.children :
        # debug("Navigating node `" + str(i) + "'")
        x = toxml(i, xml_document, element)
        assert(x != None)

        element = x

    if (xml_element != None) :
        xml_element.appendChild(element)
    else :
        xml_element = element

    # debug("Child `" + str(node) + "' navigation completed")

    return xml_element

class Database(object) :
    def __init__(self) :
        debug("DB `" + str(self) + "' created successfully")

    def load(self, name) :
        assert(name != None)
        # debug("Loading DB from `" + name + "'")

        try :
            # debug("Parsing XML file")
            xml_input  = xml.dom.minidom.parse(name)
            assert(xml_input != None)
            # debug("XML file parsing completed successfully")

            xml_root = xml_input.documentElement
            assert(xml_root != None)
            # debug("Got root node")

        except IOError, e :
            raise Exceptions.ProblemsReading(name, str(e))
        except Exception, e :
            raise Exceptions.ProblemsReading(name, str(e))
        except :
            bug("Unhandled exception while loading DB from file")

        # debug("XML transformation in progress")
        tree = fromxml(xml_root)
        assert(tree != None)

        # debug("DB `" + name + " ' loaded successfully")

        return tree

    def save(self, name, tree) :
        assert(name != None)
        assert(tree != None)
        # debug("Saving DB into `" + name + "'")

        try :
            xml_output = xml.dom.minidom.Document()
            assert(xml_output != None)

            x = toxml(tree, xml_output, None)
            assert(x != None)

            xml_output.appendChild(x)

            try :
                filehandle = open(name, "w")
            except :
                raise Exceptions.CannotWrite(name)

            filehandle.write(xml_output.toprettyxml())
            filehandle.close()

        except IOError, e :
            raise Exceptions.ProblemsWriting(name, str(e))
        except Exception, e :
            raise Exceptions.ProblemsWriting(name, str(e))
        except :
            bug("Unhandled exception while saving DB to file")

        # debug("DB `" + name + " ' saved successfully")

# Test
if (__name__ == '__main__') :
    db = Database()

    #debug("Test completed")
    sys.exit(0)
