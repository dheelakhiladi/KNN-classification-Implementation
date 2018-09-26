from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Importing the dataset
data = pd.read_csv('Data.csv')
print("Input Data and Shape")
print(data.shape)
data.head()

f1 = data['Value'].values
X = np.array(f1)

def dist(a, b, ax = 0):
    return np.linalg.norm(a - b, axis=ax)

k = 3
C_x = np.random.randint(0, np.max(X), size=k)

C = np.array(C_x,dtype=np.float32)
print(C)

C_old = np.zeros(C.shape)
clusters = np.zeros(len(X))
error = dist(C, C_old, None)

while error != 0:
    for i in range(len(X)):
        distances = dist(X[i],C,None)
        cluster = np.argmin(distances)
        clusters[i] = cluster
    C_old = deepcopy(C)
    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == i]
        S = sum(points)
        C[i] = S/len(points)    
    error = dist(C, C_old, None)

print(clusters)
print(C)
