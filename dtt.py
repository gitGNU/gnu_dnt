#!/usr/bin/python

import sys
import getopt
import xml.dom.minidom

class Entry :
    name_     = ""
    parent_   = None
    children_ = 

    def name():
        return name_

if __name__ == '__main__' :
    # Parse command line
    try :
        opts, args = getopt.getopt(sys.argv[1:],
                                   "a:r:e:R:hv",
                                   ["add=",
                                    "remove=",
                                    "edit=",
                                    "reparent=",
                                    "help",
                                    "version"])
    except :
        hint("Parameters error")
        sys.exit(1)
    for opt, arg in opts :
        if opt in ("a", "add") :
            elif opt in ("r", "remove") :
                elif opt in ("e", "edit") :
                    elif opt in ("r", "reparent") :
                        elif opt in ("h", "help") :
                            elif opt in ("v", "version") :
                                else :

    # Load DB
    # Execute requested operation
    # Save DB

sys.exit(0)
