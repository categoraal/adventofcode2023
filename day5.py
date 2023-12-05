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


input = open('in5').read().strip().split('\n\n')
#print(input[1:])
seeds = [int(i) for i in re.findall(r'\d+',input[0])]
length = len(seeds)/2
ranges = []

for i in range(int(length)):
	ranges.append([seeds[2*i],seeds[2*i]+seeds[2*i+1]])
#print(ranges)

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


# print(ranges)
# for k in ranges:
# 	print(k)

c = 0
for i in input[1:]:
	c = 0
	newranges = []
	i = i.split('\n')[1:]
	rr = []
	for k in ranges:
		# print('current range',k)
		lb = k[0];up = k[1]
		flag = 0
		for j in i:
			dest,source,rg = [int(u) for u in re.findall('\d+',j)]
			dist = dest-source
			ilb = source;iub = source+rg
			inter = intersection(lb,up,ilb,iub)
			# print('inter',inter)
			if inter is not None:
				flag = 1
				newranges.append([inter[0]+dist,inter[1]+dist])
				rest = restrange(inter[0],inter[1],lb,up)
				rr.append([lb,up])
				if rest:
					for r in rest:
						ranges.append(r)
	
					

	for r in rr:
		# print('rrrrrrr',r)
		try:
			ranges.remove(r)
		except:
			True
	ranges = newranges + ranges
	# print(ranges)


print(min(min(ranges)))



































# for i in input[1:]:
# 	newranges = []
# 	i = i.split('\n')[1:]
# 	for lb,up in ranges:
# 		for j in i:
			# print('bound',lb,up)
			# dest,source,rg = [int(u) for u in re.findall('\d+',j)]
			# print('instr',source,source+rg)
			# print(intersection(lb,up,source,source+rg))
			# if source <= lb < source + rg and source < up <= source + rg:
			# 	print('1')
			# 	nlb = lb + dest - source
			# 	nup = up + dest - source
			# 	newranges.append([nlb,nup])
			# elif lb < source and up > source + rg:
			# 	print('4')
			# 	nlb = dest
			# 	nup = dest + rg
			# 	newranges.append([lb,up])
			# 	ranges.append([lb,source])
			# 	ranges.append([source+rg,up])
			# elif source <= lb and lb < source+rg and up > source + rg: 
			# 	print('2')
			# 	nlb = lb + dest - source
			# 	nup = dest + rg
			# 	newranges.append([nlb,nup])
			# 	ranges.append([source+rg,up])
			# elif lb < source and source < up and up <= source + rg:
			# 	print('3')
			# 	nlb = dest
			# 	nup = up + dest - source
			# 	newranges.append([nlb,nup])
			# 	ranges.append([lb,source])
			# elif up <= source:
			# 	newranges.append([lb,up])
			# elif lb >= source + rg:
			# 	newranges.append([lb,up])
			# print('ranges',ranges)






#for i in input[1:]:
#	i = i.split('\n')[1:]
#	for k in seeds:
#		for j in i:
#			dest,source,rg = [int(u) for u in re.findall('\d+',j)]
#			if source <= seedsdict[k][-1] and seedsdict[k][-1] < source+rg and jumpdict[k] == 0:
#				seedsdict[k].append(seedsdict[k][-1] + (dest-source))
#				jumpdict[k] = 1
#		for l in seeds:
#			jumpdict[l] = 0	
#	for k in seeds:
#		jumpdict[k] == 0	













































# for i in input[1:]:
# 	newranges = []
# 	i = i.split('\n')[1:]
# 	for lb,up in ranges:	
# 		print('ranges',lb,up,ranges)
# 		for j in i:
# 			dest,source,rg = [int(u) for u in re.findall('\d+',j)]
# 			print('instruction',dest,source,rg)
# 			if source <= lb < source + rg and source < up <= source + rg:
# 				print('1')
# 				lb1 = lb + dest - source
# 				up1 = up + dest - source					
# 				newranges.append([lb1,up1])
# 				ranges.remove([lb,up])
# 				print('1')

# 			elif source <= lb < source + rg and up > source + rg: 
# 				print('2')
# 				lb1 = lb + dest -source
# 				up1 = dest + rg
# 				newranges.append([lb1,up1])
# 				ranges.append([source+rg,up])
# 				ranges.remove([lb,up])
# 				print('2')

# 			elif lb < source and source < up <= source + rg:
# 				print('3')
# 				lb1 = dest 
# 				up2 = up + rg
# 				ranges.append([lb,source])	
# 				newranges.append([lb1,up1])
# 				ranges.remove([lb,up])
# 				print('3')

# 			elif lb < source and up > source + rg:
# 				print('4')
# 				lb1 = dest
# 				up1 = dest + rg 
# 				newranges.append([lb1,up1])
# 				ranges.append([lb,source])
# 				ranges.append([source+rg,up])
# 				ranges.remove([lb,up])
# 				print('4')
# 			else:
# 				print('5')
# 			print('ranges eoi',ranges)
# 	ranges =ranges + newranges
# 	print(ranges)
	
# print(ranges)