f1 = open('input.txt', 'r')

x = 0
y = 0
z = 0
xMoves= {'n': 0, 'ne': 1, 'se': 1, 's': 0, 'sw': -1, 'nw': -1}
yMoves= {'n': 1, 'ne': 0, 'se': -1, 's': -1, 'sw': 0, 'nw': 1}
zMoves= {'n': -1, 'ne': -1, 'se': 0, 's': 1, 'sw': 1, 'nw': 0}
maxDistance = 0
for i in f1.readline()[:-1].split(','):
	x += xMoves[i]
	y += yMoves[i]
	z += zMoves[i]
	maxDistance = max((abs(x) + abs(y) + abs(z)) / 2, maxDistance)
print maxDistance
