import elementtree.ElementTree as ET
from   Trace import *
from   Entry import *

# Internal use (XML->Tree)
def fromxml(xml) :
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
    
    j = 0
    for x in xml.getchildren() :
        debug("Working with child")
        tmp = fromxml(x)
        if (tmp != None) :
            entry.child(j, tmp)
            tmp.parent(entry)
            j = j + 1
            
    debug("Returning " + str(entry))
            
    return entry

# Internal use (Tree->XML)
def toxml(tree) :
    return None

class DB :
    def __init__(self) :
	pass

    def load(self, name) :
	xml  = ET.parse(name).getroot()
	return fromxml(xml)

    def save(self, name, tree) :
	xml = toxml(tree)
	xml.write(name)

