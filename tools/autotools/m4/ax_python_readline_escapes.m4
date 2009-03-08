##### http://autoconf-archive.cryp.to/ax_python_readline_escapes.html
#
# SYNOPSIS
#
#   AX_PYTHON_READLINE_ESCAPES([ACTION-IF-TRUE],[ACTION-IF-FALSE])
#
# With strange combinations of python, readline and glibc (?) the python
# readline module spits escape sequences at the first print() call. This macro
# looks for those sequences and executes ACTION-IF-TRUE whenever it find the
# combination, executes ACTION-IF-FALSE otherwise
#
# LAST MODIFICATION
#
#   2009-03-08
#
# COPYLEFT
#
#  Copyright (c) 2009 Francesco Salvestrini <salvestrini@users.sourceforge.net>
#
#   This program is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License as
#   published by the Free Software Foundation; either version 2 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#   General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
#   02111-1307, USA.

AC_DEFUN([AX_PYTHON_READLINE_ESCAPES],[
  AC_PREREQ([2.61])
  AC_REQUIRE([AM_PATH_PYTHON])

  AC_MSG_CHECKING([for python/readline unneeded escapes])
  AS_IF([test -n "$PYTHON"],[
      AS_IF([test ! "`$PYTHON -c \"import readline ; print('x')\"`" = "x"],[
        AC_MSG_RESULT([yes])
        $1
      ],[
        AC_MSG_RESULT([no])
        $2
      ])
  ],[
      AC_MSG_ERROR([could not find python interpreter])
  ])
])
