from Centroid import Centroid
from Vec2 import Vec2

from random import random

from math import *
from angle import angle

class Swarm(list):
	def __init__(self, count):
		self.speed= 1.0/16.0
		self.paused= False

	def __new__(cls, count):
		swarm= list.__new__(cls)
		for n in range(count):
			x= random()-random()
			y= random()-random()
			c= Centroid(x,y)
			c.inertia= Vec2(0,0)

			swarm.append(c)

		return swarm

	def repel(self, step):
		for i in range(1,len(self)):
			for j in range(i):
				if self[i] in self[j].neighbors:
					assert self[j] in self[i].neighbors
					a=angle(self[j],self[i])
					dx,dy = self[i]-self[j]
					dist= sqrt(dx*dx+dy*dy)
					push= 1.0/dist
					a+=1.5707*push
					push= sin(a)*push*step,cos(a)*push*step
					self[i].inertia+= push
					self[j].inertia-= push

	def move(self, step):
		if self.paused: return
		self.repel(step)
		step*= self.speed
		for c in self:
			c+= c.inertia*step
			if abs(c.x)>=1:
				c.inertia.x*=-1
				c.x+=c.inertia.x*2*step
			if abs(c.y)>=1:
				c.inertia.y*=-1
				c.y+=c.inertia.y*2*step

			c.clear()

