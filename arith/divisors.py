import math

def divisors(n):
	negs = []
	if n<0: n=-n; negs=[-1]
	sqrtN = int(math.ceil(math.sqrt(n)))
	hiDivs = []
	loDivs = []
	for x in xrange(1,sqrtN):
		if n%x == 0:
			loDivs.append(x)
			hiDivs.append(n/x)
	hiDivs.reverse()
	return negs+loDivs+hiDivs


import sys
if __name__ == '__main__':
	print divisors(int(sys.argv[1]))