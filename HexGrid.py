from math import *
from random import random as rand
def Sin(deg): return sin(deg*6.283185/360.0)
def Cos(deg): return cos(deg*6.283185/360.0)
def HexGridRow(r,a,randomi):
	P=[]
	x,y = Cos(a)*r,Sin(a)*r
	dx = Cos(a+120)
	dy = Sin(a+120)
	for i in range(r):
		ra=360.0*rand()
		rx=.5*Sin(ra)*randomi
		ry=.5*Cos(ra)*randomi
		P.append( (x+rx,y+ry) )
		x+=dx;y+=dy
	return P

def HexGrid(radius,randomi=.5):
	P=[]
	for a in range(6):
		P.extend(HexGridRow(radius,a*360/6,randomi))
	if radius>1:	P.extend(HexGrid(radius-1))
	else:			P.append((0,0))
	return P

__all__=['HexGrid']

