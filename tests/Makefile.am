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
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program; if not, write to the Free Software Foundation, Inc.,
## 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
##

include $(top_srcdir)/Makefile.sub

CLEANFILES =
EXTRA_DIST =
##
## NOTE:
##     In order to debug the tests during the 'distcheck' target use the
##     following TESTS_ENVIRONMENT:
##
##       TESTS_ENVIRONMENT = testdir=@abs_builddir@ DEBUG=x VERBOSE=x
##
TESTS_ENVIRONMENT = testdir=@abs_builddir@

scripts =					\
        wrapper					\
        defs

all-local: $(scripts)

# wrapper
wrapper: $(srcdir)/wrapper.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/wrapper.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
CLEANFILES += wrapper
EXTRA_DIST += wrapper.in

##
## NOTE:
##   defs should not be made executable because it should be only included by
##   test-cases
##

# defs
defs: $(srcdir)/defs.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/defs.in > $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
CLEANFILES += defs
EXTRA_DIST += defs.in

# Tests
FAIL_TESTS    =
SUCCESS_TESTS =

FAIL_TESTS    +=				\
	test-fail				\
	test-command-show-filter-07		\
	test-command-show-filter-10

SUCCESS_TESTS +=				\
	test-success				\
	test-verbose				\
	test-debug				\
	test-warnings				\
	test-help				\
	test-version				\
						\
	test-command-init-01			\
	test-command-clean-01			\
						\
	test-command-init-help-01		\
	test-command-init-opts-short-01	\
	test-command-init-opts-long-01		\
	test-command-init-version-01		\
	test-command-init-configuration-01	\
						\
	test-command-clean-help-01		\
	test-command-clean-opts-short-01	\
	test-command-clean-opts-long-01	\
	test-command-clean-version-01		\
						\
	test-command-add-help-01		\
	test-command-add-opts-short-01		\
	test-command-add-opts-long-01		\
	test-command-add-version-01		\
	test-command-add-01			\
	test-command-add-02			\
	test-command-add-03			\
	test-command-add-04			\
	test-command-add-configuration-01	\
						\
	test-command-remove-help-01		\
	test-command-remove-opts-short-01	\
	test-command-remove-opts-long-01	\
	test-command-remove-version-01		\
	test-command-remove-01			\
						\
	test-command-edit-help-01		\
	test-command-edit-opts-short-01	\
	test-command-edit-opts-long-01		\
	test-command-edit-version-01		\
	test-command-edit-01			\
	test-command-edit-02			\
	test-command-edit-03			\
	test-command-edit-04			\
	test-command-edit-interactive-01	\
	test-command-edit-interactive-02	\
	test-command-edit-interactive-03	\
	test-command-edit-no-interactive-01	\
	test-command-edit-configuration-01	\
						\
	test-command-fix-help-01		\
	test-command-fix-opts-short-01		\
	test-command-fix-opts-long-01		\
	test-command-fix-version-01		\
	test-command-fix-01			\
						\
	test-command-move-help-01		\
	test-command-move-opts-short-01	\
	test-command-move-opts-long-01		\
	test-command-move-version-01		\
	test-command-move-01			\
						\
	test-command-config-help-01		\
	test-command-config-opts-short-01	\
	test-command-config-opts-long-01	\
	test-command-config-version-01		\
	test-command-config-01			\
	test-command-config-02			\
	test-command-config-03			\
						\
	test-command-show-help-01		\
	test-command-show-opts-short-01	\
	test-command-show-opts-long-01		\
	test-command-show-version-01		\
	test-command-show-01			\
	test-command-show-02			\
	test-command-show-03			\
	test-command-show-04			\
	test-command-show-05			\
	test-command-show-06			\
	test-command-show-07			\
	test-command-show-08			\
	test-command-show-09			\
	test-command-show-10			\
	test-command-show-11			\
	test-command-show-filter-01		\
	test-command-show-filter-02		\
	test-command-show-filter-03		\
	test-command-show-filter-04		\
	test-command-show-filter-05		\
	test-command-show-filter-06		\
	test-command-show-filter-08		\
	test-command-show-filter-09		\
	test-command-show-filter-11		\
	test-command-show-filter-12		\
	test-command-show-filter-13		\
	test-command-show-filter-14		\
	test-command-show-filter-15		\
	test-command-show-filter-16		\
	test-command-show-wrap-01		\
	test-command-show-wrap-02		\
	test-command-show-wrap-03		\
	test-command-show-flags-01		\
	test-command-show-warnings-01		\
	test-command-show-warnings-02		\
	test-command-show-collapsed-01		\
	test-command-show-configuration-01	\
						\
	test-command-mark-help-01		\
	test-command-mark-opts-short-01	\
	test-command-mark-opts-long-01		\
	test-command-mark-version-01		\
	test-command-mark-done-01		\
	test-command-mark-done-02		\
	test-command-mark-done-03		\
	test-command-mark-done-04		\
	test-command-mark-not-done-01		\
						\
	test-devtodo-to-dnt-01			\
	test-dnt-to-devtodo-01			\
						\
	test-import-export-01			\
	test-import-export-02

