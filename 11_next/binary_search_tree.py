"""
TODO:
- maintain parent attribute. I makes better the deletion
"""
from dataclasses import dataclass


@dataclass
class Node:
    value: str
    parent: "Node" = None
    left: "Node" = None
    right: "Node" = None


def search(tree, node):
    if tree is None:
        return False

    if tree.value == node:
        return True

    if node < tree.value:
        return search(tree.left, node)

    if  node > tree.value:
        return search(tree.right, node)

def delete(tree, node):
    #if tree is None:
    #    raise ValueError(f'Not found {node}')

    #if tree.value == node:
    #    #return True
    #    tree.parent
    #    del tree

    if node < tree.value:
        if tree.left is None:
            raise ValueError(f'Not found {node}')
        if tree.left.value == node:
            if tree.left.left:
                tree.left = tree.left.left
            if tree.left.right:
                insert_node(tree, tree.left.right)
            del tree.left
            return
        return delete(tree.left, node)

    if node > tree.value:
        if tree.right is None:
            raise ValueError(f'Not found {node}')
        if tree.right.value == node:
            if tree.right.left:
                tree.right = tree.right.left
            if tree.right.right:
                insert_node(tree, tree.right.right)
            del tree.right
            return
        return delete(tree.right, node)
    assert False

def insert(tree,node:str):
    if node < tree.value:
        if tree.left is None:
            tree.left = Node(node)
            return
        return insert(tree.left, node)

    if node > tree.value:
        if tree.right is None:
            tree.right = Node(node)
            return
        return insert(tree.right, node)

    if node == tree.value:
        raise ValueError(f'node {node} already exists')


def insert_node(tree,node:Node):
    if node.value < tree.value:
        if tree.left is None:
            tree.left = node
            return
        return insert(tree.left, node)

    if node.value > tree.value:
        if tree.right is None:
            tree.right = node
            return
        return insert(tree.right, node)

    if node.value == tree.value:
        raise ValueError(f'node {node} already exists')

def minimum(tree):
    res = tree.left
    while res.left:
        res = res.left
    return res.value

def maximum(tree):
    res = tree.right
    while res.right:
        res = res.right
    return res.value

def traverse(tree):
    res = []

    if tree is None:
        return []

    res.extend(traverse(tree.left))
    res.append(tree.value)
    res.extend(traverse(tree.right))

    return res

def depth(root):
    if root is None:
        return 0
    max_depth = 1 +max(depth(root.left), depth(root.right))
    return max_depth
    

def test_tree():
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

    assert search(root, "Javier") == True
    assert search(root, "Manolo") == False

    insert(root,"Manolo")
    assert search(root,"Manolo") == True

    assert minimum(root) == 'Alejandro'
    assert maximum(root) == 'Pedro'
    assert traverse(root) == ['Alejandro', 'David','Javier', 'Jose','Juan', 'Manolo', 'Miguel', 'Pedro']

    delete(root,"Manolo")
    assert search(root,"Manolo") == False
    assert depth(root) == 3
