# Merge sort

def mergesort(list):
    listlen = len(list)
    if listlen == 1: return list
    left = mergesort(list[:listlen//2])
    right = mergesort(list[listlen//2:])
    i = j = 0
    leftlen = len(left)
    rightlen = len(right)
    output = []
    while i < leftlen or j < rightlen:
        if i == leftlen:
            output += right[j:]
            break
        if j == rightlen:
            output += left[i:]
            break
        if left[i] <= right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    return output
