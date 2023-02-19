import pytest
from binary_search_tree import *

@pytest.fixture
def tree_of_names():
    # https://www.epdata.es/datos/nombres-apellidos-mas-frecuentes-espana-ine/373#:~:text=Antonio%20y%20Mar%C3%ADa%20Carmen%20siguen,son%20Antonio%2C%20Manuel%20y%20Jos%C3%A9.
    # tree = Node('Laura', None, Node('Cristina',None,None,None), Node('Maria Jose',None,None))

    #    tree = [
    #                   'jose',
    #             ['David', 'Miguel'],
    # ['Alejandro', 'Javier', 'Juan', 'Pedro']
    #        ]
    """
                  ┌ Alejandro
         ┌─ David ┤
         │        └─── Javier
    Jose ┤
         │        ┌───── Juan
         └ Miguel ┤
                  └──── Pedro
    """
    jose = Node("Jose")
    david = Node("David")
    miguel = Node("Miguel")
    alejandro = Node("Alejandro")
    javier = Node("Javier")
    juan = Node("Juan")
    pedro = Node("Pedro")

    jose.parent = None
    jose.left, jose.right = david, miguel
    david.left, david.right, miguel.left, miguel.right = (
        alejandro,
        javier,
        juan,
        pedro,
    )
    root = jose
    return root


def test_search(tree_of_names):
    assert search(tree_of_names, "Javier") == True
    assert search(tree_of_names, "Manolo") == False

def test_search_loop(tree_of_names):
    assert search_loop(tree_of_names, "Javier").value == "Javier"
    assert search_loop(tree_of_names, "Manolo") == None

def test_insert(tree_of_names):
    insert(tree_of_names, "Manolo")
    assert search(tree_of_names, "Manolo") == True

def test_minimum(tree_of_names):
    assert minimum(tree_of_names) == "Alejandro"
def test_maximum(tree_of_names):
    assert maximum(tree_of_names) == "Pedro"

def test_traverse(tree_of_names):
    insert(tree_of_names, "Manolo")
    assert traverse(tree_of_names) == [
        "Alejandro",
        "David",
        "Javier",
        "Jose",
        "Juan",
        "Manolo",
        "Miguel",
        "Pedro",
    ]

def test_delete(tree_of_names):
    insert(tree_of_names, "Manolo")
    delete(tree_of_names, "Manolo")
    assert search(tree_of_names, "Manolo") == False

def test_depth(tree_of_names):
    assert depth(tree_of_names) == 3

def test_is_full(tree_of_names):
    assert is_full(tree_of_names) == True
    insert(tree_of_names, "Manolo")
    assert is_full(tree_of_names) == False

def test_is_full2(tree_of_names):
    assert is_full2(tree_of_names) == True
    insert(tree_of_names, "Manolo")
    assert is_full2(tree_of_names) == False
