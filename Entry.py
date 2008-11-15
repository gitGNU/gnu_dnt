import datetime
from   Trace import *

class Node :
    __parent   = None
    __children = []
    __index    = 0

    def __init__(self, p = None, c = []) :
        debug("Node " + str(self) + " created successfully !!!!")
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
        if (self.__parent != None) :
            debug("Changing node parent !!!!!!!")
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
        Node.__init__(self)
	self.__title    = title
	self.__note     = note
	self.__priority = priority
	self.__time     = time
        debug("Entry " + str(self) + " created successfully !!!!")

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
