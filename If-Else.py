# Task
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format
#
# A single line containing a positive integer, .
#
# Constraints
#
# Output Format
#
# Print Weird if the number is weird. Otherwise, print Not Weird.


#!/bin/python3

import math
import os
import random
import re
import sys

def checkifodd(num):
    if num % 2 == 0:
        if n > 20:
            return "Not Weird"
        elif n >= 6 and n <= 20:
            return "Weird"
        elif n >= 2 and n <= 5:
            return "Not Weird"

    else:
        return "Weird"



if __name__ == '__main__':
    n = int(input().strip())
    print(checkifodd(n))