# XXX FIXME: Add this test again ASAP
#	test-import-export-03


XFAIL_TESTS  = $(FAIL_TESTS)
TESTS        = $(FAIL_TESTS) $(SUCCESS_TESTS)

test-success: $(srcdir)/test-success.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-success.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-success.in
CLEANFILES += test-success

test-fail: $(srcdir)/test-fail.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-fail.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-fail.in
CLEANFILES += test-fail

test-dnt-to-devtodo-01: $(srcdir)/test-dnt-to-devtodo-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-dnt-to-devtodo-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-dnt-to-devtodo-01.in
CLEANFILES += test-dnt-to-devtodo-01

test-devtodo-to-dnt-01: $(srcdir)/test-devtodo-to-dnt-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-devtodo-to-dnt-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-devtodo-to-dnt-01.in
CLEANFILES += test-devtodo-to-dnt-01

test-verbose: $(srcdir)/test-verbose.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-verbose.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-verbose.in
CLEANFILES += test-verbose

test-debug: $(srcdir)/test-debug.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-debug.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-debug.in
CLEANFILES += test-debug

test-warnings: $(srcdir)/test-warnings.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-warnings.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-warnings.in
CLEANFILES += test-warnings

test-help: $(srcdir)/test-help.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-help.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-help.in
CLEANFILES += test-help

test-version: $(srcdir)/test-version.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-version.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-version.in
CLEANFILES += test-version

test-command-edit-01: $(srcdir)/test-command-edit-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-edit-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-edit-01.in
CLEANFILES += test-command-edit-01

test-command-edit-02: $(srcdir)/test-command-edit-02.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-edit-02.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-edit-02.in
CLEANFILES += test-command-edit-02

test-command-edit-03: $(srcdir)/test-command-edit-03.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-edit-03.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-edit-03.in
CLEANFILES += test-command-edit-03

test-command-edit-04: $(srcdir)/test-command-edit-04.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-edit-04.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-edit-04.in
CLEANFILES += test-command-edit-04

test-command-edit-interactive-01: $(srcdir)/test-command-edit-interactive-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-edit-interactive-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-edit-interactive-01.in
CLEANFILES += test-command-edit-interactive-01

test-command-edit-interactive-02: $(srcdir)/test-command-edit-interactive-02.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-edit-interactive-02.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-edit-interactive-02.in
CLEANFILES += test-command-edit-interactive-02

test-command-edit-interactive-03: $(srcdir)/test-command-edit-interactive-03.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-edit-interactive-03.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-edit-interactive-03.in
CLEANFILES += test-command-edit-interactive-03

test-command-edit-no-interactive-01: $(srcdir)/test-command-edit-no-interactive-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-edit-no-interactive-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-edit-no-interactive-01.in
CLEANFILES += test-command-edit-no-interactive-01

