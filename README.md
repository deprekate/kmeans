# kmeans
A python implementation of the kmeans algorithm that functions as a drop in for sklearn, albeit more slow.

This way you just include this script in with your tarballed python code, and users won't have to separately install sklearn

To use, simply include the **kmeans.py** file in the root directory with your code, and import it.

Then use it the same as you would call sklearn:
```sh
>>> from kmeans import KMeans
>>> X = [[1, 2], [1, 4], [1, 0],[4, 2], [4, 4], [4, 0]]
>>> kmeans = KMeans(n_clusters=2).fit(X)
>>> kmeans.labels_
[0, 0, 0, 1, 1, 1]
>>> kmeans.cluster_centers_
[[1.0, 2.0], [4.0, 2.0]]
```
