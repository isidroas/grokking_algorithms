def bin_search(arr, obj):
    size = len(arr)
    if size==0:
        return None
    elif size==1:
        return 0 if obj in arr else None
    elif size==2:
        if arr[0]==obj:
            return 0
        elif arr[1]==obj:
            return 1
        return None
    mid = size //2
    if arr[mid]==obj:
        return mid

    if arr[mid]>obj:
        return bin_search(arr[:mid], obj)
    else:
        rec = bin_search(arr[mid:], obj)
        if rec is None:
            return None
        return rec + mid


def test_bin():
    assert bin_search([20],20) == 0
    assert bin_search([20, 30],20) == 0
    assert bin_search([20, 30],30) == 1
    assert bin_search([20, 30],25) == None
    assert bin_search([2, 3, 4],2) == 0

    assert bin_search([1,5,10,20,50],1) == 0
    assert bin_search([1,5,10,20,50],5) == 1
    assert bin_search([1,5,10,20,50],10) == 2
    assert bin_search([1,5,10,20,50],20) == 3
    assert bin_search([1,5,10,20,50],50) == 4

    assert bin_search([1,5,10,20],1) == 0
    assert bin_search([1,5,10,20],5) == 1
    assert bin_search([1,5,10,20],10) == 2
    assert bin_search([1,5,10,20],20) == 3
    assert bin_search([1,5,10,20],50) == None
