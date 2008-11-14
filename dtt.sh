#!/usr/bin/python

import os
import sys
import traceback
import getopt
import datetime
import pprint
import re
from   xml.sax import saxutils, handler, make_parser

PACKAGE_NAME    = "Development Tracking Tool"
PACKAGE_VERSION = "0.1"
PROGRAM_NAME    = "dtt"

class Node :
    __parent   = None
    __children = []

    def parent(self) :
	return self.__parent

    def parent(self, p) :
	self.__parent = p

    def children(self) :
	return self.__children

    def children(self, i, p) :
	self.__children[p]


class Entry(Node) :
    def __init__(self) :
	self.title_    = ""
	self.note_     = ""
	self.priority_ = 0
	self.time_     = datetime.date.today()

    def __repr__(self) :
	return '<Entry %#x `%s\'>' %(id(self), self.title_)

    def title(self) :
	return self.title_
    def title(self, p) :
	# Remove leading and trailing whitespaces
	#        assert(p != None)
	#	self.title_ = re.match(r'^[ \t]*(.*)[ \t]*$', p).group(1)
	self.title_ = p

    def note(self) :
	return self.note_
    def note(self, p) :
	# Remove leading and trailing whitespaces
	#        assert(p != None)
	#	self.title_ = re.match(r'^[ \t]*(.*)[ \t]*$', p).group(1)
	self.title_ = p

    def priority(self) :
	return self.priority_
    def priority(self, p) :
	self.priority_ = p

    def time(self) :
	return self.time_
    def time(self, p) :
	self.time_ = p

class Stack :
    __data = []

    def push(self, p) :
	self.__data.append(p)

    def pop(self) :
	result = self.__data[-1]
	del self.__data[-1]
	return result

    def head(self) :
	return self.__data[-1]

    def size(self) :
	return len(self.__data)

class DBHelper(handler.ContentHandler) :
    text_   = ""
    tree_   = None
    stack_  = Stack()

    def __init__(self, t) :
	self.tree_ = t

    def startDocument(self) :
	pass

    def endDocument(self) :
	assert(self.stack_.size() == 0)

    def startElement(self, name, attrs) :
	debug("start-element(" + name + ")")

	if (name != "note") :
	    return

	node = Entry()
	self.stack_.push(node)

	for attr in attrs.keys() :
	    if (attr == "time") :
		node.time(attrs[attr])
	    elif (attr == "priority") :
		node.priority(attrs[attr])
	    else :
		warning("Skipping unknown attribute `" + attrs[attr] + "'")

	debug("start-element(" + attr + ", " + str(self.stack_.size()) + ")")

    def endElement(self, name) :
	debug("stop-element(" + name + ", " + str(self.stack_.size()) + ")")

	if (name != "note") :
	    return

	self.stack_.head().title(self.text_)
	self.text_ = ""
	self.stack_.pop()

    def characters(self, chars) :
	self.text_ = self.text_ + chars

class DB :
    __tree = None

    def __init__(self) :
	self.__tree = Entry()

    def load(self, s) :
	parser = make_parser()
	parser.setContentHandler(DBHelper(self.__tree))
	parser.parse(s)
	return self.__tree

    def save(self, s) :
	return True

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

    # Execute requested operation
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint(tree)

    # Save DB
    db.save(destination)

if __name__ == '__main__' :
    sys.exit(main(sys.argv))
