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
	dnt-clean.1				\
	dnt-config.1				\
	dnt-dump.1				\
	dnt-edit.1				\
	dnt-init.1				\
	dnt-move.1				\
	dnt-remove.1				\
	dnt-show.1				\
	dnt-touch.1

man_aux       = dnt.x				\
		dnt-add.x			\
		dnt-clean.x			\
		dnt-config.x			\
		dnt-dump.x			\
		dnt-edit.x			\
		dnt-init.x			\
		dnt-move.x			\
		dnt-remove.x			\
		dnt-show.x			\
		dnt-touch.x

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

dnt-add.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/Commands/Add.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-add.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-add.1 \
	    "$(top_builddir)/src/dnt add"

dnt-clean.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/Commands/Clean.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-clean.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-clean.1 \
	    "$(top_builddir)/src/dnt clean"

dnt-config.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/Commands/Config.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-config.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-config.1 \
	    "$(top_builddir)/src/dnt config"

dnt-dump.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/Commands/Dump.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-dump.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-dump.1 \
	    "$(top_builddir)/src/dnt dump"

dnt-edit.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/Commands/Edit.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-edit.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-edit.1 \
	    "$(top_builddir)/src/dnt edit"

dnt-init.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/Commands/Init.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-init.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-init.1 \
	    "$(top_builddir)/src/dnt init"

dnt-move.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/Commands/Move.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-move.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-move.1 \
	    "$(top_builddir)/src/dnt move"

dnt-remove.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/Commands/Remove.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-remove.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-remove.1 \
	    "$(top_builddir)/src/dnt remove"

dnt-show.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/Commands/Show.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-show.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-show.1 \
	    "$(top_builddir)/src/dnt show"

dnt-touch.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/Commands/Touch.py $(top_srcdir)/configure.ac
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
