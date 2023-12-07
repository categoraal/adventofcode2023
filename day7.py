import re
import functools

input = open('in7').read().strip().split('\n')
input = [i.split() for i in input]

fc = dict()
f4c = dict()
fh = dict()
toc = dict()
tp = dict()
op = dict()
hc = dict()

for hand,bid in input:
	strength = 0
	unique = set(hand)
	cc = []
	for i in unique:
		cc.append(hand.count(i))
	if len(unique) == 1:
		fc[hand] = bid
	if sorted(cc) == [1,4]:
		f4c[hand] = bid
	if sorted(cc) == [2,3]:
		fh[hand] = bid
	if sorted(cc) == [1,1,3]:
		toc[hand] = bid
	if sorted(cc) == [1,2,2]:
		tp[hand] = bid
	if sorted(cc) == [1,1,1,2]:
		op[hand] = bid
	if len(unique) == 5:
		hc[hand] = bid

fcl = list(fc.keys())
f4cl = list(f4c.keys())
fhl = list(fh.keys())
tocl = list(toc.keys())
tpl = list(tp.keys())
opl = list(op.keys())
hcl = list(hc.keys())

def compare(l1,l2):
	#A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
	score = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2,'2':1}
	for i, j in zip(l1,l2):
		if score[i] > score[j]:
			return 1
		elif score[i] < score[j]:
			return -1

fcl = sorted(fcl,key=functools.cmp_to_key(compare)) 
f4cl = sorted(f4cl,key=functools.cmp_to_key(compare))
fhl =   sorted(fhl,key=functools.cmp_to_key(compare))
tocl = sorted(tocl,key=functools.cmp_to_key(compare))
tpl = sorted(tpl,key=functools.cmp_to_key(compare))
opl = sorted(opl,key=functools.cmp_to_key(compare))
hcl = sorted(hcl,key=functools.cmp_to_key(compare))
ordered = hcl+opl+tpl+tocl+fhl+f4cl+fcl

hands = dict()
for i,j in input:
	hands[i] = j

score = 0
for i, val in enumerate(ordered):
	score += (i+1)*int(hands[val])

print(score)

## part2

fc = dict();f4c = dict();fh = dict();toc = dict();tp = dict();op = dict();hc = dict()

for hand,bid in input:
	strength = 0
	unique = set(hand)
	cc = []
	for i in unique:
		cc.append(hand.count(i))
	if len(unique) == 1:
		fc[hand] = bid
	if sorted(cc) == [1,4]:
		if 'J' in hand:
			fc[hand] = bid
		else:
			f4c[hand] = bid
	if sorted(cc) == [2,3]:
		if 'J' in hand:
			fc[hand] = bid
		else:
			fh[hand] = bid
	if sorted(cc) == [1,1,3]:
		if 'J' in hand:
			f4c[hand] = bid
		else:
			toc[hand] = bid
	if sorted(cc) == [1,2,2]:
		if 'J' in hand and hand.count('J') == 2:
			f4c[hand] = bid
		elif 'J' in hand and hand.count('J') == 1:
			fh[hand] = bid
		else:
			tp[hand] = bid
	if sorted(cc) == [1,1,1,2]:
		if 'J' in hand:
			toc[hand] = bid
		else:
			op[hand] = bid
	if len(unique) == 5:
		if 'J' in hand:
			op[hand] = bid
		else:
			hc[hand] = bid

fcl = list(fc.keys())
f4cl = list(f4c.keys())
fhl = list(fh.keys())
tocl = list(toc.keys())
tpl = list(tp.keys())
opl = list(op.keys())
hcl = list(hc.keys())

def compare(l1,l2):
	#A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
	score = {'A':13, 'K':12, 'Q':11, 'J':0, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2,'2':1}
	for i, j in zip(l1,l2):
		if score[i] > score[j]:
			return 1
		elif score[i] < score[j]:
			return -1

fcl = sorted(fcl,key=functools.cmp_to_key(compare)) 
f4cl = sorted(f4cl,key=functools.cmp_to_key(compare))
fhl =   sorted(fhl,key=functools.cmp_to_key(compare))
tocl = sorted(tocl,key=functools.cmp_to_key(compare))
tpl = sorted(tpl,key=functools.cmp_to_key(compare))
opl = sorted(opl,key=functools.cmp_to_key(compare))
hcl = sorted(hcl,key=functools.cmp_to_key(compare))
ordered = hcl+opl+tpl+tocl+fhl+f4cl+fcl

hands = dict()
for i,j in input:
	hands[i] = j

score = 0
for i, val in enumerate(ordered):
	score += (i+1)*int(hands[val])
print(score)
