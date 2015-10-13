def SegSegIntersect(s1,s2):
	p1,p2 = s1 ; x1,y1 = p1;x2,y2 = p2
	p3,p4 = s2 ; x3,y3 = p3;x4,y4 = p4
	dx21 = x2-x1 ; dy21 = y2-y1
	dx43 = x4-x3 ; dy43 = y4-y3

	d = dx21*dy43 - dy21*dx43
	if d:
		dx13 , dy13 = x1-x3 , y1-y3
		r = ( dy13*dx43 - dx13*dy43) / d
		s = ( dy13*dx21 - dx13*dy21) / d
		if r >= 0 and r <= 1 and s >= 0 and s <= 1:
			return x1 + r*dx21 , y1 + r*dy21
