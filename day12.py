import re
from functools import cache
import time

#slow implementation
input = open('in12').read().strip().split('\n')
start = time.time()
def valid(l,r):
	a = [len(i) for i in re.findall(r'[#]+',l)]		
	a = tuple(a)
	return 1 if a == r else 0

def check(dots,blocks,i): #recursion ughhhh
		
	if len(dots) == i:
		return 1 if valid(dots,blocks) else 0

	if dots[i] == '?':
		return check(dots[:i]+'.'+dots[i+1:],blocks,i+1)+check(dots[:i]+'#'+dots[i+1:],blocks,i+1)
	else:
		return check(dots,blocks,i+1)	
res = 0
for i in input:
	l,r = i.split(' ')
	r = [int(k) for k in r.split(',')]
	r = tuple(r)
	x = 0
	#temp = check(l,r,x)
	#res += temp

print(res)

print(time.time()-start)

#part 2
@cache
def check(dots,blocks):
	if len(dots) == 0:
		return 1 if len(blocks) == 0 else 0
	if dots[0] == '.':
		return check(dots.strip('.'),blocks)
	if dots[0] in '?':
		return check(dots.replace('?','#',1),blocks) + check(dots[1:],blocks)		
	if dots[0] == '#':
		if len(blocks) == 0 or len(dots) < blocks[0] or '.' in dots[:blocks[0]]:
			return 0
		if len(blocks)>1:
			if len(dots) < blocks[0]+1 or dots[blocks[0]] == '#':
				return 0
			return check(dots[blocks[0]+1:],blocks[1:])
		else:
			return check(dots[blocks[0]:],blocks[1:])

res = 0
for i in input:
	l,r = i.split(' ')
	r = [int(k) for k in r.split(',')]
	r = tuple(r)
	temp = check(l,r)
	res += temp

print(res)

start = time.time()
res = 0
for i in input:
	l,r = i.split(' ')
	r = [int(k) for k in r.split(',')]
	l = l+'?'+l+'?'+l+'?'+l+'?'+l
	r = tuple(5*r)
	temp = check(l,r)
	res += temp

print(res)
print(time.time()-start)
