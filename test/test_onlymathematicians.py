from select import select
import pytest
from SelectionSort import select_min
from BinarySearch import binary_search

def test_select_min():
    assert [2, 3, 5, 6, 10] == select_min.selectionSort([10, 6, 5, 3, 2])
    assert [14, 21, 27, 41, 43, 45, 46, 57, 70] == select_min.selectionSort([14,46,43,27,57,41,45,21,70])
    assert [15, 25, 37, 68, 79] ==select_min.selectionSort([15, 79, 25, 37, 68])

def test_binary_search():
    assert 5 == binary_search.binarySearch([2, 3, 5, 6, 10, 11], 11)
    assert 1 == binary_search.binarySearch([2, 3, 5, 6, 10, 11], 3)

    myList = list(range(1, 101))
    assert 49 == binary_search.binarySearch(myList, 50)