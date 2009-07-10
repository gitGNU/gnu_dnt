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

class Entry(Node.Node) :
    def __init__(self,
                 text,
                 priority = Priority.Priority(),
                 start    = Time.Time(),
                 end      = None,
                 comment  = None) :
        super(Entry, self).__init__()
        self.text_set(text)
        self.priority_set(priority)
        self._start_set(start)
        self._end_set(end)
        self._comment_set(comment)
        debug("Entry `" + str(self) + "' created successfully")

    def text_get(self) :
        return self.__text

    def text_set(self, t) :
        assert(t != None)
        assert(isinstance(t, str))
        assert(t != "")

        # Remove leading and trailing whitespaces from input string
        self.__text = string.rstrip(string.lstrip(t))

    text = property(text_get, text_set, None, None)

    def priority_get(self) :
        return self.__priority

    def priority_set(self, p) :
        assert(p != None)
        self.__priority = p

    priority = property(priority_get, priority_set, None, None)

    def start_get(self) :
        return self.__start

    def _start_set(self, t) :
        self.__start = t

    def start_set(self, t) :
        if (t != None) :
            if (self.__end != None) :
                if (t > self.__end) :
                    raise ValueError("start date after end date")
        self._start_set(t)

    start = property(start_get, start_set, None, None)

    def end_get(self) :
        return self.__end

    def _end_set(self, t) :
        self.__end = t

    def end_set(self, t) :
        if (t != None) :
            if (self.__start != None) :
                if (t < self.__start) :
                    raise ValueError("end date before start date")
        self._end_set(t)

    end = property(end_get, end_set, None, None)

    def comment_get(self) :
        return self.__comment

    def _comment_set(self, t) :
        self.__comment = t

    def comment_set(self, t) :
        assert(t != None)
        assert(isinstance(t, str))
        assert(t != "")

        # Remove leading and trailing whitespaces from input string
        self.__comment = string.rstrip(string.lstrip(t))

    comment = property(comment_get, comment_set, None, None)

    def mark_as_done(self) :
        self.__end = Time.Time()

    def mark_as_not_done(self) :
        self.__end = None

    def done_get(self) :
        if (self.__end == None) :
            return False
        if (self.__end <= Time.Time()) :
            return True
        return False

    done = property(done_get, None, None, None)

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
