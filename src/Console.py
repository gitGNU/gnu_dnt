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
import readline

from   Debug      import *
from   Trace      import *
import Exceptions

class Console(object) :
    def __init__(self) :
        pass

    def interact(self, buffer = "") :
        assert(buffer != None)
        self.__buffer = buffer

        try :
            prompt = sys.ps1
        except AttributeError :
            try :
                prompt = sys.ps2
            except AttributeError :
                prompt = ">>> "
        assert(prompt != None)

        readline.set_startup_hook(lambda: readline.insert_text(self.__buffer))
        try :
            self.__buffer = raw_input(prompt)
        finally :
            readline.set_startup_hook(None)

#        try :
#            readline.insert_text(self.__buffer)
#            self.__buffer = raw_input(prompt)
#        except EOFError :
#            sys.write("\n")
#        except KeyboardInterrupt :
#            self.__buffer = ""

        return self.__buffer

    def buffer_get(self) :
        return self.__buffer

    buffer = property(buffer_get, None)

# Test
if (__name__ == '__main__') :
    c = Console()

    debug("Test completed")
    sys.exit(0)
