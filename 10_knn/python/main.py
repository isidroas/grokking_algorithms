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
    res = 0
    for i in range(len(p1)):
        res += (p1[i]-p2[i])**2
    return math.sqrt(res)

assert dist([1,1], [3,3])