test-command-edit-configuration-01: $(srcdir)/test-command-edit-configuration-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-edit-configuration-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-edit-configuration-01.in
CLEANFILES += test-command-edit-configuration-01

test-command-fix-01: $(srcdir)/test-command-fix-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-fix-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-fix-01.in
CLEANFILES += test-command-fix-01

test-command-move-01: $(srcdir)/test-command-move-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-move-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-move-01.in
CLEANFILES += test-command-move-01

test-command-add-01: $(srcdir)/test-command-add-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-add-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-add-01.in
CLEANFILES += test-command-add-01

test-command-add-02: $(srcdir)/test-command-add-02.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-add-02.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-add-02.in
CLEANFILES += test-command-add-02

test-command-add-03: $(srcdir)/test-command-add-03.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-add-03.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-add-03.in
CLEANFILES += test-command-add-03

test-command-add-04: $(srcdir)/test-command-add-04.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-add-04.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-add-04.in
CLEANFILES += test-command-add-04

test-command-remove-01: $(srcdir)/test-command-remove-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-remove-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-remove-01.in
CLEANFILES += test-command-remove-01

test-command-init-01: $(srcdir)/test-command-init-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-init-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-init-01.in
CLEANFILES += test-command-init-01

test-command-clean-01: $(srcdir)/test-command-clean-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-clean-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-clean-01.in
CLEANFILES += test-command-clean-01

test-command-config-01: $(srcdir)/test-command-config-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-config-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-config-01.in
CLEANFILES += test-command-config-01

test-command-config-02: $(srcdir)/test-command-config-02.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-config-02.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-config-02.in
CLEANFILES += test-command-config-02

test-command-config-03: $(srcdir)/test-command-config-03.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-config-03.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-config-03.in
CLEANFILES += test-command-config-03

test-command-init-help-01: $(srcdir)/test-command-init-help-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-init-help-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-init-help-01.in
CLEANFILES += test-command-init-help-01

test-command-init-opts-short-01: $(srcdir)/test-command-init-opts-short-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-init-opts-short-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-init-opts-short-01.in
CLEANFILES += test-command-init-opts-short-01

test-command-init-opts-long-01: $(srcdir)/test-command-init-opts-long-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-init-opts-long-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-init-opts-long-01.in
CLEANFILES += test-command-init-opts-long-01

test-command-init-version-01: $(srcdir)/test-command-init-version-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-init-version-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-init-version-01.in
CLEANFILES += test-command-init-version-01

test-command-init-configuration-01: $(srcdir)/test-command-init-configuration-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-init-configuration-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-init-configuration-01.in
CLEANFILES += test-command-init-configuration-01

test-command-clean-help-01: $(srcdir)/test-command-clean-help-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-clean-help-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-clean-help-01.in
CLEANFILES += test-command-clean-help-01

test-command-clean-opts-short-01: $(srcdir)/test-command-clean-opts-short-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-clean-opts-short-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-clean-opts-short-01.in
CLEANFILES += test-command-clean-opts-short-01

test-command-clean-opts-long-01: $(srcdir)/test-command-clean-opts-long-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-clean-opts-long-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-clean-opts-long-01.in
CLEANFILES += test-command-clean-opts-long-01

test-command-clean-version-01: $(srcdir)/test-command-clean-version-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-clean-version-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-clean-version-01.in
CLEANFILES += test-command-clean-version-01

test-command-add-help-01: $(srcdir)/test-command-add-help-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-add-help-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-add-help-01.in
CLEANFILES += test-command-add-help-01

test-command-add-opts-short-01: $(srcdir)/test-command-add-opts-short-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-add-opts-short-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-add-opts-short-01.in
CLEANFILES += test-command-add-opts-short-01

test-command-add-opts-long-01: $(srcdir)/test-command-add-opts-long-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-add-opts-long-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-add-opts-long-01.in
CLEANFILES += test-command-add-opts-long-01

test-command-add-version-01: $(srcdir)/test-command-add-version-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-add-version-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-add-version-01.in
CLEANFILES += test-command-add-version-01

