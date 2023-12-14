import re
from collections import defaultdict
import time

input = open('in5').read().strip().split('\n\n')

seeds = [int(i) for i in re.findall(r'\d+',input[0])]

seedsdict = dict()
jumpdict = dict()
for i in seeds:
	seedsdict[i] = [i]
	jumpdict[i] = 0

for i in input[1:]:
	i = i.split('\n')[1:]
	for k in seeds:
		for j in i:
			dest,source,rg = [int(u) for u in re.findall('\d+',j)]
			if source <= seedsdict[k][-1] and seedsdict[k][-1] < source+rg and jumpdict[k] == 0:
				seedsdict[k].append(seedsdict[k][-1] + (dest-source))
				jumpdict[k] = 1
		for l in seeds:
			jumpdict[l] = 0	
	for k in seeds:
		jumpdict[k] == 0	
loc = []
for i in seeds:
	loc.append(seedsdict[i][-1])
print(sorted(loc)[0])
			
#Part 2:
start = time.time()
input = open('in5').read().strip().split('\n\n')
seeds = [int(i) for i in re.findall(r'\d+',input[0])]
length = len(seeds)/2
ranges = []

for i in range(int(length)):
	ranges.append([seeds[2*i],seeds[2*i]+seeds[2*i+1]])

def intersection(l1,u1,l2,u2):
	temp = max(l1,l2),min(u1,u2)
	return temp if temp[0] < temp[1] else None

def restrange(l1,u1,l2,u2):
	if l1 == l2 and u1 == u2:
		return
	if l1 == l2:
		return [[u1,u2]]
	if u1 == u2:
		return [[l2,l1]]
	else:
		return [[l2,l1],[u1,u2]]


for i in input[1:]:
	newranges = []
	i = i.split('\n')[1:]
	rr = []
	for k in ranges:
		lb = k[0];up = k[1]
		flag = 0
		for j in i:
			dest,source,rg = [int(u) for u in re.findall('\d+',j)]
			dist = dest-source
			ilb = source;iub = source+rg
			inter = intersection(lb,up,ilb,iub)
			if inter is not None:
				flag = 1
				newranges.append([inter[0]+dist,inter[1]+dist])
				rest = restrange(inter[0],inter[1],lb,up)
				rr.append([lb,up])
				if rest:
					for r in rest:
						ranges.append(r)
	for r in rr:
		try:
			ranges.remove(r)
		except:
			True
	ranges = newranges + ranges
	stop = time.time()
print(min(min(ranges)))
print(stop-start)