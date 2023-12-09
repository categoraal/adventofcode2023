input = open('in9').read().strip().split('\n')
input = [[int(i) for i in line.split()] for line in input]

def diffs(x):
	val = []
	for i in range(len(x)-1):
		val.append(x[i+1]-x[i])	
	return val

p1 = 0
p2 = 0
for i,val in enumerate(input):
	val = [val]
	while set(val[-1]) != {0}:
		diff = diffs(val[-1])		
		val.append(diff)
	p1+= sum([k[-1] for k in val] )

	l = len(val)
	d = 0
	val.pop(-1)
	for j in val[::-1]: 
		d = j[0] - d	

	p2 += d

print(p1)
print(p2)
