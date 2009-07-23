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
import re
import textwrap

from   Debug import *
from   Trace import *
import Exceptions

# NOTE:
#     See http://en.wikipedia.org/wiki/ANSI_escape_code for a detailed
#     description

_color_codes = [ "30", "31", "32", "33", "34", "35", "36", "37", "38" ]

COLOR_IDX_BLACK   = 0
COLOR_IDX_RED     = 1
COLOR_IDX_GREEN   = 2
COLOR_IDX_YELLOW  = 3
COLOR_IDX_BLUE    = 4
COLOR_IDX_MAGENTA = 5
COLOR_IDX_CYAN    = 6
COLOR_IDX_WHITE   = 7

color_enabled = True

def _bright(color, text) :
    t = None
    if (color_enabled is True) :
        try :
            t = '\033[1;' + _color_codes[color] + 'm' + text + '\033[1;m'
        #    except IndexError, e :
        #        t = text
        except Exception, e:
            bug(str(e))
    else :
        t = text
    assert(t != None)
    return t

def _normal(color, text) :
    t = None
    if (color_enabled is True) :
        try :
            t = '\033[' + _color_codes[color] + 'm' + text + '\033[m'
        #    except IndexError, e :
        #        t = text
        except Exception, e:
            bug(str(e))
    else :
        t = text
    assert(t != None)
    return t

def bright_red(t) :
    return _bright(COLOR_IDX_RED, t)
def normal_red(t) :
    return _normal(COLOR_IDX_RED, t)

def bright_green(t) :
    return _bright(COLOR_IDX_GREEN, t)
def normal_green(t) :
    return _normal(COLOR_IDX_GREEN, t)

def bright_yellow(t) :
    return _bright(COLOR_IDX_YELLOW, t)
def normal_yellow(t) :
    return _normal(COLOR_IDX_YELLOW, t)

def bright_blue(t) :
    return _bright(COLOR_IDX_BLUE, t)
def normal_blue(t) :
    return _normal(COLOR_IDX_BLUE, t)

def bright_magenta(t) :
    return _bright(COLOR_IDX_MAGENTA, t)
def normal_magenta(t) :
    return _normal(COLOR_IDX_MAGENTA, t)

def bright_cyan(t) :
    return _bright(COLOR_IDX_CYAN, t)
def normal_cyan(t) :
    return _normal(COLOR_IDX_CYAN, t)

def bright_white(t) :
    return _bright(COLOR_IDX_WHITE, t)
def normal_white(t) :
    return _normal(COLOR_IDX_WHITE, t)

def wrap(t, w) :
    assert(t != None)
    assert(w > 0)

    result        = [ ]
    buffer        = ''
    buffer_length = 0
    re_ansi       = re.compile(r'(' + chr(27) + '\[[0-9;]*[m]' + r')')

    # Split over ansi sequences
    for i in re_ansi.split(t) :

        if re_ansi.match(i) :
            buffer += i
        else :

            # Split over chars
            for j in i :

                if (buffer_length + 1) > w :

                    if re.match(r'^\s+('        +
                                chr(27)         +
                                '\[[0-9;]*[m]'  +
                                r')+$', buffer) :
                        # Special case: spaces preceding ANSI
                        # escapes should be clean from the buffer
                        # if we reach wrap's width
                        buffer = re.sub(r'^\s+', '', buffer)
                        buffer += j
                        buffer_length = 1
                    elif re.match(r'^\s*$', buffer) :
                        # An empty line? Don't output it.
                        buffer = re.sub(r'\s*$', '', buffer)
                        buffer         += j
                        buffer_length  += 1
                    else :
                        # Clean trailing spaces and append to result
                        buffer = re.sub(r'\s+$', '', buffer)
                        result.append(buffer)
                        buffer         = j
                        buffer_length  = 1
                else :
                    buffer        += j
                    buffer_length += 1

    # Append the crumbs to result
    if len(buffer) > 0  :
        buffer = re.sub(r'\s+$', '', buffer)
        result.append(buffer)

    return result

# Test
if (__name__ == '__main__') :

    # Preliminary checks
    assert(textwrap.wrap("test", 1) == wrap("test", 1))
    assert(textwrap.wrap("test", 2) == wrap("test", 2))
    assert(textwrap.wrap("test", 3) == wrap("test", 3))
    assert(textwrap.wrap("test", 4) == wrap("test", 4))
    assert(textwrap.wrap("test", 5) == wrap("test", 5))

    # Extensive checks to ensure that
    #
    #     textwrap.wrap() == ANSI.textwrap()
    #
    # On non-ANSI input
    x = [ "this",
          "this is",
          "this is a",
          "this is a test",

          " this",
          "this ",

          "  this",
          "this  ",

          "  this is",
          "this is  ",

          "  this  is",
          "this  is  ",

          "  this   is",
          "this   is  ",

          "     this     is      a         test",
          "this   is   a     test     ",
          "         this   is   a     test     "
          ]

    for i in range(0, len(x)) :
        print("x[" + str(i) + "] = '" + x[i] + "'")
        for j in range (1, len(x[i]) + 1) :
            print("wrap " + str(j))
            print(str(textwrap.wrap(x[i], j)))
            print(str(wrap(x[i], j)))
            assert(textwrap.wrap(x[i], j) == wrap(x[i], j))

    debug("Test completed")
    sys.exit(0)
