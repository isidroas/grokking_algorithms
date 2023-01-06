def longest_common_substring(str1, str2):
    grid = _grid(str1, str2)
    max1 = (max(row) for row in grid)
    return max(max1)

def longest_common_substring2(str1, str2):
    grid = _grid(str1, str2)
    max1 = 0
    mrow = None
    mcolumn = None
    for row, char1 in enumerate(str1):
        for column, char2 in enumerate(str2):
            cel = grid[row][column]
            if cel>=max1:
                max1 = cel
                mrow=row
                mcolumn = column

    return str1[mrow-max1+1:mrow+1]

def _grid(str1, str2):
    """
    |   | s | t | r | 2 |
    |---+---+---+---+---|
    | s | 0 |   |   |   |
    | t |   | 1 |   |   |
    | r |   |   | 2 |   |
    | 1 |   |   |   | 3 |
    """

    grid = [[None for i in range(len(str2)) ] for j in range(len(str1))]
    for row, char1 in enumerate(str1):
        for column, char2 in enumerate(str2):
            #print(locals())
            #import pdb;pdb.set_trace()
            if char1 == char2:
                try:
                    grid[row][column] = grid[row-1][column-1] + 1
                except IndexError:
                    grid[row][column] =  1
            else:
                grid[row][column] =  0
    print(grid)
    return grid


def test():
    #assert 'ish' = longest_common_substring('fish', 'hish')

    expected =[
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 2, 0],
        [0, 0, 0, 3],
    ]
    #assert expected == _grid('fish', 'hish')
    assert 3 == longest_common_substring('fish', 'hish')
    assert 'ish' == longest_common_substring2('fish', 'hish')
