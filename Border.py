from Bounds import Bounds
from sgn import sgn
from Seg import Seg
from nSect import nSect

class Border:
	IntersectsTested=[] # 2 out of three border-border intersects are redundant
	borders=[] # a convenient place to keep them

	@classmethod
	def reset(cls):
		Border.IntersectsTested=[]
		Border.borders=[]

	@classmethod
	def clear(cls):
		for b in Border.borders:
			b.nIntersects=0
			b.intersectsBounds=False

	@classmethod
	def of(cls, centroids):
		for b in Border.borders:
			if b.centroids==centroids:
				return b
		raise

	#	create a 'line' perpendicular to 'line' (c1,c2), in manhattan metric
	def __init__(self, c1,c2 ):
		self.centroids= {c1,c2}
		Border.borders.append(self)

		xMin,yMin = Bounds.xMin,Bounds.yMin
		xMax,yMax = Bounds.xMax,Bounds.yMax

		x1,y1=c1 ; x2,y2=c2
		dx,dy= x2-x1 , y2-y1
		ax,ay= abs(dx),abs(dy)
		a= min(ax,ay)
		sx,sy= sgn(dx),sgn(dy)
		o= a*sx/2,-a*sy/2
		cp= (c1+c2)/2.0
		p1,p2 = cp+o,cp-o # this is the 45 degree sloping middle segment

		#	now make the outer segments, extending from the sloping
		#	middle segment to the bounding box. They'll both be either
		#	horizontal or vertical, opposite the greater difference axis
		if ax>ay:	# vertical
			p0= p1.x, yMin if p1.y<p2.y else yMax
			p3= p2.x, yMin if p2.y<p1.y else yMax
		else:		# horizontal
			p0= xMin if p1.x<p2.x else xMax, p1.y
			p3= xMin if p2.x<p1.x else xMax, p2.y

		self.lines= [Seg(p0,p1),Seg(p1,p2),Seg(p2,p3)]

		# obsolete method names follow
		# next, validate the line's segment's 4 end points for inclusion in the final geometry
		self.validateBoundaryIntersects_p0p3()
		self.validateMidPoints_p1p2()

		# After this and the other borders are created, they are intersected against each other,
		# and the intersect points are validated and included as has just been done

	def validateBoundaryIntersects_p0p3(self):
		self.nIntersects= 0
		for p in [self.lines[0][0],self.lines[2][1]]:
			if nSect(p,self.centroids):
				self.nIntersects+=1
				for c in self.centroids:
					c.verts.append(p)
					n= list(self.centroids-{c})[0]
					c.addNeighbor(n,p)
					c.isClosed= False

	def validateMidPoints_p1p2(self):
		pa=[]
		for p in [self.lines[1][0],self.lines[1][1]]:
			if nSect(p,self.centroids):
				for c in self.centroids:
					c.verts.append(p)
					n= list(self.centroids-{c})[0]
					c.addNeighbor(n,p)

	def getBorderBorderIntersectPoint(self,other):
		for l1 in self.lines:
			for l2 in other.lines:
				p= l1.intersect(l2)
				if p: return p

	#	intersect another border, and add to the geometry if validated
	def validate_BorderBorderIntersectPoint(self, other):
		if self.centroids & other.centroids: # do they have a centroid in common
			C= self.centroids | other.centroids # both's centroids. len(C)==3
			if not C in Border.IntersectsTested: # 3 centroids, 3 borders
				Border.IntersectsTested.append(C) # 3 intersect tests, 2nd and 3rd ~= 1st

				v= self.getBorderBorderIntersectPoint(other)
				if v and nSect(v,C):
					C3= self.centroids ^ other.centroids
					assert len(C3)==2,str(C3)
					third= Border.of(C3)
					self.nIntersects+=1
					other.nIntersects+=1
					third.nIntersects+=1
					for c in C:
						c.verts.append(v)
						for n in C-{c}:
							c.addNeighbor(n,v)

					return v


