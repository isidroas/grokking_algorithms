import pytest
from mine import *

@pytest.fixture
def graph():
    return {
        "START": {"A": 6, "B": 2},
        "A": {"FIN": 1},
        "B": {"FIN": 5, "A": 3},
        "FIN": {},
    }


def test_simple(graph):
    assert dijkstra(graph, "START") == {
        "START": 0,
        "B": 2,
        "A": 5,
        "FIN": 6,
    }


def test_cycle():
    dijkstra({"START": {"FIN": 1}, "FIN": {"START": 1}}, "START")


def test_not_edges():
    with pytest.raises(KeyError):
        dijkstra({"START": {"FIN": 1}}, "START")


def test_not_rechable():
    dijkstra({"START": {"FIN": 1},"FIN": {"START": 1}, "A": {"B": 1}, "B": {"A": 1}}, "START")
    dijkstra({"START": {},"FIN": {}, "A": {}}, "START")


#def test_path(graph):
#    assert dijkstra2(graph, "START") == {
#        "B": "START",
#        "A": "B",
#        "FIN": "A",
#    }

def test_shortest_path_tree(graph):
    expected = {"START":["B"],
                "B":["A"],
                "A":["FIN"],
                "FIN":[]}
    assert shortest_path_tree(graph, "START") == expected

#def test_shortest_path(graph):
#    shortest_path(graph, "START","FIN") == ["START", "B", "A", "FIN"]
#    shortest_path(graph, "START","A") == ["START", "B", "A"]
