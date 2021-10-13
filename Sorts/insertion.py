# Insertion sort
import utils

def insertionsort(list):
    listlen = len(list)
    for i in range(listlen):
        while i != 0 and list[i] < list[i-1]:
            utils.swap(list, i, i-1)
            i -= 1
    return list
