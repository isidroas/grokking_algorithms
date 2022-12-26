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
    seen: bool = False
    cost: int = math.inf  # or -1 for inf
    parent: str = None




def _search_lower_cost(state):
    node = None
    for n in state.values():
        if n.seen or n.cost is None:
            continue

        if node is None:
            node = n
            continue

        if n.cost < node.cost:
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
