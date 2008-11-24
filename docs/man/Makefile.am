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

dist_man_MANS =					\
	dnt.1					\
	dnt-add.1				\
	dnt-edit.1				\
	dnt-import.1				\
	dnt-init.1				\
	dnt-move.1				\
	dnt-remove.1				\
	dnt-show.1				\
	dnt-touch.1
man_aux       = dnt.x

EXTRA_DIST = $(man_aux)

##
## NOTE:
##     Distributed files should never depend on non-distributed built files
##
dnt.1: $(top_srcdir)/src/dnt.in $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt.1 \
	    $(top_builddir)/src/dnt

dnt-add.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdAdd.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-add.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-add.1 \
	    "$(top_builddir)/src/dnt add"

dnt-edit.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdEdit.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-edit.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-edit.1 \
	    "$(top_builddir)/src/dnt edit"

dnt-import.1: $(top_srcdir)/src/Command.py  $(top_srcdir)/src/cmdImport.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-import.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-import.1 \
	    "$(top_builddir)/src/dnt import"

dnt-init.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdInit.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-init.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-init.1 \
	    "$(top_builddir)/src/dnt init"

dnt-move.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdMove.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-move.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-move.1 \
	    "$(top_builddir)/src/dnt move"

dnt-remove.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdRemove.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-remove.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-remove.1 \
	    "$(top_builddir)/src/dnt remove"

dnt-show.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdShow.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-show.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-show.1 \
	    "$(top_builddir)/src/dnt show"

dnt-touch.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdTouch.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-touch.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-touch.1 \
	    "$(top_builddir)/src/dnt touch"

##
## Maintainer related targets
##
update-local: Makefile

maintainer-check-local: Makefile
