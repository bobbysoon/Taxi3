#!/usr/bin/python

if __name__ == "__main__": # test
	from ConnectedSubset import ConnectedSubset
	from Swarm import *
	from Demo import *
	from Centroid import *
	from Taxi import *
	from time import sleep

	import sfml as sf
	from angle import angle

	from SFVert import *

	class SFCentroidTriFan(sf.VertexArray):
		def __init__(self, c):
			verts= [(angle(c,v),v) for v in c.verts]
			verts= sorted( verts , key=lambda x: x[0] )
			verts= [v for a,v in verts]
			verts.append(verts[0])
			verts.insert(0,c)

			sf.VertexArray.__init__(self, sf.PrimitiveType.TRIANGLES_FAN, len(verts) )

			col= sf.Color(64,64,64)
			for i in range(len(verts)):
				self[i].color=col
				self[i].position=verts[i]

	class SFVert:
		def __init__(self, target, hue):
			self.target= target
			self.circ= sf.CircleShape(point_count=6)
			self.circ.outline_color = Hue(hue,a=.25)
			self.circ.fill_color = Hue(hue,a=.5)

		def setScale(self,scale):
			self.circ.origin= scale,scale
			self.circ.radius= scale
			self.circ.outline_thickness= scale/3.0

		def draw(self, pos):
			self.circ.position= pos
			self.target.draw(self.circ)

	class LPPDemo(Demo):
		def __init__(self, swarm, size=(800,600)):
			Demo.__init__(self,swarm=swarm, size=size)
			self.vert= SFVert(self.window, .8)

		def draw(self, taxi):
			self.window.clear()
			for c in Centroid.centroids:	self.window.draw(c.triFan)
			for c in Centroid.centroids:	self.window.draw(c.linesStrip)
			self.vert.setScale(self.view.size.x/self.window.size.x*3)
			for c in Centroid.centroids:	self.vert.draw(c)
			self.window.display()
			self.processEvents()


	swarm= Swarm(48)
	demo= LPPDemo(swarm)
	taxi=Taxi(swarm)
	Centroid.centroids= ConnectedSubset(taxi)
	for c in Centroid.centroids:
		c.triFan=SFCentroidTriFan(c)
		c.linesStrip=SFCentroidOutline(c)

	demo.draw(taxi)
	while demo.is_open:
		demo.draw(taxi)
		sleep(.25)


