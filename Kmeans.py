from copy import deepcopy
import numpy as np
import pandas as pd

data = pd.read_csv('Data.csv')
print("Input Data and Shape")
print(data.shape)
data.head()

f1 = data['Value'].values
X = np.array(f1)

print(X)

def dist(a, b, ax = 0):
    return np.linalg.norm(a - b, axis=ax)

k = 3
C_x = np.random.randint(0, np.max(X), size=k)

C = np.array(C_x,dtype=np.float32)
print(C)

C_old = np.zeros(C.shape)
clusters = np.zeros(len(X))
error = dist(C, C_old, None)
K = np.zeros(len(C))
index_mi = 0
Sum = 0
algo_it = 0
C_old = np.zeros(len(C))
#print error
while error != 0:
	for i in range(len(C)):
			C_old[i] = C[i]
			pass
	for i in range(len(X)):
		for j in range(len(C)):
			K[j] = dist(X[i],C[j],None)
			#print(K)
			pass
			mi = min(K)
			for it in range(len(K)):
				if K[it] == mi:
					index_mi = it
					clusters[i] = C[index_mi]
		pass
	pass
	
	it_c = 0
	for j in range(len(C)):
		Sum = 0
		count = 0
		for i in range(len(X)):
			if clusters[i] == C[j]:
				Sum += X[i]
				count = count+1
				pass
		C[j] = Sum/count
		it = it+1
		pass
	error = dist(C,C_old,None)
	algo_it = algo_it+1
pass

print(C)
print(X)
print(clusters)
print(algo_it)

