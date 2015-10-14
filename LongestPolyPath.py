#!/usr/bin/python
from random import shuffle

__all__ = ['LongestPolyPath']

def PolyArea2D(verts):
	n=0
	x1,y1=verts[-1]
	for p in verts:
		x2,y2=p
		n+=x1*y2-x2*y1
		x1=x2;y1=y2
	return 0.5*abs(n)

polies=None

def PolyPath(cell,cells,others):
	global polies
	paths={}
	shuffle(others[cell])
	for n in others[cell]:			#	for each neighbor,
		if not [None for nn in others[n] if not nn in cells]:
			nCells= [c for c in cells if c!=cell]
			path = PolyPath(n,nCells,others)
			area=sum([polies[pi].area for pi in path])
			paths[area]= path

	path = [cell]
	if paths:
		longestPath= paths[sorted(paths.keys())[-1]]
		path.extend(longestPath)

	return path


def LongestPolyPath(taxi,loopStep=None,window=None):
	global polies
	polies = taxi.centroids
	for p in polies: p.area= PolyArea2D(p.verts)
	others=[[polies.index(n) for n in p.neighbors if n in polies] for p in polies]
	cells= range(len(polies))
	outerCells = [polies.index(p) for p in polies if [None for p2 in p.neighbors if not p2.isClosed] ]
	shuffle(outerCells)
	paths = {};iProg=0
	for cell in outerCells:
		iProg+=1
		path= PolyPath(cell,cells,others)
		if path:
			area=sum([polies[pi].area for pi in path])
			paths[area]= path
			if window:
				pathPolies = [polies[i] for i in range(len(polies)) if i in path]
				loopStep( pathPolies,taxi , iProg*100//len(outerCells) , window )
			elif loopStep: loopStep( 'LongestPolyPath: %d%%'%(iProg*100//len(outerCells)) )
			else: print 'LongestPolyPath: %d%%  \r'%(iProg*100//len(outerCells))

	path = paths[sorted(paths.keys())[-1]]

	return [polies[i] for i in path]


if __name__ == "__main__": # test
	from Swarm import *
	from Demo import *
	from Centroid import *
	from Taxi import *
	from LongestPolyPath import LongestPolyPath
	from time import sleep

	import sfml as sf
	from angle import angle

	class SFCentroidTriFan(sf.VertexArray):
		def __init__(self, c):
			verts= [(angle(c,v),v) for v in c.verts]
			verts= sorted( verts , key=lambda x: x[0] )
			verts= [v for a,v in verts]
			verts.append(verts[0])
			verts.insert(0,c)

			sf.VertexArray.__init__(self, sf.PrimitiveType.TRIANGLES_FAN, len(verts) )

			col= sf.Color.BLACK
			for i in range(len(verts)):
				self[i].color=col
				self[i].position=verts[i]
			self[0].color=sf.Color.GREEN

	class LPPDemo(Demo):
		def draw(self, taxi):
			self.window.clear()
			for c in Centroid.centroids:	self.window.draw(c.triFan)
			for c in Centroid.centroids:	self.window.draw(c.linesStrip)
			self.window.display()
			self.processEvents()


	swarm= Swarm(32)
	demo= LPPDemo(swarm)
	taxi=Taxi(swarm)

	Centroid.centroids= LongestPolyPath(taxi)
	for c in Centroid.centroids:
		c.triFan=SFCentroidTriFan(c)
		c.linesStrip=SFCentroidOutline(c)

	demo.draw(taxi)
	while demo.is_open:
		demo.draw(taxi)
		sleep(.25)


