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

# readline module outputs escapes when imported, delay its import only when
# really needed ...
#import readline

from   Debug      import *
from   Trace      import *
import Exceptions

class Console(object) :
    def __init__(self) :
        pass

    def interact(self, prompt = "", buffer = "", history = []) :
        assert(prompt != None)
        assert(buffer != None)

        self.__buffer = buffer
        self.__prompt = prompt

        import readline

        # Try to clean the history (available in Python >= 2.4)
        try :
            readline.clear_history()
        except :
            pass

        # Fill the history
        if (history != None) :
            debug("History is not empty")
            assert(type(history) == list)
            debug("Filling console history")
            for i in range(0, len(history)) :
                assert(type(history[i]) == str)
                readline.add_history(history[i])

        # Fill the history with buffer
        debug("Filling console buffer")
        readline.set_startup_hook(lambda: readline.insert_text(self.__buffer))
        try :
            self.__buffer = raw_input(self.__prompt)
        except EOFError, e :
            print("")
        except KeyboardInterrupt, e :
            print("")
            self.__buffer = ""
            raise Exceptions.ExplicitExit(e, 1)
        readline.set_startup_hook(None)

#        try :
#            readline.insert_text(self.__buffer)
#            self.__buffer = raw_input(prompt)

        return self.__buffer

    def buffer_get(self) :
        return self.__buffer

    buffer = property(buffer_get, None)

# Test
if (__name__ == '__main__') :
    c = Console()

    debug("Test completed")
    sys.exit(0)
