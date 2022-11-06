def max(a, b):
    return a if a>b else b

def find_max(arr):
    if len(arr) == 2:
        return max(arr[0], arr[1])
    return max(find_max(arr[1:]), arr[0])

def test_max():
    assert 5 == find_max([1,5,3])
