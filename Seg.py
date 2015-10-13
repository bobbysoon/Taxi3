from Vec2 import Vec2
from SegSegIntersect import SegSegIntersect

class Seg(tuple):
	def __new__(self, r1,r2=None):
		if type(r2) is None: r1,r2=r1
		r1x,r1y=r1;r2x,r2y=r2
		return tuple.__new__(Seg, (Vec2(r1x,r1y),Vec2(r2x,r2y)) )

	def intersect(self,other):
		if other.__class__ is Seg:	return SegSegIntersect(other,self)
		if other.__class__ is Ray:	return RaySegIntersect(other,self)
		if other.__class__ is Line:	return SegLineIntersect(self,other)

