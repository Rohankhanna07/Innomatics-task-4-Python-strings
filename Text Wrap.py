#!/usr/bin/env python
# coding: utf-8

# task 7
# You are given a string S and width W.
# Your task is to wrap the string into a paragraph of width W .

# In[ ]:


import textwrap

def wrap(string, max_width):
    return textwrap.TextWrapper(width=max_width).fill(text=string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[ ]:




