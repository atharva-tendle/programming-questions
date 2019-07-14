#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    # Read the integer n
    n = int(input().strip())
    # check if n is odd
    if n % 2 != 0:
        print('Weird')
    # check if n is between 2 and 5 
    elif n >= 2 and n <= 5:
        print('Not Weird')
    # check if n is between 6 and 20
    elif n >= 6 and n <= 20:
        print('Weird')
    # if nothing else works then n is greater than 20
    else:
        print('Not Weird')