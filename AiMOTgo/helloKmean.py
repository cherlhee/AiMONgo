import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans




# X: from -2 to 0
xx = -2*np.random.rand(100, 2)
# xx = np.random.rand(100, 2)


# X1: from 1 to 3
x1 = 1 + 2*np.random.rand(50, 2)



xx[50:100, :] = x1

plt.scatter(xx[:, 0], xx[:, 1])

# s: symbol size
# plt.scatter(xx[:, 0], xx[:, 1], s = 510)


# print(X)
# print(X1)




# to seek centers
Kmean = KMeans(n_clusters= 2)
Kmean.fit(xx)


# to mark centers
ptCenters = Kmean.cluster_centers_
print(ptCenters)

plt.scatter(ptCenters[0,0], ptCenters[0,1], c='r')
plt.scatter(ptCenters[1,0], ptCenters[1,1], c='r')

plt.show()