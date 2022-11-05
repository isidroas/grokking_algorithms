def bin_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (high + low) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


def test_positive():
    assert bin_search([3, 20, 53, 85, 20], 3) == 0
    assert bin_search([3, 20, 53, 85, 20], 20) == 1
    assert bin_search([3, 20, 53, 85, 20], 53) == 2
    assert bin_search([3, 20, 53, 85, 97], 85) == 3
    assert bin_search([3, 20, 53, 85, 97], 97) == 4


def test_negative_down():
    assert bin_search([3, 20, 53, 85, 97], 2) == None
    assert False


def test_negative_up():
    assert bin_search([3, 20, 53, 85, 97], 98) == None


def test_negative_middle():
    assert bin_search([3, 20, 53, 85, 97], 54) == None
