##
## Input file for automake
##
## Copyright (C) 2008, 2009 Francesco Salvestrini
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
	devtodo-to-dnt.1			\
	dnt-to-devtodo.1			\
	dnt.1					\
	dnt-add.1				\
	dnt-clean.1				\
	dnt-config.1				\
	dnt-edit.1				\
	dnt-fix.1				\
	dnt-init.1				\
	dnt-move.1				\
	dnt-remove.1				\
	dnt-mark.1				\
	dnt-show.1

man_aux       =					\
	devtodo-to-dnt.x			\
	dnt-to-devtodo.x			\
	dnt.x					\
	dnt-add.x				\
	dnt-clean.x				\
	dnt-config.x				\
	dnt-edit.x				\
	dnt-fix.x				\
	dnt-init.x				\
	dnt-move.x				\
	dnt-remove.x				\
	dnt-mark.x				\
	dnt-show.x

EXTRA_DIST = $(man_aux)

##
## NOTE:
##     Distributed files should never depend on non-distributed built files
##
dnt-to-devtodo.1: $(top_srcdir)/src/dnt-to-devtodo.in $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-to-devtodo.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-to-devtodo.1 \
	    $(top_builddir)/src/dnt-to-devtodo

devtodo-to-dnt.1: $(top_srcdir)/src/devtodo-to-dnt.in $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/devtodo-to-dnt.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=devtodo-to-dnt.1 \
	    $(top_builddir)/src/devtodo-to-dnt

dnt.1: $(top_srcdir)/src/dnt.in $(top_srcdir)/src/Command.py $(top_srcdir)/configure.ac
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

dnt-fix.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/Commands/Fix.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-fix.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-fix.1 \
	    "$(top_builddir)/src/dnt fix"

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

dnt-mark.1: $(top_srcdir)/src/Command.py $(top_srcdir)/src/Commands/Mark.py $(top_srcdir)/configure.ac
	PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(abs_top_srcdir)/src@PATH_SEPARATOR@$(abs_top_builddir)/src ; \
	export PYTHONPATH ; \
	$(HELP2MAN) \
	    --include=$(srcdir)/dnt-mark.x \
	    --source="@PACKAGE_NAME@" \
	    --manual="User Commands" \
	    --section=1	\
	    --output=dnt-mark.1 \
	    "$(top_builddir)/src/dnt mark"

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

##
## Maintainer related targets
##
update-local: Makefile

maintainer-check-local: Makefile
