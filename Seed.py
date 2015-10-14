from sys import argv
from random import randint as iRand, seed as random_seed
from sys import maxint
def Seed():
	if argv[1:]:	seed=int(argv[1])
	else:
		seed = iRand(0, maxint )
		print 'seed:',seed
	random_seed(seed)
