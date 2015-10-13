from Vec2 import Vec2
class Bounds:
	def __init__(self, P):
		xa,ya=zip(*P)
		#	n*1.25, because a centroid == Bounds.corner screws with vert
		#	 ordering (by angle - currently handled in SF*Region.__init__)
		Bounds.xMin,Bounds.yMin,Bounds.xMax,Bounds.yMax = [n*1.25 for n in [min(xa),min(ya),max(xa),max(ya)]]
		Bounds.corners= [(Bounds.xMin,Bounds.yMin),(Bounds.xMax,Bounds.yMin),(Bounds.xMax,Bounds.yMax),(Bounds.xMin,Bounds.yMax)]
		Bounds.boundingBox= Vec2(Bounds.xMin,Bounds.yMin),Vec2(Bounds.xMax,Bounds.yMax) # to initialize window.view with
