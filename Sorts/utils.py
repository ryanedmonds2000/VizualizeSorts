# Helper functions

def swap(list, i, j):
    """ Swaps the elements in indexes i and j in the given list. Updates
    list without returning """
    temp = list[j]
    list[j] = list[i]
    list[i] = temp
