def findZero(key, pipes, seenList, traverse):
	if key == "0":
		return 1
	if traverse == 10000:
		return 0
	for i in pipes[key]:
		if i not in seenList:
			seenList.append(i)
			count = findZero(i, pipes, seenList, traverse+1)
			if count == 1:
				return 1
	return 0

f1 = open('input.txt', 'r')

pipes = {}
for i in f1.readlines():
	splitLine = i[:-1].split(' ')
	endList = []
	for j in splitLine[2:]:
		endList.append(j.split(',')[0])
		
	pipes[splitLine[0]] = endList

count = 0
for k in pipes:
	count += findZero(k, pipes, [], 0)

print count
