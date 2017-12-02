#!/usr/bin/python3

import sys

print('args len=', len(sys.argv))
if (len(sys.argv) > 1):
    for arg in sys.argv:
        print("arg=", arg)
else:
   print("no args")

print("PYTHON")

if True:
    print("true")
    print("really true")
else:
    print("false")
    print("I said false!")

# input("\n\nPress enter")

print("finished")