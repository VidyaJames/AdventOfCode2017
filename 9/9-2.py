f1 = open('input.txt', 'r')

readString = f1.readline()[:-1]
cancelled = 0
score = 0
garbage = 0
for i in readString:
	if cancelled == 0:
		if garbage == 0:
			if i == '<':
				garbage = 1
		elif i == '>':
			garbage = 0
		elif i == '!':
			cancelled = 1
		else:
			score += 1
	else:
		cancelled = 0
print score
