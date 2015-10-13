import sfml as sf

from sys import argv
from Centroid import Centroid

from SFVert import SFVert
from SFCentroidOutline import SFCentroidOutline
from SFLine import SFLine

from Hue import *

class Demo:
	def __init__(self, swarm, size=(800,600)):
		self.swarm= swarm
		self.window= sf.RenderWindow( sf.VideoMode(*size) , argv[0] )
		w= self.window
		self.view= w.view
		self.is_open= w.is_open
		self.close= w.close
		self.paused= False
		self.clock = sf.Clock()
		self.sfVert= SFVert(self.window, Red)
		self.sfNVert= SFVert(self.window, Blue)
		self.view.size=2,2
		self.view.center=0,0
		self.drawNeighbors= True
		self.drawCentroids= True
		self.drawPolies= True

	def draw(self, taxi):
		self.scale= self.view.size.x/self.window.size.x
		self.sfVert.setScale(self.scale*2.5)
		self.sfNVert.setScale(self.scale*2.5)

		self.window.clear()
		for c in Centroid.centroids: self.drawCentroid(c)
		self.window.display()

		self.processEvents()

	def drawCentroid(self, c):
		if self.drawNeighbors:
			for n in c.neighborVerts:
				xa,ya=zip(*c.neighborVerts[n])
				cx=(min(xa)+max(xa))/2
				cy=(min(ya)+max(ya))/2
				self.window.draw(SFLine(c,(cx,cy), hue=.75, s=0.5, v=.25))
		if self.drawPolies:
			self.window.draw(SFCentroidOutline(c))
		if self.drawCentroids:
			self.sfVert.draw(c)

	def processEvents(self):
		for e in self.window.events:
			if type(e) is sf.CloseEvent: exit()
			elif type(e) is sf.KeyEvent:
				if e.pressed:
					if e.code == sf.Keyboard.ESCAPE: exit()
					elif e.code == sf.Keyboard.SPACE:	self.swarm.paused= not self.swarm.paused
					elif e.code == sf.Keyboard.UP:		self.swarm.speed*=2
					elif e.code == sf.Keyboard.DOWN:	self.swarm.speed/=2
					elif e.code == sf.Keyboard.TAB:		self.swarm.speed*=-1
					elif e.code == sf.Keyboard.C:		self.drawCentroids= not self.drawCentroids
					elif e.code == sf.Keyboard.N:		self.drawNeighbors= not self.drawNeighbors
					elif e.code == sf.Keyboard.P:		self.drawPolies= not self.drawPolies

	@property
	def step(self):
		tDelta = self.clock.restart().seconds
		return tDelta/10

