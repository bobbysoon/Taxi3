from Centroid import Centroid
from Bounds import Bounds
from Border import Border
from DistSort import DistSort
from Vec2 import Vec2

class Taxi:
	def __init__(self, centroids):
		Centroid.centroids= centroids

		Bounds(centroids)

		Border.reset() # starting over each frame
		Centroid.reset() # starting over each frame

		for n1 in range(1,len(Centroid.centroids)):
			c1= Centroid.centroids[n1]
			# dist-sort, & break when c1 in enclosed
			others= DistSort(c1, [Centroid.centroids[n2] for n2 in range(n1)] )
			B=[]
			for c2 in others:
				b= Border(c1,c2)
				for bb in B:
					if bb.nIntersects<2:
						i= b.validate_BorderBorderIntersectPoint(bb)
						if i and b.nIntersects==2:
								break
				B.append(b)
				if {bb.nIntersects for bb in B}=={2}:
					break

		for c in Centroid.centroids:
			if not c.isClosed:
				c.addCornerVert()


