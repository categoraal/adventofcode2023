import re
input = open('in20').read().strip().split('\n')

states = {}
for i in input:
	l = re.findall(r'\w+',i)
	if l[0] not in states:
		if i[0] == 'b':
			states[l[0]] = [i[0],'low',(l[1:])] #type, output, points to 
		if i[0] == '%': #switches when low pulse. on to off -> low, off to on -> high
			states[l[0]] = [i[0],'off',(l[1:])] #type, on or off, point to
		if i[0] == '&':
			states[l[0]] = [i[0],{},l[1:]] #type,mem,points to 
		if i[0] == 'o':
			states[l[0]] = []

for i in input:
	for j in re.findall(r'\w+',i):
		if j not in states:
			states[j] = ['n',]

for i in input:
	k = re.findall(r'\w+',i)
	for j in k[1:]:
		if states[j][0] == '&':	
			a,b,c = states[j]
			b[k[0]] = 'low'
			states[j] = [a,b,c]

queu = []
signals = []
for cnt in range(1000):
	queu = [('broadcaster','low')]
	sigs = ['low']
	for key,inp in queu:
		state = states[key]
		t = state[0]
		if t == 'b':
			sig = 'low'

		if t == '%':
			t, oo, dest = state
			if inp == 'low' and oo == 'off':
				states[key] = [t,'on',dest]
				sig = 'high'
			elif inp == 'low' and oo == 'on':
				states[key] = [t,'off',dest]
				sig = 'low'

		if t == '&':
			t,mem,dest = state
			high = False
			for i in mem:
				if mem[i] == 'low':
					 high = True
			if high:
				sig = 'high'
			else:
				sig = 'low'
			
		for i in state[-1]:
			sigs.append(sig)			
			nstate = states[i]
			if nstate[0] == '%':
				if sig == 'low':
					queu.append((i,sig))
			if nstate[0] == '&':
				nstate[1][key] = sig
				queu.append((i,sig))	
	signals += sigs
print(signals.count('low')*signals.count('high'))

states = {}
for i in input:
	l = re.findall(r'\w+',i)
	if l[0] not in states:
		if i[0] == 'b':
			states[l[0]] = [i[0],'low',(l[1:])] #type, output, points to 
		if i[0] == '%': #switches when low pulse. on to off -> low, off to on -> high
			states[l[0]] = [i[0],'off',(l[1:])] #type, on or off, point to
		if i[0] == '&':
			states[l[0]] = [i[0],{},l[1:]] #type,mem,points to 
		if i[0] == 'o':
			states[l[0]] = []

for i in input:
	for j in re.findall(r'\w+',i):
		if j not in states:
			states[j] = ['n',]

for i in input:
	k = re.findall(r'\w+',i)
	for j in k[1:]:
		if states[j][0] == '&':	
			a,b,c = states[j]
			b[k[0]] = 'low'
			states[j] = [a,b,c]

queu = []
cnt = 0
flag1 = True
flag2 = True
flag3 = True
flag4 = True
res = 1
while flag1 or flag2 or flag3 or flag4:
	cnt += 1
	queu = [('broadcaster','low')]
	for key,inp in queu:
		state = states[key]
		t = state[0]
		if t == 'b':
			sig = 'low'

		if t == '%':
			t, oo, dest = state
			if inp == 'low' and oo == 'off':
				states[key] = [t,'on',dest]
				sig = 'high'
			elif inp == 'low' and oo == 'on':
				states[key] = [t,'off',dest]
				sig = 'low'

		if t == '&':
			t,mem,dest = state
			high = False
			for i in mem:
				if mem[i] == 'low':
					 high = True
			if high:
				sig = 'high'
			else:
				sig = 'low'
			
		for i in state[-1]:
			nstate = states[i]
			if nstate[0] == '%':
				if sig == 'low':
					queu.append((i,sig))
			if nstate[0] == '&':
				nstate[1][key] = sig
				queu.append((i,sig))	

			if i == 'xc' and sig == 'low' and flag1:
				flag1 = False
				res *= cnt
			if i == 'th' and sig == 'low'and flag2:
				flag2 = False
				res *= cnt
			if i == 'pd' and sig == 'low'and flag3:
				flag3 = False
				res *= cnt
			if i == 'bp' and sig == 'low'and flag4:
				flag4 = False
				res *= cnt

				break
print(res)
