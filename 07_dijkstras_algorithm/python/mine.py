graph = {
    "start": {"A": 6, "B": 2},
    "A": {"FIN": 1},
    "B": {"FIN": 5, "A": 3},
}


def dijkstra(graph, init):
    pass


def test():
    assert dijkstra(graph, "START") == {
        "start": 0,
        "B": 2,
        "A": 5,
        "FIN": 6,
    }


def test_path():
    assert dijkstra2(graph, "START") == {
        "B": "START",
        "A": "B",
        "FIN": "A",
    }
