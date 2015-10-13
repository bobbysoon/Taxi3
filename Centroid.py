from Vec2 import Vec2

from Bounds import Bounds

from mDist import mDist

class Centroid(Vec2):
	ID=0
	centroids=[] # a convenient place to keep them

	@classmethod
	def reset(cls):
		for c in Centroid.centroids:
			c.clear()

	def clear(self):
		self.verts=list()
		self.neighbors=set()
		self.neighborVerts=dict()
		self.isClosed= True

	@classmethod
	def at(cls,p):
		dists= [ (mDist(p,c),c) for c in Centroid.centroids ]
		return [p for d,p in sorted(dists,key=lambda x: x[0])][0]

	@classmethod
	def region(cls,p):
		return cls.at(p)

	def __new__(cls, *args, **kwargs):
		instance= Vec2.__new__(cls, *args, **kwargs )
		instance.ID= Centroid.ID ; Centroid.ID+=1
		instance.clear()
		return instance

	#	called after border intersects
	def addCornerVert(self): # because we can
		for p in Bounds.corners:
			if Centroid.region(p)==self:
				self.verts.append(p)

	def addNeighbor(self, n, v):
		self.neighbors.add(n)
		if not n in self.neighborVerts:
			self.neighborVerts[n]=set()
		self.neighborVerts[n].add(tuple(v))

