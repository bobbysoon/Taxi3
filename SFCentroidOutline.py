import sfml as sf

from angle import angle

class SFCentroidOutline(sf.VertexArray):
	def __init__(self, c):
		verts= [(angle(c,v),v) for v in c.verts]
		verts= sorted( verts , key=lambda x: x[0] )
		verts= [v for a,v in verts]
		verts.append(verts[0])

		sf.VertexArray.__init__(self, sf.PrimitiveType.LINES_STRIP, len(verts) )

		col= sf.Color(32,32,32)
		for i in range(len(verts)):
			self[i].color=col
			self[i].position= verts[i]

