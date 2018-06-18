from kmeans import KMeans

X = [[1, 2], [1, 4], [1, 0],[4, 2], [4, 4], [4, 0]]

kmeans = KMeans(n_clusters=2).fit(X)
print kmeans.labels_
print kmeans.cluster_centers_

