import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram , linkage , fcluster
from sklearn.datasets import make_blobs
"""pip install scipy"""

x ,y = make_blobs(n_samples=50, centers=3, cluster_std=1.0, random_state=42)
model = linkage(x, method='ward')

plt.figure(figsize=(10,7))
dendrogram(model, orientation='bottom', distance_sort='ascending',show_leaf_counts=True)
plt.title("Hierarchial Clustering")
plt.show()

max_clusters = 3
clusters = fcluster(model,max_clusters, criterion="maxclust" )
plt.scatter(x[:,0], x[:,1], c=clusters, cmap='prism')
plt.show()
