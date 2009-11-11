# -*- python -*-

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
import string

from   Debug    import *
from   Trace    import *
import Node
import Priority
import Time

#
# XXX FIXME:
#     We should fetch the properies from Node and Entry classes. Only
#     those are the allowed symbols inside a filter (a subset of them
#     all: children and parent should be hidden ...)
#
def help_text() :
    return "text, priority, start, end, " + Node.help_text()

class Entry(Node.Node) :
    def __init__(self,
                 text,
                 priority = Priority.Priority(),
                 start    = Time.Time(),
                 end      = None,
                 comment  = None) :
        super(Entry, self).__init__()
        self.__text_set(text)
        self.__priority_set(priority)
        self.__start_set_raw(start)
        self.__end_set_raw(end)
        self.__comment_set_raw(comment)
        debug("Entry `" + str(self) + "' created successfully")

    def __text_get(self) :
        return self.__text

    def __text_set_raw(self, t) :
        # Remove leading and trailing whitespaces whenever possible
        self.__text = t
        if (isinstance(self.__text, str)) :
            self.__text = string.strip(self.__text)

    # NOTE:
    #   text_set is slightly different from comment_set:
    #   test MUST be a non empty string nor a None ...
    def __text_set(self, t) :
        assert(t != None)
        # Use basestring to perform the test, we could have to deal with
        # unicode characters in user-input
        assert(isinstance(t, basestring))
        assert(t != "")
        self.__text_set_raw(t)

    text = property(__text_get, __text_set, None, None)

    def __priority_get(self) :
        return self.__priority

    def __priority_set(self, p) :
        assert(p != None)
        assert(isinstance(p, Priority.Priority))
        self.__priority = p

    priority = property(__priority_get, __priority_set, None, None)

    def __start_get(self) :
        return self.__start

    def __start_set_raw(self, t) :
        self.__start = t

    def __start_set(self, t) :
        if (t != None) :
            if (self.__end != None) :
                if (t > self.__end) :
                    raise ValueError("start date after end date")
        self.__start_set_raw(t)

    start = property(__start_get, __start_set, None, None)

    def __end_get(self) :
        return self.__end

    def __end_set_raw(self, t) :
        self.__end = t

    def __end_set(self, t) :
        if (t != None) :
            if (self.__start != None) :
                if (t < self.__start) :
                    raise ValueError("end date before start date")
        self.__end_set_raw(t)

    end = property(__end_get, __end_set, None, None)

    def __comment_get(self) :
        return self.__comment

    def __comment_set_raw(self, t) :
        self.__comment = t

    def __comment_set(self, t) :
        tmp = t
        # Use basestring to perform the test, we could have to deal with
        # unicode characters in user-input
        assert((tmp == None) or (isinstance(tmp, basestring)))
        if (isinstance(tmp, str)) :
            # Remove useless whitespaces
            tmp = string.strip(tmp)
            if (tmp == "") :
                # An empty comment means no comment
                tmp = None
        self.__comment_set_raw(tmp)

    comment = property(__comment_get, __comment_set, None, None)

    def mark_as_done(self) :
        self.__end = Time.Time()

    def mark_as_not_done(self) :
        self.__end = None

    def __done_get(self) :
        if (self.__end == None) :
            return False
        if (self.__end <= Time.Time()) :
            return True
        return False

    done = property(__done_get, None, None, None)

    def __str__(self) :
        return '<Entry #%x>' % (id(self))

    def accept(self, visitor) :
        assert(visitor != None)
        assert(hasattr(visitor, "visit"))
        visitor.visit(self)

# Test
if (__name__ == '__main__') :
    root = Entry("root")
    e1   = Entry("e1")
    e11  = Entry("e11")
    e12  = Entry("e12")
    e2   = Entry("e2")

    root.add(e1)
    root.add(e2)
    e1.add(e12)
    e1.add(e11)

    # NOTE:
    #     We should not use Visitor class (which could use Entry and/or Node
    #     class
    class TestVisitor(object) :
        def visit(self, e) :
            debug("Visiting entry " + str(e))
            for j in e.children :
                j.accept(self) # Re-accept myself

    v = TestVisitor()
    root.accept(v)

    e3 = Entry("test")
    e3.end = e3.start
    assert(e3.done)

#    e3.end   = e3.start
#    e3.start = e3.start - 1
#    assert(not(e3.done))

    debug("Test completed")
    sys.exit(0)
