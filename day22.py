import re
from operator import itemgetter

input = open('in22').read().strip().split('\n')
input = [[int(i) for i in re.findall(r'\d+',j)] for j in input]
input = sorted(input,key =itemgetter(2,5)) 

# def over(a,b):
# 	#if not b:
# 	#	return a
# 	x1,y1,z1,x2,y2,z2 = a	
# 	x3,y3,z3,x4,y4,z4 = b
# 	if z3 <= z1 <= z4 or z3 <= z2 <= z4 or z1 <= z3 <= z2 or z1 <= z4 <= z2:
# 		if x1 <= x3 <= x2 or x1 <= x4 <= x2 or x3 <= x1 <= x4 or x3 <= x2 <= x4:
# 			if y1 <= y3 <= y2 or y1 <= y4 <= y2 or y3 <= y1 <= y4 or y3 <= y2 <= y4:
# 				return True
# 	return False	

def over(a,b):
	if not b:
		return a
	x1,y1,z1,x2,y2,z2 = a	
	x3,y3,z3,x4,y4,z4 = b
	if max(z1,z3) <= min(z2,z4):
		if max(x1,x3) <= min(x2,x4):
			if max(y1,y3) <= min(y2,y4):
				return True
	return False

def f(x,rp):
	x1,y1,z1,x2,y2,z2 = x
	if z1 == 1 or z2 == 1:
		return tuple(x)	
	while z1 > 1 and z2 > 1:
		z1 -= 1; z2 -= 1
		for i in rp:
			if over([x1,y1,z1,x2,y2,z2],i):
				return 	(x1,y1,z1+1,x2,y2,z2+1)
	return (x1,y1,z1,x2,y2,z2)

rp = []
rpl = {}
c = 0
pos = set()
for i in input:
	res = f(i,rp)
	rp.append(res)
	pos.add(str(c))
	c += 1

rp = sorted(rp,key =itemgetter(2,5))
for idx,val in enumerate(rp):
	rpl[idx] = val

rr = {}
for i in rpl: #which blocks below
	a = set()
	x1,y1,z1,x2,y2,z2 = rpl[i]
	for j in rpl:
		x3,y3,z3,x4,y4,z4 = rpl[j]
		if z1 == z4+1:
			if i != j and over(rpl[i],(x3,y3,z3+1,x4,y4,z4+1)):
				a.add(j)
	rr[i] = a
	
inv = set()
for i in rr:
	if len(rr[i]) == 1:
		inv.update(rr[i])

print(len(pos)-len(inv))

#part 2
rm = {} #which blocks above
for i in rpl:
	a = set()
	x1,y1,z1,x2,y2,z2 = rpl[i]
	for j in rpl:
		x3,y3,z3,x4,y4,z4 = rpl[j]
		if z2 == z3-1:
			if i != j and over(rpl[i],(x3,y3,z3-1,x4,y4,z4-1)):
				a.add(j)
	rm[i] = a

def fallingblocks(block):
	queu = [b for b in rm[block] if len(rr[b]) == 1]
	removed = set(queu)
	removed.add(block)
	for b in queu:
		for k in rm[b]-removed: #all blocks not yet removed above currently removed blocks
			if rr[k] <= removed: #if all blocks below are falling, add k to queu, and remove k
				queu.append(k)
				removed.add(k)
	return len(removed)-1
res = 0
for block in inv:
	res += fallingblocks(block)
print(res)