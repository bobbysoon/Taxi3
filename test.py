#!/usr/bin/python

from Demo import Demo
from Swarm import Swarm
from Taxi import Taxi

swarm= Swarm(count=24)
demo= Demo(swarm)
while demo.is_open:
	demo.draw(Taxi(swarm))
	if not demo.paused:
		swarm.move(demo.step)

