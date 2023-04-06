# https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments

import sys
import time

arguments = sys.argv
arguments.pop(0)

while True:
    time.sleep(10)
    print(arguments)
