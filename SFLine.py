import sfml as sf

from Hue import *

class SFLine(sf.VertexArray):
	def __init__(self, p0,p1, hue=Green, s=1.0, v=1.0, a=1.0):
		sf.VertexArray.__init__(self, sf.PrimitiveType.LINES_STRIP, 2 )

		self[0].position= p0
		self[1].position= p1
		col= Hue(hue, s=s, v=v, a=a)
		self[0].color=col
		self[1].color=col

