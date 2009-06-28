#
# Copyright (C) 2008, 2009 Francesco Salvestrini
#                          Alessandro Massignan
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
import string
import re

from   Debug      import *
from   Trace      import *
import Entry
import Exceptions

#
# XXX FIXME:
#     We should fetch the properies from Node and Entry classes. Only
#     those are the allowed symbols inside a filter (a subset of them
#     all: children and parent should be hidden ...)
#
#     Please update the description ASAP !!!
#
def help() :
    return "Recognized filters are: all, done, not-done"

class Filter(object) :
    def __init__(self, s = None) :
        if ((s == None) or (s == "")) :
            self.__expression = "1"
        else :
            self.__expression = s
        assert(self.__expression != None)

    def _transform(self, input, pfx) :
        tmp = input

        assert(tmp != None)
        assert(pfx != None)

        #
        # XXX FIXME:
        #     These are weak regexp because we could find
        #     matching string inside a quoted string
        #
        # XXX FIXME:
        #     Patterns are hand-written, we should find a way to
        #     autocompute them all (from Node and Entry properties)
        #     The proposed task is not straightforward because we
        #     should not allow children or parent node property
        #     access ...
        #

        # Spitting by quoted strings matches
        split1 = re.split(r'([\"\'][^\'\"]*[\"\'])+', tmp)

        # Splitting by non-word matches
        result = ""

        for i in split1 :
            if (re.match('^\s+$', i)) :
                continue

            i = re.sub('^\s+', '', i)
            i = re.sub('\s+$', '', i)

            if (re.match('^[\"\'].*[\"\']$', i)) :
                # Quoted string
                result += i
            else :
                split2 = re.split('(\W+)', i)

                for j in split2 :
                    if (re.match('^\s+$', j)) :
                        continue

                    j = re.sub('^\s*', '', j)
                    j = re.sub('\s*$', '', j)

                    if (re.match('not|and|or|'        +
                                 'is\s+not|is|!=|==|' +
                                 '>|<|>=|<=', j)) :
                        # Operator
                        result += ' ' + j + ' '
                    elif(re.match('all', j)) :
                        # Special case
                        result += '1'
                    elif (re.match('[A-Za-z_][A-Za-z0-9_]*', j)) :
                        # Identifier
                        result += 'node.' + j
                    elif (re.match('-?[0-9]+', j)) :
                        # Integer value
                        result += j
                    elif (re.match('\(|\)', j)) :
                        # Parentheses
                        result += j
                    else :
                        raise Exceptions.InvalidExpression(tmp)

        return result

    def evaluate(self, node) :
        assert(self.__expression != None)
        assert(node != None)

        tmp = node
        fnc = self._transform(self.__expression, "tmp")

        ret = False
        try :
            ret = eval(fnc, locals())
        except :
            raise Exceptions.InvalidExpression(self.__expression)

        return ret

# Test
if (__name__ == '__main__') :
    #
    # XXX FIXME:
    #     We should evaluate all the checks over a tree or a node
    #     Please fix ASAP !!!

    v = Filter()
    assert(v != None)
    v = Filter("all")
    assert(v != None)
    v = Filter("done")
    assert(v != None)
    v = Filter("not done")
    assert(v != None)
    v = Filter("all,done,not done")
    assert(v != None)
    v = Filter("all, done, ~done")
    assert(v != None)
    v = Filter("all ,done ,not done")
    assert(v != None)
    v = Filter("all , done , ~ done")
    assert(v != None)
    v = Filter("all  ,  done  ,  ~ done")
    assert(v != None)
    v = Filter("all   ,   done   ,   ~ done")
    assert(v != None)
    v = Filter("all    ,    done    ,    ~    done")
    assert(v != None)

    debug("Test completed")
    sys.exit(0)
