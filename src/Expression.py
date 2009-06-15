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
import Exceptions
import ply.lex as lex
import ply.yacc as yacc

class Expression(object) :
    def __init__(self, s = "") :
        self.__function = self._parse(s)
        assert(self.__function != None)

    def _parse(self, s) :
        assert(self != None)
        assert(s != None)

        debug("Building lexer")

        tokens = (
            'IDENTIFIER',
            'AND', 'OR',
            'SPACES'
            )

        def t_IDENTIFIER(t) :
            r'[A-Za-z_][A-Za-z0-9_-]*'
            return t

        def t_AND(t) :
            r'\&|,'
            t.value = "and"
            return t

        def t_OR(t) :
            r'\|'
            t.value = "or"
            return t

        def t_SPACES(t) :
            r'\s+'
            t.lexer.skip(len(t.value[0]) - 1)

        def t_error(t) :
            raise Exceptions.InvalidToken(t.value[0])

        lex.lex()

        precedence = ( )

        def p_expression(t) :
            '''expression : identifier
                          | identifier operator expression'''
            if (len(t) == 4) :
                if (t[2] == "and") :
                    tmp = lambda x, y: x and y
                elif (t[2] == "or") :
                    tmp = lambda x, y: x or y
                else :
                    raise Exceptions.InvalidSyntax(s)
            elif (len(t) == 2) :
                tmp = t[1]

            assert(tmp != None)
            t[0] = tmp
            return t[0]

        def p_identifier(t) :
            'identifier : IDENTIFIER'
            tmp = None

            if (t[1] == "all") :
                tmp = lambda x: True
            elif (t[1] == "done") :
                tmp = lambda x: x.done()
            elif (t[1] == "not-done") :
                tmp = lambda x: not(x.done())
            else :
                raise Exceptions.InvalidSyntax(s)

            assert(tmp != None)
            t[0] = tmp

        def p_operator(t) :
            '''operator : AND
                        | OR'''
            t[0] = t[1]

        def p_error(t) :
            raise Exceptions.InvalidSyntax(s)

        yacc.yacc()

        debug("Parsing expression `" + str(s) + "'")

        # Avoiding unnecessary debugging files
        yacc.yacc(debug=0)
        yacc.yacc(write_tables=0)

        tmp = yacc.parse(s)
        assert(tmp != None)

        return tmp

    def function_get(self) :
        assert(self.__function != None)
        return self.__function

    function = property(function_get, None)

# Test
if (__name__ == '__main__') :

    v = Expression("all")
    assert(v != None)
    v = Expression("done")
    assert(v != None)
    v = Expression("not-done")
    assert(v != None)
    v = Expression("all,done,not-done")
    assert(v != None)
    v = Expression("all, done, not-done")
    assert(v != None)
    v = Expression("all ,done ,not-done")
    assert(v != None)
    v = Expression("all , done , not-done")
    assert(v != None)
    v = Expression("all  ,  done  ,  not-done")
    assert(v != None)
    v = Expression("all   ,   done   ,   not-done")
    assert(v != None)
    v = Expression("all    ,    done    ,    not-done")
    assert(v != None)

#    # The following tests should PASS
#    try :
#        expression = Expression()
#        assert(expression != None)
#
#        expression = Expression("")
#        assert(expression != None)
#
#        expression = Expression("x and y")
#        assert(expression != None)
#
#        expression = Expression("x and y and z")
#        assert(expression != None)
#
#        expression = Expression("((x and y and z))")
#
#        expression = Expression("(x and (y and z))")
#
#        expression = Expression("x or y")
#        assert(expression != None)
#
#        expression = Expression("x or y or z")
#        assert(expression != None)
#
#        expression = Expression("(x or y)")
#        assert(expression != None)
#
#        expression = Expression("((x or y) or z)")
#        assert(expression != None)
#
#        expression = Expression("(x or (y or z))")
#        assert(expression != None)
#
#        expression = Expression("((x or (y or z)) and a) and b")
#        assert(expression != None)
#
#    except :
#        sys.exit(1)
#
#    # The following tests should FAIL
#    try :
#        expression = Expression("and and")
#        assert(expression != None)
#
#        expression = Expression("or")
#        assert(expression != None)
#
#        expression = Expression("x and")
#        assert(expression != None)
#
#        expression = Expression("x and")
#        assert(expression != None)
#
#    except :
#        sys.exit(1)

    debug("Test completed")
    sys.exit(0)
