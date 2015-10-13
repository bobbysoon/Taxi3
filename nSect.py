from mDist import mDist
from Centroid import Centroid

epsilon=1e-03

def nSect(p, ca):
	dists= [mDist(c,p) for c in ca]
	minDist,maxDist = min(dists),max(dists)
	if maxDist-minDist>epsilon: return False
	for c in Centroid.centroids:
		if not c in ca:
			if mDist(c,p) <= minDist:
				return False
	return True

