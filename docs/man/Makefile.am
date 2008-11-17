##
## Input file for automake
##
## Copyright (C) 2007, 2008 Francesco Salvestrini
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program; if not, write to the Free Software Foundation, Inc.,
## 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
##

include $(top_srcdir)/Makefile.sub

dist_man_MANS = dtt.1
man_aux       = dtt.x

EXTRA_DIST = $(man_aux)

##
## NOTE:
##     Distributed files should never depend on non-distributed built files
##
dtt.1: $(top_srcdir)/src/dtt.in $(top_srcdir)/configure.ac
	$(HELP2MAN) \
	    --include=$(srcdir)/dtt.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dtt.1 \
	    $(top_builddir)/src/dtt$(EXEEXT)

##
## Maintainer related targets
##
update-local: Makefile

maintainer-check-local: Makefile