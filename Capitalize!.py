#!/usr/bin/env python
# coding: utf-8

# task 6
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
# nput Format
# 
# A single line of input containing the full name,S 

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for n in s.split():
        s = s.replace(n,n.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# In[ ]:




