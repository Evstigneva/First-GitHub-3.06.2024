import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs

x, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

dbscan = DBSCAN(eps=0.3, min_samples=5)

y_dbscan = dbscan.fit_predict(x)

plt.scatter(x[:, 0], x[:, 1], c=y_dbscan, cmap='viridis')
plt.title("DBSCAN Clustering")
plt.show()