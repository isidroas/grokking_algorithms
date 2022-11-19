from random import randint


def partition_v1(arr, pivot_index):
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

def partition_v2(arr, pivot_index):
    pivot = arr.pop(pivot_index)

    left = [ i for i in arr if i<pivot]
    right = [ i for i in arr if i>pivot]

    return left, pivot, right

def partition_v3(arr, pivot_index):
    """
    from TheAlgorithims
    """

    pivot = arr[ pivot_index ]
    lesser =[]
    greater = []

    for i in arr[:pivot_index]:
        (lesser if i < pivot else greater).append(i)

    for i in arr[pivot_index+1:]:
        (lesser if i < pivot else greater).append(i)

    return lesser, pivot, greater

PARTITION = partition_v3
def quicksort(arr):
    if len(arr) < 2:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        return arr

    pivot_index = randint(0, len(arr) - 1)
    left, pivot, right = PARTITION(arr, pivot_index)
    return quicksort(left) + [pivot] + quicksort(right)


