def selection_sort(unsorted):
    size = len(unsorted)
    sort = [None]*size
    seen = [None]*size
    for i in range(size):
        smallest = None
        for j in range(size):
            if j in seen:
                continue
            if smallest is None:
                smallest = j
                continue
            if unsorted[j] < unsorted[smallest]:
                smallest = j
        seen[i] = smallest
        sort[i] = unsorted[smallest]
    return sort

find_smallest = lambda l: l.index(min(l))

def selection_sort(unsorted):
    sort = []
    for i in range(len(unsorted)):
        smallest_index = find_smallest(unsorted)
        smallest_value = unsorted.pop(smallest_index)
        sort.append(smallest_value)
    return sort


def test_sort():
    unsorted = [5,3,6,2,10]
    sort = selection_sort(unsorted)
    assert sort == [2,3,5,6,10]

def test_against_python_builtin():
    from random import randint
    unsorted = [randint(1,10**3) for i in range(10000)]
    expected = sorted(unsorted)
    sort = selection_sort(unsorted)
    assert sort == expected
