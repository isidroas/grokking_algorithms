"""
iris database (flowers)
"""
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import math
import operator
from  collections import Counter

data = datasets.load_iris()

X = np.array(data["data"])
y = np.array(data["target"])
CLASSES = data["target_names"]

print(f"{CLASSES=}")
print(f"{X[0]=}")
print(f"{y=}")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

def dist(p1, p2):
    """
    >>> dist([1,1], [3,3])
    2.8284271247461903
    >>> dist([1,2], [4,6])
    5.0
    """
    res = 0
    for i in range(len(p1)):
        res += (p1[i]-p2[i])**2
    return math.sqrt(res)

def _distances(X_train, y_train, X_test):
    res =[]
    for x, y in zip(X_train, y_train):
        res.append((dist(x,X_test), y))
    return res

def _sort_dist(list_):
    list_.sort(key=lambda x:x[0])
    return list_


def _get_mode(classes):
    c = Counter(classes)
    return c.most_common(1)[0][0]

def classify(X_train, y_train, X_test, k=5)-> int:
    dist = _distances(X_train, y_train, X_test)
    sort = _sort_dist(dist)
    classes = (x[1] for x in sort[:k])
    mode = _get_mode(classes)
    return mode

def get_error(X_train, y_train, X_test, y_test, k=5):
    corrects=0
    for x, y_real in zip(X_test, y_test):
        y_estimated = classify(X_train, y_train, x, k=k)
        if y_real == y_estimated:
            corrects +=1
    return 1 - corrects/len(y_test)

def test_distances():
    assert _distances(X_train = [(2,2),(1,4)],y_train=(0,1), X_test = (1,2)) == [(1,0), (2,1)]

def test_sort():
    assert _sort_dist([(2,0), (1,1)]) == [(1,1), (2,0)]

def test_mode():
    assert _get_mode([1,2,3,2,3,1,3]) == 3
    assert _get_mode([1,1,2]) == 1

def test_classify():
    y_test_estimated = classify(X_train, y_train, [4.4, 3.1, 1.3, 1.4], k=5)
    assert CLASSES[y_test_estimated] == 'setosa' # or 0

def test_error():
    error = get_error(X_train, y_train, X_test, y_test, k=5)
    assert 0 <=error<=1



if __name__=="__main__":
    pass

    #y_test_estimated = classify(X_train, y_train, X_test, k=)
    #error = calculate_error_rate(y_test_estimated, y_test)


