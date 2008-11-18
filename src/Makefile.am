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
	dtt

pythonlibdir = $(pkgvlibsdir)/python/DTT

dist_pythonlib_DATA =				\
	Color.py				\
	DB.py					\
	Debug.py				\
	Entry.py				\
	Node.py					\
	Options.py				\
	Trace.py

nodist_pythonlib_DATA =				\
	Config.py

CLEANFILES = $(nodist_pythonlib_DATA) $(bin_SCRIPTS) $(pkgvbin_SCRIPTS)

Config.py: Makefile $(srcdir)/Config.py.in
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/Config.py.in > $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
		rm -f $@ $@.tmp ; \
		exit 1 ; \
	}

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

DTT_PYTHON_SRCS =				\
        dtt.in

DTT_SRCS = $(DTT_PYTHON_SRCS)

EXTRA_DIST = $(DTT_SRCS)

dtt: $(srcdir)/dtt.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/dtt.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
		rm -f $@ $@.tmp ; \
		exit 1 ; \
	}

##
## Maintainer related targets
##
update-local: Makefile

maintainer-check-local: Makefile
	$(WHITESPACE_DETECT)  $(DTT_PYTHON_SRCS)
