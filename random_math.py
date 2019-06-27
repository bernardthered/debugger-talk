#!/usr/bin/env python

"""
Prepared for a presentation on debuggers to demonstrate three different debuggers.

Each of the three lines in main() can be uncommented to try out a different debugger.
"""

import random

MAX = 100


def main(num_loops=1000):
    for i in range(num_loops):
        num = random.randint(0, MAX)
        denom = random.randint(0, MAX)
        result = num / denom
        # import pdb; pdb.pdb.set_trace()  # regular pdb
        # import pdb; pdb.set_trace()  # this is pdb++ (it takes over the name `pdb` when it is installed)
        # from pudb import set_trace; set_trace()  # pudb
        print("{} divided by {} is {:.2f}".format(num, denom, result))


if __name__ == "__main__":
    import sys
    arg = sys.argv[-1]
    if arg.isdigit():
        main(arg)
    else:
        main()
