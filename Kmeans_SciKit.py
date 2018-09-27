import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.cluster as sk
plt.rcParams['figure.figsize'] = (16,9)
plt.style.use('ggplot')

data = pd.read_csv('data.csv')
print('Input Data and Shape')
print(data.shape)
data.head()
print (data.columns)

feature1 = data[data.columns[0]].values
feature2 = data[data.columns[1]].values
print('feature1 is Volume')
print('feature2 is Average Average price')
X = np.array(list(zip(feature1,feature2)))
plt.scatter(feature1, feature2, c='red', s=7 )
plt.show()

kmeans = sk.KMeans(n_clusters = 3)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_

plt.scatter(feature1, feature2, c=labels, cmap = 'viridis')
plt.show()
print (centroids)