test-command-add-configuration-01: $(srcdir)/test-command-add-configuration-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-add-configuration-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-add-configuration-01.in
CLEANFILES += test-command-add-configuration-01

test-command-config-help-01: $(srcdir)/test-command-config-help-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-config-help-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-config-help-01.in
CLEANFILES += test-command-config-help-01

test-command-config-opts-short-01: $(srcdir)/test-command-config-opts-short-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-config-opts-short-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-config-opts-short-01.in
CLEANFILES += test-command-config-opts-short-01

test-command-config-opts-long-01: $(srcdir)/test-command-config-opts-long-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-config-opts-long-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-config-opts-long-01.in
CLEANFILES += test-command-config-opts-long-01

test-command-config-version-01: $(srcdir)/test-command-config-version-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-config-version-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-config-version-01.in
CLEANFILES += test-command-config-version-01

test-command-mark-help-01: $(srcdir)/test-command-mark-help-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-mark-help-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-mark-help-01.in
CLEANFILES += test-command-mark-help-01

test-command-mark-opts-short-01: $(srcdir)/test-command-mark-opts-short-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-mark-opts-short-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-mark-opts-short-01.in
CLEANFILES += test-command-mark-opts-short-01

test-command-mark-opts-long-01: $(srcdir)/test-command-mark-opts-long-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-mark-opts-long-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-mark-opts-long-01.in
CLEANFILES += test-command-mark-opts-long-01

test-command-mark-version-01: $(srcdir)/test-command-mark-version-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-mark-version-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-mark-version-01.in
CLEANFILES += test-command-mark-version-01

test-command-mark-done-01: $(srcdir)/test-command-mark-done-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-mark-done-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-mark-done-01.in
CLEANFILES += test-command-mark-done-01

test-command-mark-done-02: $(srcdir)/test-command-mark-done-02.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-mark-done-02.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-mark-done-02.in
CLEANFILES += test-command-mark-done-02

test-command-mark-done-03: $(srcdir)/test-command-mark-done-03.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-mark-done-03.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-mark-done-03.in
CLEANFILES += test-command-mark-done-03

test-command-mark-done-04: $(srcdir)/test-command-mark-done-04.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-mark-done-04.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-mark-done-04.in
CLEANFILES += test-command-mark-done-04

test-command-mark-not-done-01: $(srcdir)/test-command-mark-not-done-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-mark-not-done-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-mark-not-done-01.in
CLEANFILES += test-command-mark-not-done-01

test-command-fix-help-01: $(srcdir)/test-command-fix-help-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-fix-help-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-fix-help-01.in
CLEANFILES += test-command-fix-help-01

test-command-fix-opts-short-01: $(srcdir)/test-command-fix-opts-short-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-fix-opts-short-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-fix-opts-short-01.in
CLEANFILES += test-command-fix-opts-short-01

test-command-fix-opts-long-01: $(srcdir)/test-command-fix-opts-long-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-fix-opts-long-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-fix-opts-long-01.in
CLEANFILES += test-command-fix-opts-long-01

test-command-fix-version-01: $(srcdir)/test-command-fix-version-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-fix-version-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-fix-version-01.in
CLEANFILES += test-command-fix-version-01

test-command-show-wrap-01: $(srcdir)/test-command-show-wrap-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-wrap-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-wrap-01.in
CLEANFILES += test-command-show-wrap-01

test-command-show-wrap-02: $(srcdir)/test-command-show-wrap-02.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-wrap-02.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-wrap-02.in
CLEANFILES += test-command-show-wrap-02

test-command-show-wrap-03: $(srcdir)/test-command-show-wrap-03.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-wrap-03.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-wrap-03.in
CLEANFILES += test-command-show-wrap-03

test-command-show-flags-01: $(srcdir)/test-command-show-flags-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-flags-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-flags-01.in
CLEANFILES += test-command-show-flags-01

test-command-show-warnings-01: $(srcdir)/test-command-show-warnings-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-warnings-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-warnings-01.in
CLEANFILES += test-command-show-warnings-01

