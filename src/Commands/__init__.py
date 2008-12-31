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

from Trace import *

try :
    import Init
    import Clean
    import Config
    import Add
    import Edit
    import Fix
    import Move
    import Remove
    import Show
    import Dump
    import Touch
    import Done
except ImportError :
    # XXX FIXME: Add better error reporting ....
    print("Cannot import package's commands ...")
    sys.exit(-1)

commands = {
    'init'   : { 'description' : Init.description,
                 'do'          : Init.do,
                 'authors'     : Init.authors        },

    'clean'  : { 'description' : Clean.description,
                 'do'          : Clean.do,
                 'authors'     : Clean.authors       },

    'add'    : { 'description' : Add.description,
                 'do'          : Add.do,
                 'authors'     : Add.authors         },

    'config' : { 'description' : Config.description,
                 'do'          : Config.do,
                 'authors'     : Config.authors      },

    'edit'   : { 'description' : Edit.description,
                 'do'          : Edit.do,
                 'authors'     : Edit.authors        },

    'fix'    : { 'description' : Fix.description,
                 'do'          : Fix.do,
                 'authors'     : Fix.authors         },

    'move'   : { 'description' : Move.description,
                 'do'          : Move.do,
                 'authors'     : Move.authors        },

    'remove' : { 'description' : Remove.description,
                 'do'          : Remove.do,
                 'authors'     : Remove.authors      },

    'show'   : { 'description' : Show.description,
                 'do'          : Show.do,
                 'authors'     : Show.authors        },

    'dump'   : { 'description' : Dump.description,
                 'do'          : Dump.do,
                 'authors'     : Dump.authors        },

    'touch'  : { 'description' : Touch.description,
                 'do'          : Touch.do,
                 'authors'     : Touch.authors       },

    'done'   : { 'description' : Done.description,
                 'do'          : Done.do,
                 'authors'     : Done.authors        },
    }

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
