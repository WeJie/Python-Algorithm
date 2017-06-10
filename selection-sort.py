# -*- coding:utf-8 -*-

def find_samllest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        samllest_index = find_samllest(arr)
        new_arr.append(arr.pop(samllest_index))
    return new_arr

test = [3, 1, 4, 9, 5]

print selection_sort(test)
