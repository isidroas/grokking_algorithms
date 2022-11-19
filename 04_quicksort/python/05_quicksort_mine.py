from random import randint


def partition(arr, pivot_index):
    pivot = arr[pivot_index]
    left, right = [], []

    for index, item in enumerate(arr):
        if index == pivot_index:
            continue
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

    return left, pivot, right


def quicksort(arr):
    if len(arr) < 2:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        return arr

    pivot_index = randint(0, len(arr) - 1)
    left, pivot, right = partition(arr, pivot_index)
    return quicksort(left) + [pivot] + quicksort(right)


def test_base_case():
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    assert quicksort([2, 1]) == [1, 2]
    assert quicksort([1, 2]) == [1, 2]


def test_partition():
    assert partition([33, 15, 10], 0) == ([15, 10], 33, [])
    assert partition([33, 15, 10], 1) == ([10], 15, [33])
    assert partition([33, 15, 10], 2) == ([], 10, [33, 15])


def test_rec():
    assert quicksort([33, 15, 10]) == [10, 15, 33]
    assert quicksort([33, 10, 15, 7]) == [7, 10, 15, 33]
    assert quicksort([3, 5, 2, 1, 4]) == [1, 2, 3, 4, 5]
