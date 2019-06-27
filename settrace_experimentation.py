#!/usr/bin/env python

"""
Prepared for a presentation on debuggers to demonstrate how sys.settrace() works.

The lines at the end of the two "trace_*" methods can be commented & uncommented to change the behavior and learn what's
possible.
"""

import sys
import random
from datetime import datetime

MAX = 100


def main(num_loops=1000):
    for i in range(num_loops):
        num = random.randint(0, MAX)
        denom = random.randint(0, MAX)
        result = num / denom
        print("{} divided by {} is {:.2f}".format(num, denom, result))


def trace_lines(frame, event, arg):
    """
    This method is run before each line executes when in settrace mode.
    """
    line_no = frame.f_lineno
    co = frame.f_code
    func_name = co.co_name
    print(f"  in trace_lines(), event:{event} {func_name} line {line_no}.")
    # print(f"  in trace_lines(), event:{event} {func_name} line {line_no}. vars: {frame.f_locals}")
    # print(f"  {datetime.now()} in trace_lines(), event:{event} {func_name} line {line_no}.")


def trace_calls(frame, event, arg):
    """
    Print some info about what's going on
    """
    # This method is called when in settrace mode each time a function is called, and it returns
    # the method that should be run for each line in the function that runs.
    co = frame.f_code
    filename = co.co_filename
    if filename != sys.argv[0]:
        return
    func_name = co.co_name
    line_no = frame.f_lineno
    print(f"in trace_calls(), event:{event}, arg:{arg}, filename:{filename}, func_name:{func_name}, line:{line_no}")
    # return trace_lines
    return


if __name__ == "__main__":
    arg = sys.argv[-1]
    if arg.isdigit():
        main(arg)
    else:
        sys.settrace(trace_calls)
        main()
