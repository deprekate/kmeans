#kmeans
A python implementation of the kmeans algorithm that functions as a drop in for sklearn
This way you include this script in with your tarballed python code, so users wont have to seperately install sklearn

To use, simply include the kmeans.py file in the root directory with your code, and import it.

Then use it the same as you would calls sklearn:
```sh
>>> from sklearn.cluster import KMeans
>>> import numpy as np
>>> X = np.array([[1, 2], [1, 4], [1, 0],
...               [4, 2], [4, 4], [4, 0]])
>>> kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
>>> kmeans.labels_
array([0, 0, 0, 1, 1, 1], dtype=int32)
>>> kmeans.predict([[0, 0], [4, 4]])
array([0, 1], dtype=int32)
>>> kmeans.cluster_centers_
array([[ 1.,  2.],
       [ 4.,  2.]])
```
