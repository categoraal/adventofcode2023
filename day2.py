import re

input = open('in2').read().strip().split('\n')

bred = 12
bblue = 14
bgreen = 13

def possible(game):
	game = game.split(',')
	flag = 0
	for i in game:
		if i.endswith('blue'):
			blue = int(re.findall(r'\d+',i)[0])
			if blue > bblue:
				return 1
		
		if i.endswith('red'):
			red = int(re.findall(r'\d+',i)[0])
			if red > bred:
				return 1
		if i.endswith('green'):
			green = int(re.findall(r'\d+',i)[0])
			if green > bgreen:
				return 1
	return 0

res = 0
for line in input:
	gameidx,games = line.split(':')
	games = games.split(';')
	flag = 1
	for game in games:
	    flag -=	possible(game)
	if flag == 1:
		res +=int(re.findall(r'\d+',gameidx)[0])

#print(res)	



input = open('in2').read().strip().split('\n')


def power(games):
	b = 1
	r = 1
	g = 1
	game = games.split(';')
	for round in game:
		round = round.split(',')	
		for i in round:
			if i.endswith('blue'):
				blue = int(re.findall(r'\d+',i)[0])
				if blue > b:
					b = int(re.findall(r'\d+',i)[0])
			if i.endswith('red'):
				red = int(re.findall(r'\d+',i)[0])
				if red > r:
					r = int(re.findall(r'\d+',i)[0])
			if i.endswith('green'):
				green = int(re.findall(r'\d+',i)[0])
				if green > g:
					g = int(re.findall(r'\d+',i)[0])
			
	return b*r*g			
	return 0

res = 0
for line in input:
	line = line.split(':')	
	res+= power(line[1])
print(res)	
