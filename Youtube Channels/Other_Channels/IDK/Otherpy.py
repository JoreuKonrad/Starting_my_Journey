
# Learning how to call other py file without creating __pycache__

import sys
sys.dont_write_bytecode = True

from name import test

test()


