import pytest
from pdb import set_trace

def _is_mango_seller(name):
    return name == "peggy"

def search(graph, init):
    to_ask = [init]
    searched = []
    i = 0 # debug
    while to_ask:
        name = to_ask.pop(0)
        if name in searched:
            continue
        i+=1
        if _is_mango_seller(name):
            return name
        neigh =graph[name]
        to_ask.extend(neigh)
        searched.append(name)
    return None

@pytest.fixture
def graph():
    return {
        "you" : {"alice", "bob", "claire"},
        "bob" : {"anuj", "peggy"},
        "alice" : {"peggy",},
        "claire" : {"thom","jonny"},
        "anuj" : {},
        "peggy" : {},
        "thom" : {},
        "jonny" : {},
    }

@pytest.fixture
def graph_infinite():
    return {
        "you" : {"anuj"},
        "anuj" : {"you"},
    }




def test(graph):
    assert search(graph,'you') == 'peggy'
    assert search(graph,'bob') == 'peggy'
    assert search(graph,'claire') == None

def test_infinite(graph_infinite):
    #import pdb; pdb.set_trace()
    assert search(graph_infinite,'you') == None

