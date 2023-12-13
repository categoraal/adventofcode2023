boards = open('in13').read().strip().split('\n\n')
from copy import deepcopy

def c(board):
	l = len(board)
	for i in range(len(board)-1):
		if board[i] == board[i+1]:
			b = min(l-i-1,i+1)
			if board[i+1-b:i+1] == list(reversed(board[i+1:i+1+b])):
				return i+1
	return 0
		
vert = 0
hor = 0

for board in boards:
	board = board.split('\n')
	hor += c(board)
	board = list(map(list, zip(*board)))	
	vert += c(board)

print(100*hor+vert)

#part 2
def c_n(board,c):
	l = len(board)
	for i in range(len(board)-1):
		if board[i] == board[i+1] and i+1 != c:
			b = min(l-i-1,i+1)
			if board[i+1-b:i+1] == list(reversed(board[i+1:i+1+b])):
				return i+1
	return 0
		
def bc(board):
	board = [list(i) for i in board]
	cb = []
	count = 0
	for i in range(len(board)):
		for j in range(len(board[0])):
			b = deepcopy(board)
			if b[i][j] == '.':
				b[i][j] = '#'
			else:
				b[i][j] = '.'
			cb.append(b)
	return cb

vert = 0
hor = 0
cnt = 0
c2 = 0
for board in boards:
	c2+=1
	board = board.split('\n')
	nb = bc(board)
	h = c(board)
	v = c(list(map(list, zip(*board))))
	for b in nb:	
		h1 = c_n(b,h)
		if h1 != h and h1 != 0:
			hor += h1 
			cnt += 1
			break
		v1 = c_n(list(map(list, zip(*b))),v)
		if v1 != v and v1 != 0:
			vert += v1
			cnt += 1
			break
print(int(100*hor+vert))