test-command-show-warnings-02: $(srcdir)/test-command-show-warnings-02.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-warnings-02.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-warnings-02.in
CLEANFILES += test-command-show-warnings-02

test-command-show-collapsed-01: $(srcdir)/test-command-show-collapsed-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-collapsed-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-collapsed-01.in
CLEANFILES += test-command-show-collapsed-01

test-command-show-configuration-01: $(srcdir)/test-command-show-configuration-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-configuration-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-configuration-01.in
CLEANFILES += test-command-show-configuration-01

test-command-edit-help-01: $(srcdir)/test-command-edit-help-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-edit-help-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-edit-help-01.in
CLEANFILES += test-command-edit-help-01

test-command-edit-opts-short-01: $(srcdir)/test-command-edit-opts-short-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-edit-opts-short-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-edit-opts-short-01.in
CLEANFILES += test-command-edit-opts-short-01

test-command-edit-opts-long-01: $(srcdir)/test-command-edit-opts-long-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-edit-opts-long-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-edit-opts-long-01.in
CLEANFILES += test-command-edit-opts-long-01

test-command-edit-version-01: $(srcdir)/test-command-edit-version-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-edit-version-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-edit-version-01.in
CLEANFILES += test-command-edit-version-01

test-command-move-help-01: $(srcdir)/test-command-move-help-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-move-help-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-move-help-01.in
CLEANFILES += test-command-move-help-01

test-command-move-opts-short-01: $(srcdir)/test-command-move-opts-short-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-move-opts-short-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-move-opts-short-01.in
CLEANFILES += test-command-move-opts-short-01

test-command-move-opts-long-01: $(srcdir)/test-command-move-opts-long-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-move-opts-long-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-move-opts-long-01.in
CLEANFILES += test-command-move-opts-long-01

test-command-move-version-01: $(srcdir)/test-command-move-version-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-move-version-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-move-version-01.in
CLEANFILES += test-command-move-version-01

test-command-remove-help-01: $(srcdir)/test-command-remove-help-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-remove-help-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-remove-help-01.in
CLEANFILES += test-command-remove-help-01

test-command-remove-opts-short-01: $(srcdir)/test-command-remove-opts-short-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-remove-opts-short-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-remove-opts-short-01.in
CLEANFILES += test-command-remove-opts-short-01

test-command-remove-opts-long-01: $(srcdir)/test-command-remove-opts-long-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-remove-opts-long-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-remove-opts-long-01.in
CLEANFILES += test-command-remove-opts-long-01

test-command-remove-version-01: $(srcdir)/test-command-remove-version-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-remove-version-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-remove-version-01.in
CLEANFILES += test-command-remove-version-01

test-command-show-01: $(srcdir)/test-command-show-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-01.in
CLEANFILES += test-command-show-01

test-command-show-02: $(srcdir)/test-command-show-02.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-02.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-02.in
CLEANFILES += test-command-show-02

test-command-show-03: $(srcdir)/test-command-show-03.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-03.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-03.in
CLEANFILES += test-command-show-03

test-command-show-04: $(srcdir)/test-command-show-04.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-04.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-04.in
CLEANFILES += test-command-show-04

test-command-show-05: $(srcdir)/test-command-show-05.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-05.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-05.in
CLEANFILES += test-command-show-05

test-command-show-06: $(srcdir)/test-command-show-06.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-06.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-06.in
CLEANFILES += test-command-show-06

test-command-show-07: $(srcdir)/test-command-show-07.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-07.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-07.in
CLEANFILES += test-command-show-07

test-command-show-08: $(srcdir)/test-command-show-08.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-08.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-08.in
CLEANFILES += test-command-show-08

test-command-show-09: $(srcdir)/test-command-show-09.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-09.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-09.in
CLEANFILES += test-command-show-09

test-command-show-10: $(srcdir)/test-command-show-10.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-10.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-10.in
CLEANFILES += test-command-show-10

test-command-show-11: $(srcdir)/test-command-show-11.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-11.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-11.in
CLEANFILES += test-command-show-11

