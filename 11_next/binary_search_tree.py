from dataclasses import dataclass


@dataclass
class Node:
    value: str
    parent: "Node" = None
    left: "Node" = None
    right: "Node" = None


def search(tree, node):
    if tree.value == node:
        return True

    if node < tree.value:
        return False if tree.left is None else search(tree.left, node)

    if  node > tree.value:
        return False if tree.right is None else search(tree.right, node)


def test_tree():
    # https://www.epdata.es/datos/nombres-apellidos-mas-frecuentes-espana-ine/373#:~:text=Antonio%20y%20Mar%C3%ADa%20Carmen%20siguen,son%20Antonio%2C%20Manuel%20y%20Jos%C3%A9.
    # tree = Node('Laura', None, Node('Cristina',None,None,None), Node('Maria Jose',None,None))

    #    tree = [
    #                   'jose',
    #             ['David', 'Miguel'],
    # ['Alejandro', 'Javier', 'Juan', 'Pedro']
    #        ]
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

    assert search(root, "Javier") == True
    assert search(root, "Manolo") == False

    #assert insert("Manolo")
    #assert search("Manolo") == True
