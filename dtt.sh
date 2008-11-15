#!/usr/bin/python

import os
import sys
import traceback
import getopt
import datetime
import pprint
import re
import elementtree.ElementTree as ET

PACKAGE_NAME    = "Development Tracking Tool"
PACKAGE_VERSION = "0.1"
PROGRAM_NAME    = "dtt"

class Node :
    __parent   = None
    __children = []
    __index    = 0

    def __init__(self, p = None, c = []) :
	self.__parent   = p
	self.__children = c
	self.__index    = 0

    def __repr__(self) :
	return '<Node %#x>' %(id(self))

    # Iterator related methods
    def __iter__(self):
	return self
    def next(self):
	if (self.__index == self.__children.len()) :
	    raise StopIteration
        tmp = self.__children[self.__index]
	self.__index = self.__index + 1
	return tmp

    def parent(self) :
	return self.__parent

    def parent(self, node) :
	self.__parent = node

    def children(self) :
	return self.__children

    def child(self, index, node) :
        debug("Node " + str(self) +
              " has " + str(len(self.__children)) +
              " children")
        if (node == None) :
            debug("Removing node " + str(node) + " from position " + str(index))
            self.__children.remove(index)
        else :
            debug("Inserting node " + str(node) + " in position " + str(index))
            self.__children.insert(index, node)
        debug("Node " + str(self) +
              " has " + str(len(self.__children)) +
              " children")

class Entry(Node) :
    def __init__(self,
		 title    = "",
		 note     = "",
		 priority = "",
		 time     = datetime.date.today()) :
	self.__title    = title
	self.__note     = note
	self.__priority = priority
	self.__time     = time

    def __repr__(self) :
	return '<Entry %#x>' %(id(self))

    def title(self) :
	return self.__title
    def title(self, p) :
	# Remove leading and trailing whitespaces
	#        assert(p != None)
	#	self.title_ = re.match(r'^[ \t]*(.*)[ \t]*$', p).group(1)
	self.__title = p

    def note(self) :
	return self.__note
    def note(self, p) :
	# Remove leading and trailing whitespaces
	#        assert(p != None)
	#	self.title_ = re.match(r'^[ \t]*(.*)[ \t]*$', p).group(1)
	self.__note = p

    def priority(self) :
	return self.__priority
    def priority(self, p) :
	self.__priority = p

    def time(self) :
	return self.__time
    def time(self, p) :
	self.__time = p

    def dump(self, indent) :
	print(indent + self.__title)
	print(indent + self.__note)
	print(indent + self.__priority)
	#print(s + self.__time)
	for j in self.children() :
	    j.dump(indent + indent)

class DB :
    def __init__(self) :
	pass

    # Internal use (XML->Tree)
    def fromxml(self, xml) :
        debug("Handling node tag " + xml.tag)

	if (xml.tag == "note") :
            title    = ""
            note     = ""
            priority = xml.attrib['priority']
            time     = xml.attrib['time']
        elif (xml.tag == "todo") :
            title    = "root"
            note     = ""
            priority = ""
            time     = ""
        else :
            raise Exception("Unknown element")

        entry = Entry(title, note, priority, time)
        debug("Created node " + str(entry))

        j = 1
	for x in xml.getchildren() :
            tmp = self.fromxml(x)
            debug("Working with child " + str(tmp))
            if (tmp != None) :
                tmp.parent(entry)
                entry.child(j, tmp)
                j = j + 1

        debug("Returning " + str(entry))

        return entry

    # Internal use (Tree->XML)
    def toxml(self, tree) :
	return None

    def load(self, name) :
	xml  = ET.parse(name).getroot()
	return self.fromxml(xml)

    def save(self, name, tree) :
	xml = self.toxml(tree)
	xml.write(name)

def debug(s) :
    print(PROGRAM_NAME + ": " + s)

def error(s) :
    print(PROGRAM_NAME + ": " + s)

def warning(s) :
    print(PROGRAM_NAME + ": " + s)

def bug(s = "") :
    tmp1 = "Bug hit"
    if s != "" :
	tmp2 = tmp1 + ": " + s
    else :
	tmp2 = tmp1 + "!"

    error(tmp2)
    os._exit(1)

def hint(s) :
    print(s)
    print("Use `" + PROGRAM_NAME + " -h' for help")

def usage() :
    print(PROGRAM_NAME + " OPTIONS")
    print("")
    print("  -v | --verbose    Enable debug mode")
    print("  -h | --help       This help")
    print("")
    print("Report bugs to <@PACKAGE_BUGREPORT@>")

def version() :
    print(PROGRAM_NAME + " (" + PACKAGE_NAME + ") " + PACKAGE_VERSION)

def main(args) :
    # Parse command line
    try :
	opts, args = getopt.getopt(args[1:],
				   "a:r:e:R:svh",
				   [ "add=",
				     "remove=",
				     "edit=",
				     "reparent=",
				     "show",
				     "help",
				     "version" ])
    except getopt.GetoptError :
	hint("Parameter(s) error")
	return 1

    action      = "show"
    source      = ".todo"
    destination = ".dtt"
    for opt, arg in opts :
	if opt in ("-a", "--add") :
	    action = "add" ;      parms  = ("")
	elif opt in ("-r", "--remove") :
	    action = "remove" ;   parms  = ("") ;
	elif opt in ("-e", "--edit") :
	    action = "edit" ;     parms  = ("")
	elif opt in ("-r", "--reparent") :
	    action = "reparent" ; parms  = ("")
	elif opt in ("-s", "--show") :
	    action = "show" ;     parms  = ("")
	elif opt in ("-h", "--help") :
	    usage()
	    return 0
	elif opt in ("-v", "--version") :
	    version()
	    return 0
	else :
	    bug()
    if (action == None) :
	hint("Missing parameter(s)")
	return 1

    # Load DB
    db   = DB()
    tree = db.load(source)

#    tree.dump(" ")

    # Save DB
    db.save(destination, tree)

if __name__ == '__main__' :
    sys.exit(main(sys.argv))
