import re

input = open('in6').read().strip().split('\n')
time = [int(i) for i in re.findall(r'\d+',input[0])]
distance = [int(i) for i in re.findall(r'\d+',input[1])]

res = [0,0,0,0] 
for i in range(len(time)):
	t = time[i]
	d = distance[i]
	for j in range(t):
		if j*(t-j) > d:
			res[i] += 1	

print(res[0]*res[1]*res[2]*res[3])

#part 2

t = int(''.join(re.findall(r'\d+',input[0])))
dist = int(''.join(re.findall(r'\d+',input[1])))

upper,lower = 0,0
for i in range(t):
	if i*(t-i)>dist:
		upper = i
		break

for i in reversed(range(t)):
	if i*(t-i)>dist:
		lower = i
		break

print(lower-upper+1)	
