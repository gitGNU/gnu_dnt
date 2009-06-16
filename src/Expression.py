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

from   Debug       import *
from   Trace       import *
import Exceptions
import ply.lex  as lex
import ply.yacc as yacc

class Expression(object) :
    def __init__(self, s = "") :
        self.__function = self._parse(s)
        assert(self.__function != None)

    def _parse(self, s) :
        assert(self != None)
        assert(s != None)

        debug("Building lexer")

        reserved = {
            'not' : 'NOT',
            }

        tokens = [ 'IDENTIFIER',
                   'AND',
                   'OR'
                   ] + list(reserved.values())

        t_AND    = r'\&|,'
        t_OR     = r'\|'
        t_NOT    = r'~'

        def t_IDENTIFIER(t) :
            r'[A-Za-z_][A-Za-z0-9_-]*'
            t.type = reserved.get(t.value,'IDENTIFIER')
            return t

        t_ignore = ' \t\n\v\r\b'

        def t_error(t) :
            raise Exceptions.InvalidToken(t.value[0])

        lex.lex()

        debug("Building parser")

        precedence = (
            ('left', 'AND', 'OR'),
            ('right', 'NOT'),
            )

        def p_expression_identifier(t) :
            'expression : identifier'
            t[0] = t[1]
            assert(t[0] != None)

        def p_expression_not(t) :
            'expression : NOT expression'
            t[0] = lambda x : not(t[2](x))
            assert(t[0] != None)

        def p_expression_and(t) :
            'expression : expression AND expression'
            t[0] = lambda x : t[1](x) and t[3](x)
            assert(t[0] != None)

        def p_expression_or(t) :
            'expression : expression OR expression'
            t[0] = lambda x : t[1](x) or t[3](x)
            assert(t[0] != None)

        def p_identifier(t) :
            'identifier : IDENTIFIER'
            tmp = None

            if (t[1] == "all") :
                tmp = lambda x: True
            elif (t[1] == "done") :
                tmp = lambda x: x.done()
            else :
                raise Exceptions.InvalidIdentifier(t[1])

            assert(tmp != None)
            t[0] = tmp

        def p_error(t) :
            raise Exceptions.InvalidSyntax(s)

        # Avoiding unnecessary debugging files
        yacc.yacc(debug = 0, write_tables = 0)

        debug("Parsing expression `" + str(s) + "'")

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
    v = Expression("not done")
    assert(v != None)
    v = Expression("all,done,not done")
    assert(v != None)
    v = Expression("all, done, ~done")
    assert(v != None)
    v = Expression("all ,done ,not done")
    assert(v != None)
    v = Expression("all , done , ~ done")
    assert(v != None)
    v = Expression("all  ,  done  ,  ~ done")
    assert(v != None)
    v = Expression("all   ,   done   ,   ~ done")
    assert(v != None)
    v = Expression("all    ,    done    ,    ~    done")
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
