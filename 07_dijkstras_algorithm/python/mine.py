import logging
import math
from dataclasses import dataclass
from logging import Logger
from pprint import pformat, pprint
from typing import Dict

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


@dataclass
class Node:
    name: str

    # Already seen. The cost indicated shoul be definitive
    seen: bool = False

    # Cost from initial node
    cost: int = math.inf

    # Parent of the path used to calculate cost
    parent: str = None

# TODO: create Table class. To avoid Dict[name, Node] ?
#    or NodeCollection


def _search_lower_cost(state):
    node = None
    for n in state.values():

        if n.seen:
            continue

        if node is None or n.cost < node.cost:
            node = n

    return node


def _dijkstra(graph, init):
    state: Dict[str, Node] = {k: Node(k) for k in graph}
    state[init].cost = 0

    node = _search_lower_cost(state)
    while node is not None:

        for neigh_name, cost in graph[node.name].items():
            neigh = state[neigh_name]

            total_cost = node.cost + cost

            if neigh.cost > total_cost:
                assert not neigh.seen, "search_lower_cost didn't do its job well"
                neigh.cost = total_cost
                neigh.parent = node.name

        node.seen = True

        if LOG.isEnabledFor(logging.DEBUG):
            _debug_state(node, state)

        node = _search_lower_cost(state)

    return state


def dijkstra(graph, init):
    state = _dijkstra(graph, init)
    return {n.name: n.cost for n in state.values()}

def shortest_path_tree(graph,init):
    state = _dijkstra(graph, init)

    tree = {} # Dict[parent: childs]
    for node in state.values():
        # get childs
        tree[node.name]= [n.name for n in state.values() if n.parent == node.name]
    return tree

def shortest_path(graph,init, final):
    state = _dijkstra(graph, init)

    res =[]
    node = state[init]
    res.append(node.name)
    while node.name != init:
        node = state[node.parent]
        res.append(node.name)
    return res

def _debug_state(node, state, table=True):
    if table:
        from tabulate import tabulate

        rows = ((row.name, row.seen, row.cost, row.parent) for row in state.values())
        headers = ("name", "seen", "cost", "parent")
        # table = tabulate(rows, headers=headers, tablefmt='grid')
        table = tabulate(rows, tablefmt="simple_grid")
        no_indented = table
    else:
        no_indented = pformat(list(state.values()))

    from textwrap import indent

    indented = indent(no_indented, "\t\t")
    LOG.debug("node=%s, state=\n%s", node.name, indented)
