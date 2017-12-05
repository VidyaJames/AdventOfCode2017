f1 = open('input.txt', 'r')

target = int(f1.readline())
answer = 0
values = {}
x = 0
y = 0
values[(x,y)] = 1
moves = ["right", "up", "left", "down"]
moveNum = 0

i = 0
while answer == 0:
	moveNum += 1
	j = 0
	while j < 2:
		k = 0
		while k < moveNum and answer == 0:
			total = values[(x,y)]
			l = 0
			while l < 3:
				checkX = x 
				checkY = y
				if moves[i] == "right":
					checkX += l
					checkY += 1
				elif moves[i] == "up":
					checkX -= 1
					checkY += l
				elif moves[i] == "left":
					checkX -= l
					checkY -= 1
				elif moves[i] == "down":
					checkX += 1
					checkY -= l
				if (checkX, checkY) in values:
					total += values[(checkX, checkY)]
				l += 1
			if moves[i] == "right":
				x += 1
			elif moves[i] == "up":
				y += 1
			elif moves[i] == "left":
				x -= 1
			elif moves[i] == "down":
				y -= 1
			values[(x,y)] = total
			
			if values[(x,y)] > target:
				answer = values[(x,y)]
			k += 1
		i += 1
		if i == len(moves):
			i = 0
		j += 1
print answer
