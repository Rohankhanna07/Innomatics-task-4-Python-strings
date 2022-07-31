#!/usr/bin/env python
# coding: utf-8

# task 3
# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# 
# Input Format
# 
# The first line contains the first name, and the second line contains the last name.

# In[ ]:


#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print("Hello %s %s! You just delved into python."%(first_name,last_name))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# In[ ]:




