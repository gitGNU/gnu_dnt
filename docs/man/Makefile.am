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
	dtt.1					\
	dtt-add.1				\
	dtt-edit.1				\
	dtt-import.1				\
	dtt-init.1				\
	dtt-move.1				\
	dtt-remove.1				\
	dtt-show.1				\
	dtt-touch.1
man_aux       = dtt.x

EXTRA_DIST = $(man_aux)

##
## NOTE:
##     Distributed files should never depend on non-distributed built files
##
dtt.1: $(top_srcdir)/src/dtt.in $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dtt.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dtt.1 \
	    $(top_builddir)/src/dtt

dtt-add.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdAdd.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dtt-add.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dtt-add.1 \
	    "$(top_builddir)/src/dtt add"

dtt-edit.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdEdit.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dtt-edit.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dtt-edit.1 \
	    "$(top_builddir)/src/dtt edit"

dtt-import.1: $(top_srcdir)/src/Command.py  $(top_srcdir)/src/cmdImport.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dtt-import.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dtt-import.1 \
	    "$(top_builddir)/src/dtt import"

dtt-init.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdInit.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dtt-init.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dtt-init.1 \
	    "$(top_builddir)/src/dtt init"

dtt-move.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdMove.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dtt-move.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dtt-move.1 \
	    "$(top_builddir)/src/dtt move"

dtt-remove.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdRemove.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dtt-remove.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dtt-remove.1 \
	    "$(top_builddir)/src/dtt remove"

dtt-show.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdShow.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dtt-show.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dtt-show.1 \
	    "$(top_builddir)/src/dtt show"

dtt-touch.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/cmdTouch.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dtt-touch.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dtt-touch.1 \
	    "$(top_builddir)/src/dtt touch"

##
## Maintainer related targets
##
update-local: Makefile

maintainer-check-local: Makefile
