def binary_search(arr, target):
    if not arr:
        return -1        
    if len(arr) == 1 and arr[0] == target:
        return arr[0]
    if len(arr) == 1 and arr[0] != target:
        return -1
    low = 0         
    high = len(arr) - 1    
    mid = (low + high) // 2

    if arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid+1:], target)

def test_bin():
    assert binary_search([20],20) == 0
    assert binary_search([20, 30],20) == 0
    assert binary_search([20, 30],30) == 1
    assert binary_search([20, 30],25) == None
    assert binary_search([2, 3, 4],2) == 0

    assert binary_search([1,5,10,20,50],1) == 0
    assert binary_search([1,5,10,20,50],5) == 1
    assert binary_search([1,5,10,20,50],10) == 2
    assert binary_search([1,5,10,20,50],20) == 3
    assert binary_search([1,5,10,20,50],50) == 4

    assert binary_search([1,5,10,20],1) == 0
    assert binary_search([1,5,10,20],5) == 1
    assert binary_search([1,5,10,20],10) == 2
    assert binary_search([1,5,10,20],20) == 3
    assert binary_search([1,5,10,20],50) == None
