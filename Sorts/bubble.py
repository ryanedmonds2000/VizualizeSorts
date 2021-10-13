# Bubble sort
import utils

def bubblesort(list):
    for i in range(len(list), 0, -1):
        for j in range(1, i):
            if list[j-1] > list[j]: utils.swap(list, j-1, j)
    return list
