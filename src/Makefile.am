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

bin_SCRIPTS =					\
	dnt

commandsdir = $(pkgvpythondir)/Commands

commands_PYTHON =				\
	Commands/__init__.py			\
	Commands/Add.py				\
	Commands/Config.py			\
	Commands/Edit.py			\
	Commands/Init.py			\
	Commands/Move.py			\
	Commands/Remove.py			\
	Commands/Show.py			\
	Commands/Clean.py			\
	Commands/Touch.py

pkgvpython_PYTHON =				\
	Trace.py				\
	Exceptions.py				\
	Debug.py				\
	Color.py				\
	DB.py					\
	Node.py					\
	Entry.py				\
	ID.py					\
	Command.py

nodist_pkgvpython_PYTHON =			\
	Configuration.py

BUILT_SOURCES =					\
	Configuration.py

## NOTE: The following variable is used by maintainer-check-local target
ALL_PYTHON_SRCS =				\
	$(pkgvpython_PYTHON)			\
	$(nodist_pkgvpython_PYTHON)		\
	$(commands_PYTHON)

EXTRA_DIST =

CLEANFILES =					\
	$(nodist_pkgvpython_PYTHON)		\
	$(bin_SCRIPTS)				\
	*.pyc					\
	Commands/*.pyc

dnt: $(srcdir)/dnt.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/dnt.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
		rm -f $@ $@.tmp ; \
		exit 1 ; \
	}
EXTRA_DIST += dnt.in

Configuration.py: $(srcdir)/Configuration.py.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/Configuration.py.in > $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
		rm -f $@ $@.tmp ; \
		exit 1 ; \
	}
EXTRA_DIST += Configuration.py.in

##
## Local check target
##
check-local: Makefile
	for i in $(pkgvpython_PYTHON) ; do \
		m=`echo $$i | $(SED) -e 's,\.py,,'` && \
		rm -f $$m.pyc && \
		echo $(ECHO_N) "checking module $$m ($$i)... $(ECHO_C)" && \
		PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(srcdir)@PATH_SEPARATOR@$(builddir) $(PYTHON) $(srcdir)/$$i > test.log 2>&1 || { \
			echo "$(ECHO_T)no" ; \
			cat test.log ; \
			exit 1 ; \
		} ; \
		echo "$(ECHO_T)yes" ; \
	done
	for i in $(commands_PYTHON) ; do \
		m=`echo $$i | $(SED) -e 's,\.py,,'` && \
		rm -f $$m.pyc && \
		echo $(ECHO_N) "checking module $$m ($$i)... $(ECHO_C)" && \
		PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(srcdir)@PATH_SEPARATOR@$(builddir) $(PYTHON) $(srcdir)/$$i > test.log 2>&1 || { \
			echo "$(ECHO_T)no" ; \
			cat test.log ; \
			exit 1 ; \
		} ; \
		echo "$(ECHO_T)yes" ; \
	done
	for i in $(nodist_pkgvpython_PYTHON) ; do \
		m=`echo $$i | $(SED) -e 's,\.py,,'` && \
		rm -f $$m.pyc && \
		echo $(ECHO_N) "checking module $$m ($$i)... $(ECHO_C)" && \
		PYTHONPATH=$$PYTHONPATH@PATH_SEPARATOR@$(srcdir)@PATH_SEPARATOR@$(builddir) $(PYTHON) $(builddir)/$$i > test.log 2>&1 || { \
			echo "$(ECHO_T)no" ; \
			cat test.log ; \
			exit 1 ; \
		} ; \
		echo "$(ECHO_T)yes" ; \
	done
	rm -f test.log

CLEANFILES += test.log

##
## XXX FIXME:
##     Replace 'sed' with '$SED' in install-exec-hook and uninstall-hook
##     rules ...
##

## Make versioned links on bin_SCRIPTS.  We only run the transform on the
## root name; then we make a versioned link with the transformed base name.
## This seemed like the most reasonable approach.
install-exec-hook:
	for p in $(bin_SCRIPTS); do \
	  f="`echo $$p|sed '$(transform)'`"; \
	  fv="$$f-$(API_VERSION)"; \
	  cd $(DESTDIR)$(bindir) && \
	  rm -f $$fv && \
	  mv -f $$f $$fv && \
	  $(LN_S) $$fv $$f; \
	done

uninstall-hook:
	for p in $(bin_SCRIPTS); do \
	  f="`echo $$p|sed '$(transform)'`"; \
	  fv="$$f-$(API_VERSION)"; \
	  rm -f $(DESTDIR)$(bindir)/$$fv; \
	done

##
## Maintainer related targets
##
update-local: Makefile

maintainer-check-local: Makefile
	$(WHITESPACE_DETECT) $(ALL_PYTHON_SRCS)
