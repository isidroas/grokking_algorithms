"""
iris database (flowers)
"""
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import math

data = datasets.load_iris()

X = np.array(data["data"])
y = np.array(data["target"])
classes = data["target_names"]

print(f"{classes=}")
print(f"{X[0]=}")
print(f"{y=}")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

def dist(p1, p2):
    """
    >>> dist([1,1], [3,3])
    2.8284271247461903
    """
    res = 0
    for i in range(len(p1)):
        res += (p1[i]-p2[i])**2
    return math.sqrt(res)

def classify(X_train, y_train, X_test)-> int:
    pass

if __name__=="__main__":
    #y_test_estimated = classify(X_train, y_train, X_test, k=)
    #error = calculate_error_rate(y_test_estimated, y_test)
    y_test_estimated = classify(X_train, y_train, [4.4, 3.1, 1.3, 1.4], k=5) == 'setosa'



