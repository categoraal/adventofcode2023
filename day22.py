import re
from operator import itemgetter

input = open('in22t').read().strip().split('\n')
input = [[int(i) for i in re.findall(r'\d+',j)] for j in input]

ground = 0

input = sorted(input,key =itemgetter(2,5)) 
[print(i) for i in input]

def over(a,b):
	if not b:
		return a
	x1,y1,z1,x2,y2,z2 = a	
	x3,y3,z3,x4,y4,z4 = b
	if z3 <= z1 <= z4 or z3 <= z2 <= z4 or z1 <= z3 <= z2:
		if x1 <= x3 <= x2 or x1 <= x4 <= x2 or x3 <= x1 <= x4 or x3 <= x2 <= x4:
			if y1 <= y3 <= y2 or y1 <= y4 <= y2 or y3 <= y1 <= y4 or y3 <= y2 <= y4:
				return True
	return False	

def f(x,rp):
	x1,y1,z1,x2,y2,z2 = x
	if z1 == 1 or z2 == 1:
		return x
	while z1 > 1 and z2 > 1:
		z1 -= 1; z2 -= 1
		for i in rp:
			x3,y3,z3,x4,y4,z4 = i
			if over([x1,y1,z1,x2,y2,z2],i):
				return 	(x1,y1,z1+1,x2,y2,z2+1)
	return [x1,y1,z1,x2,y2,z2]

rp = []
for i in input:
	rp.append(f(i,rp))
	
print('\n')
[print(i) for i in rp]
