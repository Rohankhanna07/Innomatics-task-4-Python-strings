#!/usr/bin/env python
# coding: utf-8

# task 2
# In Python, a string can be split on a delimiter.
# 
# Example:
# a = "this is a string"
# a = a.split(" ") # a is converted to a list of strings. 
# print a
# ['this', 'is', 'a', 'string']
# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen

# In[ ]:


def split_and_join(line):
    Output = line.split();
    Output = "-".join(Output)
    return Output;

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In[ ]:




