import sfml as sf

Red= 0.0
Green= .333
Blue= .666

def Hue(h, s=1.0, v=1.0, a=1.0):
	a*=255
	if s == 0.0: v*=255; return sf.Color(v, v, v, a)
	i = int(h*6.) # XXX assume int() truncates!
	f = (h*6.)-i
	p = int(255*(v*(1.-s)))
	q = int(255*(v*(1.-s*f)))
	t = int(255*(v*(1.-s*(1.-f))))
	v*=255
	i%=6
	if i == 0: return sf.Color(v, t, p, a)
	if i == 1: return sf.Color(q, v, p, a)
	if i == 2: return sf.Color(p, v, t, a)
	if i == 3: return sf.Color(p, q, v, a)
	if i == 4: return sf.Color(t, p, v, a)
	if i == 5: return sf.Color(v, p, q, a)

