# Insertion sort
import Sorts.utils as utils

def insertionsort(list):
    for i in range(len(list)):
        while i != 0 and list[i] < list[i-1]:
            utils.swap(list, i, i-1)
            i -= 1
    return list
