# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 22:45:22 2016

@author: YI
"""

def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

#list is a ordered array
def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        elif item < a_list[midpoint]:
                last = midpoint - 1
        else:
            first = midpoint + 1
    return found

sequential_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(sequential_list, 3))
print(sequential_search(sequential_list, 13))

binary_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(binary_list, 3))
print(binary_search(binary_list, 13))

