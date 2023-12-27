import re
rules,data = [i.split('\n') for i in open('in19').read().strip().split('\n\n')]

rd = {}
for i in rules:
	key,val = i[:-1].split('{')
	rd[key] = val.strip().split(',')	


def accepted(x,m,a,s,key):
	if key == 'A':
		return True
	elif key == 'R':
		return False

	h = {'s':s,'x':x,'a':a,'m':m}
	rule = rd[key]
	for i in rule:
		i = i.split(':')
		if len(i) > 1:
			num = int(*re.findall(r'\d+',i[0]))	
			key = i[-1]
			if '<' in i[0]:
				if h[i[0][0]] < num:
					return accepted(x,m,a,s,key)
			if '>' in i[0]:
				if h[i[0][0]] > num:
					return accepted(x,m,a,s,key)
		else:
			key = i[0]
			return accepted(x,m,a,s,key)	

res = 0
for i in data:
	l = [int(j) for j in re.findall(r'\d+',i)]
	if accepted(*l,'in'):
		res += sum(l)

print(res)

# Part 2
def inter(x,m,a,s,dir,key,bound):
	h = {'s':s,'x':x,'a':a,'m':m}
	topart = h[key]
	tl,tu = topart
	if dir == '<':
		if tu < bound:
			i1 = x,m,a,s
			i2 = None
		if tl >= bound:
			i2 = (x,m,a,s)
			i1 = None
		else:
			h[key] = (tl,bound-1)
			i1 = (h['x'],h['m'],h['a'],h['s'])
			h[key] = (bound,tu)
			i2 = (h['x'],h['m'],h['a'],h['s']) 
	else:
		if tl > bound:
			i1 = x,m,a,s
			i2 = None
		if tu <= bound:
			i2 = (x,m,a,s)
			i1 = None
		else:
			h[key] = (bound+1,tu)
			i1 = (h['x'],h['m'],h['a'],h['s'])
			h[key] = (tl,bound)
			i2 = (h['x'],h['m'],h['a'],h['s'])
	return i1,i2


def rangesplitter(x,m,a,s,key):
	xl,xh = x; ml,mh = m; al,ah = a;sl,sh = s
	if key == 'A':
		return (xh-xl+1)*(mh-ml+1)*(ah-al+1)*(sh-sl+1)
	if key == 'R':
		return 0
	
	rule = rd[key]
	res = 0
	for r in rule:
		r = r.split(':')
		nkey = r[-1]
		p = 0
		np = 0
		if len(r) == 1:
			return res + rangesplitter(x,m,a,s,nkey)
		if len(r) > 1:
			if '<' in r[0]:
				letter,bound = r[0].split('<')
				p,np = inter(x,m,a,s,'<',letter,int(bound))
			if '>' in r[0]:
				letter,bound = r[0].split('>')
				p,np = inter(x,m,a,s,'>',letter,int(bound))
			if np == (x,m,a,s):
				continue
			if np: res += rangesplitter(*np,key)
			if p: res += rangesplitter(*p,nkey)
		return res

print(rangesplitter((1,4000),(1,4000),(1,4000),(1,4000),'in'))