"""
https://en.wikipedia.org/wiki/Tree_structure#Representing_trees
"""
def list_of_lists():
    return [[1,2],[3,4]]

def dict_of_lists():
    return {1:
              [
                  {2:[{4:[]}, {5:[]}]},
                  {3:[{6:[]}, {7:[]}]},
              ]
           }

def nodes():
    return Node(1,
              [
                  Node(2,[Node(4), Node(5)]),
                  Node(3,[Node(6), Node(7)]),
              ])

def test(list_):
    assert pformat(list_) == r"""\
    *
   / \
  *   *
 / \ / \
1  2 3  1
"""

def test(list_):
    assert pformat(list_) == r"""\
*
│
├── *
│   ├── 1
│   └── 2
└── *
    ├── 3
    └── 4
"""


def test(list_):
    assert pformat(list_) == r"""\
       ┌─ 1
  ┌─ * ┤
  │    └─ 2
* ┤
  │    ┌─ 3
  └─ * ┤
       └─ 4\
"""

def test(list_):
    assert pformat(list_) == r"""\
     *
   ┌─┴─┐
   *   *
  ┌┴┐ ┌┴┐
  1 2 3 4\
"""
