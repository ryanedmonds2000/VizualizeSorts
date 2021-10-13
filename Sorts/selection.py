# Selection sort
import utils

def selectionsort(list):
    listlen = len(list)
    for i in range(len(list)):
        minimum = (list[i], i)
        for j in range(i+1,listlen):
            if list[j] < minimum[0]:
                minimum = (list[j], j)
        utils.swap(list, i, minimum[1])
    return list
