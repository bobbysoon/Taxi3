from math import atan2

def angle(p1,p2):
	return atan2(p2[0]-p1[0],p2[1]-p1[1])
