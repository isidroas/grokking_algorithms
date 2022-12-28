from typing import Set
def minimize_sets(sets: Set[Set[int]]):
    """
    Also, maximize covering (or take it all)
    Reducing overlaping
    """
    res:  Set[Set[int]] = set()
    covering:Set[int]  = set()

    while True:
        next_set = None
        for s in sets:
            # search for the best next set
            if s.issubset(covering):
                continue
            added = s ^ covering
            if next_set is None or len(added) > len(next_set ^ covering):
                next_set = s
        if next_set is None:
            break

        covering |= next_set
        res.add(next_set)

    return res





def test_set_covering():
    s1 = frozenset({1, 2, 3})
    s2 = frozenset({2, 3, 4})
    s3 = frozenset({3, 4, 5})
    s4 = frozenset({4, 5, 6})
    s5 = frozenset({5, 6, 7})

    # can not predict the order
    assert minimize_sets({s1, s2, s3, s4, s5}) == {s1, s2, s5}
