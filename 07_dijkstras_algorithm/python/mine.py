from pprint import pprint
from dataclasses import dataclass
from typing import Dict
graph = {
    "START": {"A": 6, "B": 2},
    "A": {"FIN": 1},
    "B": {"FIN": 5, "A": 3},
    "FIN": {},
}

@dataclass
class Node:
    name: str
    seen: bool = False
    cost: int = None # or -1 for inf
    parent: str = None



def _dijkstra(graph, init):
    #state: Dict[str, Node]
    state: Dict[str, Node] = {k:Node(k) for k in graph}

    state[init].cost=0
    while True:
        node = None
        for n in state.values():
            if n.seen or n.cost is None:
                continue

            if node is None:
                node = n
                continue

            if n.cost < node.cost:
                node = n

        if node is None:
            break



        for neigh_name, cost in graph[node.name].items():
            neigh = state[neigh_name]

            total_cost = node.cost + cost

            if neigh.cost is None or neigh.cost > total_cost:
                assert not neigh.seen, "something went wrong"
                neigh.cost = total_cost
                neigh.parent = node.name

        node.seen = True
        #pprint(list(state.values()))

    #pprint(graph)
    #pprint(state)
    return state

def dijkstra(graph, init):
    state = _dijkstra(graph, init)
    return {n.name:n.cost for n in state.values()}

def test():
    assert dijkstra(graph, "START") == {
        "START": 0,
        "B": 2,
        "A": 5,
        "FIN": 6,
    }

    # TODO: test cycles

def test_path():
    assert dijkstra2(graph, "START") == {
        "B": "START",
        "A": "B",
        "FIN": "A",
    }
