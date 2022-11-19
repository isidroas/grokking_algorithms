import pytest
from quick_sort_mine import *

def test_base_case():
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    assert quicksort([2, 1]) == [1, 2]
    assert quicksort([1, 2]) == [1, 2]


@pytest.mark.parametrize('partition',(partition_v1,partition_v2, partition_v3))
def test_partition(partition):
    assert partition([33, 15, 10], 0) == ([15, 10], 33, [])
    assert partition([33, 15, 10], 1) == ([10], 15, [33])
    assert partition([33, 15, 10], 2) == ([], 10, [33, 15])


def test_rec():
    assert quicksort([33, 15, 10]) == [10, 15, 33]
    assert quicksort([33, 10, 15, 7]) == [7, 10, 15, 33]
    assert quicksort([3, 5, 2, 1, 4]) == [1, 2, 3, 4, 5]

def test_python_sort():
    from random import randint
    unsorted = [randint(0,1000000) for i in range(100000)]
    quicksort(unsorted) == unsorted.sort()


@pytest.mark.parametrize('version',(partition_v1,partition_v2, partition_v3))
def test_partition_versions(version):
    import quick_sort_mine
    quick_sort_mine.PARTITION=version
    assert quicksort([3, 5, 2, 1, 4]) == [1, 2, 3, 4, 5]