test-command-show-filter-01: $(srcdir)/test-command-show-filter-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-01.in
CLEANFILES += test-command-show-filter-01

test-command-show-filter-02: $(srcdir)/test-command-show-filter-02.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-02.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-02.in
CLEANFILES += test-command-show-filter-02

test-command-show-filter-03: $(srcdir)/test-command-show-filter-03.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-03.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-03.in
CLEANFILES += test-command-show-filter-03

test-command-show-filter-04: $(srcdir)/test-command-show-filter-04.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-04.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-04.in
CLEANFILES += test-command-show-filter-04

test-command-show-filter-05: $(srcdir)/test-command-show-filter-05.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-05.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-05.in
CLEANFILES += test-command-show-filter-05

test-command-show-filter-06: $(srcdir)/test-command-show-filter-06.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-06.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-06.in
CLEANFILES += test-command-show-filter-06

test-command-show-filter-07: $(srcdir)/test-command-show-filter-07.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-07.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-07.in
CLEANFILES += test-command-show-filter-07

test-command-show-filter-08: $(srcdir)/test-command-show-filter-08.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-08.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-08.in
CLEANFILES += test-command-show-filter-08

test-command-show-filter-09: $(srcdir)/test-command-show-filter-09.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-09.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-09.in
CLEANFILES += test-command-show-filter-09

test-command-show-filter-10: $(srcdir)/test-command-show-filter-10.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-10.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-10.in
CLEANFILES += test-command-show-filter-10

test-command-show-filter-11: $(srcdir)/test-command-show-filter-11.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-11.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-11.in
CLEANFILES += test-command-show-filter-11

test-command-show-filter-12: $(srcdir)/test-command-show-filter-12.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-12.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-12.in
CLEANFILES += test-command-show-filter-12

test-command-show-filter-13: $(srcdir)/test-command-show-filter-13.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-13.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-13.in
CLEANFILES += test-command-show-filter-13

test-command-show-filter-14: $(srcdir)/test-command-show-filter-14.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-14.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-14.in
CLEANFILES += test-command-show-filter-14

test-command-show-filter-15: $(srcdir)/test-command-show-filter-15.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-15.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-15.in
CLEANFILES += test-command-show-filter-15

test-command-show-filter-16: $(srcdir)/test-command-show-filter-16.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-filter-16.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-filter-16.in
CLEANFILES += test-command-show-filter-16

test-command-show-help-01: $(srcdir)/test-command-show-help-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-help-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-help-01.in
CLEANFILES += test-command-show-help-01

test-command-show-opts-short-01: $(srcdir)/test-command-show-opts-short-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-opts-short-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-opts-short-01.in
CLEANFILES += test-command-show-opts-short-01

test-command-show-opts-long-01: $(srcdir)/test-command-show-opts-long-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-opts-long-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-opts-long-01.in
CLEANFILES += test-command-show-opts-long-01

test-command-show-version-01: $(srcdir)/test-command-show-version-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-command-show-version-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-command-show-version-01.in
CLEANFILES += test-command-show-version-01

test-import-export-01: $(srcdir)/test-import-export-01.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-import-export-01.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-import-export-01.in
CLEANFILES += test-import-export-01

test-import-export-02: $(srcdir)/test-import-export-02.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-import-export-02.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-import-export-02.in
CLEANFILES += test-import-export-02

test-import-export-03: $(srcdir)/test-import-export-03.in Makefile
	( rm -f $@ $@.tmp && \
	  $(do_subst) < $(srcdir)/test-import-export-03.in > $@.tmp && \
	  chmod +x $@.tmp && \
	  chmod a-w $@.tmp && \
	  mv -f $@.tmp $@ ) || { \
	        rm -f $@ $@.tmp ; \
	        exit 1 ; \
	}
EXTRA_DIST += test-import-export-03.in
CLEANFILES += test-import-export-03

clean-local:
	rm -rf testSubDir-*

##
## Maintainer related targets
##
update-local: Makefile

maintainer-check-local: Makefile
