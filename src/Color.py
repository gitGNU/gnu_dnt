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

import sys   # Useless

from   Trace import *

def gray(t) :
    return '\033[1;30m' + t + '\033[1;m'

def red(t) :
    return '\033[1;31m' + t + '\033[1;m'

def green(t) :
    return '\033[1;32m' + t + '\033[1;m'

def yellow(t) :
    return '\033[1;33m' + t + '\033[1;m'

def blue(t) :
    return '\033[1;34m' + t + '\033[1;m'

def magenta(t) :
    return '\033[1;35m' + t + '\033[1;m'

def cyan(t) :
    return '\033[1;36m' + t + '\033[1;m'

def white(t) :
    return '\033[1;37m' + t + '\033[1;m'

def crimson(t) :
    return '\033[1;38m' + t + '\033[1;m'

# '\033[1;41mHighlighted Red like Radish\033[1;m'
# '\033[1;42mHighlighted Green like Grass\033[1;m'
# '\033[1;43mHighlighted Brown like Bear\033[1;m'
# '\033[1;44mHighlighted Blue like Blood\033[1;m'
# '\033[1;45mHighlighted Magenta like Mimosa\033[1;m'
# '\033[1;46mHighlighted Cyan like Caribbean\033[1;m'
# '\033[1;47mHighlighted Gray like Ghost\033[1;m'
# '\033[1;48mHighlighted Crimson like Chianti\033[1;m'

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
