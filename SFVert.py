import sfml as sf
from Hue import *

class SFVert:
	def __init__(self, target, hue):
		self.target= target
		self.circ= sf.CircleShape()
		self.circ.outline_color = Hue(hue,a=.25)
		self.circ.fill_color = Hue(hue,a=.5)

	def setScale(self,scale):
		self.circ.origin= scale,scale
		self.circ.radius= scale
		self.circ.outline_thickness= scale/3.0

	def draw(self, pos):
		self.circ.position= pos
		self.target.draw(self.circ)
