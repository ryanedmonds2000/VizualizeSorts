from unittest import mock

import Sorts.utils
from Sorts.bubble import bubblesort
from Sorts.insertion import insertionsort
from Sorts.merge import mergesort
from Sorts.selection import selectionsort

sortfuncs = {
    "bubble": bubblesort,
    "insertion": insertionsort,
    "merge": mergesort,
    "selection": selectionsort
}

def visualize(sortfunc, list):
    """ Calls the given sort on the list, and vizualizes it by tracking
    element swaps. Only works on sorts that mutate the list with utils.swap"""
    with mock.patch('Sorts.utils.swap', side_effect = Sorts.utils.swap) as mocker:
        sortfunc(list)
        print(mocker.mock_calls)
