# -*- coding:utf-8 -*-
"""O(log n) on search sorted list"""

def binary_search(items, item):
    low = 0
    height = len(items) - 1
    while low <= height:
        mid = (low + height)/2
        guess = items[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            height = mid - 1
    return None

my_list = [1, 3, 5, 7, 9]

print binary_search(my_list, 3)
print binary_search(my_list, -1)
