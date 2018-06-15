#!/usr/bin env python

import os
import sys

dirname = sys.argv[1]
images = os.listdir(dirname)

for i in images:
    print('''- original: %s''' %(os.path.basename(i)))

