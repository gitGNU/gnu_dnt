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
            # XXX FIXME: ugly as hell
            s = "1 == 1"

        self.__original   =  s
        self.__expression = self._transform(self.__original, "node")

        assert(self.__expression != None)

    def _transform_part(self, input, prefix) :
        assert(input  != None)
        assert(isinstance(input, list))
        assert(prefix != None)
        assert(prefix != "")

        tmp = input

        debug("Transforming filter (recursive) " +
              "`" + str(tmp) + "'")

        # Remove leading/trailing whites
        tmp = map(lambda x:
                      string.rstrip(string.lstrip(x)),
                  tmp)
        debug("Mangled representation (pass #B.1) is: " +
              "`" + str(tmp) + "'")

        # Filter-out whitespaces and empty strings
        tmp = filter(lambda x:
                         len(x) != 0 and not(x.isspace()),
                     tmp)

        debug("Mangled representation (pass #B.2) is: " +
              "`" + str(tmp) + "'")

        result = []

        # Perform tokens check
        for i in tmp :
            debug("Iterating over `" + i + "'")

            debug("Looking for a match against `" + i + "'")
            if (i == "not" or
                i == "and" or
                i == "or"  or
                i == "!="  or
                i == "=="  or
                i == ">"   or
                i == "<"   or
                i == ">="  or
                i == "<="  or
                i == ",") :
                # Got an operator
                debug("Got operator/separator `" + i + "'")
                result.append(i)
            elif (re.match('\(+', i) or
                  re.match('\)+', i)) :
                # Got paren(s)
                debug("Got paren(s) `" + i + "'")
                result.append(i)
            elif (re.match('all', i)) :
                # Special case
                debug("Got special case `" + i + "'")
                # XXX FIXME: ugly as hell
                result.append("1 == 1")
            elif (re.match('[_A-Za-z][_A-Za-z0-9]*', i)) :
                # Got an identifier, add the requested prefix
                debug("Got identifier  `" + i + "'")
                result.append(prefix + '.' + i)
            elif (re.match('[+-]?[0-9]+', i)) :
                # Got an integer
                debug("Got integer `" + i + "'")
                result.append(i)
            else :
                raise Exceptions.InvalidToken(i)

        debug("Returning from recursion `" + str(result) + "'")
        return result

    def _transform(self, input, prefix) :
        assert(type(input)  == str)
        assert(isinstance(prefix, str))
        assert(prefix != "")

        debug("Transforming filter `" + input + "'")

        #
        # NOTE:
        #     We are going to split by quoted strings, in order
        #     to avoid mangling quoted and non-quoted string.
        #     We must rearrange the non-quoted ones ...
        #
        tmp = re.split(r'([\"\'][^\'\"]*[\"\'])+', input)
        debug("Mangled representation (pass #A.1) is: " +
              "`" + str(tmp) + "'")

        result = ""

        for i in tmp :
            debug("Handling `" + i + "'")

            if (re.match('^[\"\'].*[\"\']$', i)) :
                # This is a quoted string, keep as it is
                debug("Keeping quoted string `" + i + "' as it is")
                result += i
            else :
                # Perform word and spaces splitting, and symbol
                # mangling on the remaining junk
                tmp1 = i
                tmp1 = re.split(r'(\W+)', tmp1)
                debug("Mangled representation (pass #A.2) is: " +
                      "`" + str(tmp1) + "'")

                tmp2 = [ ]
                for t in tmp1 :
                    if (re.match(r'.*\s.*', t)) :
                        tmp2.extend(re.split(r'\s+', t))
                    else :
                        tmp2.append(t)

                debug("Mangled representation (pass #A.3) is: " +
                      "`" + str(tmp2) + "'")

                try :
                    tmp3 = self._transform_part(tmp2, prefix)
                except Exceptions.InvalidToken, e:
                    # We have a more specific exception to raise ...
                    raise e
                except Exception, e:
                    raise Exceptions.InvalidExpression(str(e))

                debug("Mangled representation (pass #A.4) is: " +
                      "`" + str(tmp3) + "'")

                result += string.join(tmp3, " ")

            debug("Result is now `" + result + "'")

        assert(result != None)

        debug("Resulting filter is `" + result + "'")
        return result

    #
    # NOTE:
    #     Due to eval() and the transformation performed on __init__ we must
    #     have the 'node' variable.
    #
    # XXX FIXME:
    #     Find a better way to handle this task
    #
    def evaluate(self, node) :
        assert(self.__expression != None)
        assert(node != None)

        debug("Evaluating filter expression " +
              "`" + self.__expression + "' "  +
              "over node `" + str(node) + "'")

        ret = False # Useless
        try :
            debug("Evaluating expression `" + self.__expression + "'")
            ret = eval(self.__expression, locals())
        except :
            raise Exceptions.InvalidExpression(self.__original)

        # The evaluation result must be boolean
        if (type(ret) != bool) :
            raise Exceptions.InvalidExpressionType(self.__original)

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
    v = Filter("all and done and not done")
    assert(v != None)
    v = Filter("all and done and not done")
    assert(v != None)
    v = Filter("all or done or not done")
    assert(v != None)
    v = Filter("all and done and not done")
    assert(v != None)
    v = Filter("all  and  done  and  not done")
    assert(v != None)
    v = Filter("all   and   done   and   not done")
    assert(v != None)
    v = Filter("all    and    done    and    not    done")
    assert(v != None)

    v = Filter("done")
    assert(v != None)
    v = Filter("not(done)")
    assert(v != None)
    v = Filter("not(not(done))")
    assert(v != None)
    v = Filter("not(not(not(done)))")
    assert(v != None)
    v = Filter("not(not(not(done)))")
    assert(v != None)
    v = Filter("not( not(not(done)))")
    assert(v != None)
    v = Filter("not( not(  not(done)))")
    assert(v != None)
    v = Filter("not( not(  not(   done)))")
    assert(v != None)
    v = Filter("not( not(  not(   done ) ) )")
    assert(v != None)

    debug("Test completed")
    sys.exit(0)
