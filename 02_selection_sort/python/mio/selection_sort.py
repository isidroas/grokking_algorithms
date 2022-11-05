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


def test_sort():
    unsorted = [5,3,6,2,10]
    sort = selection_sort(unsorted)
    assert sort == [2,3,5,6,10]
