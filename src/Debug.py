#
# Copyright (C) 2008 Francesco Salvestrini
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

import sys    # Useless
import traceback

#
# NOTE:
#     Do not include Config here in order to avoid a mutual inclusion between
#     Config and Debug (see the last lines)
#
from   Trace import *

def bug(s = "") :
    tmp1 = "Bug hit"
    if s != "" :
	tmp2 = tmp1 + ": " + s
    else :
	tmp2 = tmp1 + "!"

    traceback.print_exc(file=sys.stdout)

    error(tmp2)
    error("Please report to <" + PACKAGE_BUGREPORT + ">")

    # Like _exit(), exit immediately ...
    os._exit(1)

# Test
if (__name__ == '__main__') :
    debug("Test completed")
    sys.exit(0)
