"""
This code is intended to be similar to the human way of doing the
algorithim. The best way to learn is to take a paper and draw a table in wich
each row is a node.

The computational speed is less priorized
"""
import collections
import logging
import math
from dataclasses import dataclass
from pprint import pformat

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


@dataclass
class Node:
    name: str

    # Already seen. The cost indicated should be definitive
    seen: bool = False

    # Cost from initial node
    cost: int = math.inf

    # Parent of the path used to calculate cost
    parent: str = None


class Table(collections.UserList):
    def get(self, name):
        """
        Search node by name
        >>> Table([
        ...         Node("A"),
        ...         Node("B"),
        ...       ]).get("B")
        Node(name='B', seen=False, cost=inf, parent=None)
        """
        for node in self.data:
            if node.name == name:
                return node
        raise KeyError(f"Node {name} not in {self}")

    def __str__(self):
        return pformat(self.data)

    def format_table(self, headers=False, style="grid"):
        from tabulate import tabulate

        rows = ((row.name, row.seen, row.cost, row.parent) for row in self)
        headers = ("name", "seen", "cost", "parent") if headers else ()
        return tabulate(rows, headers=headers, tablefmt="grid")


def _search_lower_cost(table):
    """
    >>> table = [
    ...             Node("A", seen = True,  cost = 1),
    ...             Node("B", seen = False, cost = 3),
    ...             Node("C", seen = False, cost = 2),
    ... ]
    >>> _search_lower_cost(table)
    Node(name='C', seen=False, cost=2, parent=None)
    """
    node = None
    for n in table:

        if n.seen:
            continue

        if node is None or n.cost < node.cost:
            node = n

    return node


def _dijkstra(graph, init: str) -> Table:
    table = Table(Node(k) for k in graph)
    table.get(init).cost = 0

    while node := _search_lower_cost(table):

        for neigh_name, cost in graph[node.name].items():
            neigh = table.get(neigh_name)

            total_cost = node.cost + cost

            if neigh.cost > total_cost:
                assert not neigh.seen, "_search_lower_cost didn't do its job right"
                neigh.cost = total_cost
                neigh.parent = node.name

        node.seen = True

        if LOG.isEnabledFor(logging.DEBUG):
            _debug_table(node, table)

    return table


def dijkstra(graph, init):
    table = _dijkstra(graph, init)
    return {n.name: n.cost for n in table}


def shortest_path_tree(graph, init):
    table = _dijkstra(graph, init)

    tree = {}  # Dict[parent: childs]
    for node in table:
        # get childs
        tree[node.name] = [n.name for n in table if n.parent == node.name]
    return tree


def shortest_path(graph, init, final):
    table = _dijkstra(graph, init)

    res = []
    node = table.get(init)
    res.append(node.name)
    while node.name != init:
        node = table.get(node.parent)
        res.append(node.name)
    return res


def _debug_table(node, table, tabular=True):
    from textwrap import indent
    no_indented = table.format_table() if tabular else str(table)
    indented = indent(no_indented, "\t\t")
    LOG.debug("node=%s, table=\n%s", node.name, indented)
