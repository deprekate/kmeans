from kmeans import KMeans

def column(matrix, i):
	return [row[i] for row in matrix]

def mean(data):
	"""Return the sample arithmetic mean of data."""
	n = len(data)
	if n < 1:
		raise ValueError('mean requires at least one data point')
	return sum(data)/n # in Python 2 use sum(data)/float(n)

def _ss(data):
	"""Return sum of square deviations of sequence data."""
	c = mean(data)
	ss = sum((x-c)**2 for x in data)
	return ss

def stddev(data, ddof=0):
	"""Calculates the population standard deviation
	by default; specify ddof=1 to compute the sample
	standard deviation."""
	n = len(data)
	if n < 2:
		raise ValueError('variance requires at least two data points')
	ss = _ss(data)
	pvar = ss/(n-ddof)
	return pvar**0.5



x = [[1, 2], [1, 4], [1, 0],[4, 2], [4, 4], [4, 0]]
matrix = []
points = []
initial = []
m = []
s = []
file = open("NC_000867.med", "r")
file.next()
for line in file:
    row = []
    line_array = line.rstrip().split("\t")
    for aa in line_array[2:]:
            row.append(float(aa))
    matrix.append(row)
for i in range(0,20):
    col = column(matrix,i)
    m.append(mean(col))
    s.append(stddev(col))
#normalize
file.seek(0)
file.next()
for line in file:
    point = []
    line_array = line.rstrip().split("\t")
    for i, aa in enumerate(line_array[2:]):
            point.append( (float(aa)-m[i])/s[i] )
    points.append(point)


kmeans = KMeans(n_clusters=2).fit(x)
#print kmeans.labels_
#print kmeans.cluster_centers_
