def findZero(key, pipes, seenList, traverse):
	if traverse == 10000:
		return seenList
	for i in pipes[key]:
		if i not in seenList:
			seenList.append(i)
			findZero(i, pipes, seenList, traverse+1)
	return seenList

f1 = open('input.txt', 'r')

pipes = {}
for i in f1.readlines():
	splitLine = i[:-1].split(' ')
	endList = []
	for j in splitLine[2:]:
		endList.append(j.split(',')[0])
		
	pipes[splitLine[0]] = endList

groups = []
for k in pipes:
	seen = 0
	for l in groups:
		if k in l:
			seen = 1
	if seen == 0:
		groups.append(findZero(k, pipes, [], 0))

print len(groups)
