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

    if node > tree.value:
        return search(tree.right, node)

def search_loop(tree, value):
    node = tree
    while node is not None and node.value != value:
        node = node.left if value < node.value else  node.right
    return node

def delete(tree, node):
    # if tree is None:
    #    raise ValueError(f'Not found {node}')

    # if tree.value == node:
    #    #return True
    #    tree.parent
    #    del tree

    if node < tree.value:
        if tree.left is None:
            raise ValueError(f"Not found {node}")
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
            raise ValueError(f"Not found {node}")
        if tree.right.value == node:
            if tree.right.left:
                tree.right = tree.right.left
            if tree.right.right:
                insert_node(tree, tree.right.right)
            del tree.right
            return
        return delete(tree.right, node)
    assert False


def insert(tree, node: str):
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
        raise ValueError(f"node {node} already exists")


def insert_node(tree, node: Node):
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
        raise ValueError(f"node {node} already exists")


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
    max_depth = 1 + max(depth(root.left), depth(root.right))
    return max_depth


def is_full(root):
    childs = 0
    if root.left:
        if not is_full(root.left):
            return False
        childs += 1
    if root.right:
        if not is_full(root.right):
            return False
        childs += 1

    return childs in (0,2)


def is_full2(root):
    if root.left and root.right:
        return is_full2(root.left) and is_full2(root.right)
    return not root.left and not root.right
