#!/usr/bin/env python
# coding: utf-8

# task 1
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# In[ ]:


def swap_case(s):
    change=[]
    for i in range(len(s)):
        if (s[i].isupper())==True:
            change.append(s[i].lower())
        elif (s[i].islower()==True):
            change.append(s[i].upper())
        else:
            change.append(s[i])  
        stri=''
    return stri.join(change)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# In[ ]:




