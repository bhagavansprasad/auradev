#!/usr/bin/env python

from __future__ import print_function
from __future__ import absolute_import
import pexpect

child = pexpect.spawn('df')

# parse 'df' output into a list.
pattern = r"\n(\S+).*?([0-9]+)%"
filesystem_list = []
for dummy in range (0, 1000):
    i = child.expect ([pattern, pexpect.EOF])
    if i == 0:
        filesystem_list.append (child.match.groups())
    else:
        break

# Print report
print()
for m in filesystem_list:
    s = "Filesystem %s is at %s%%" % (m[0], m[1])
    # highlight filesystems over 95% capacity
    if int(m[1]) > 95:
        s = '! ' + s
    else:
        s = '  ' + s
    print(s)

