def getWeights(base,tree,weights,weightList):
	weight = weights[base]
	if base not in tree:
		weightList[base] = weight
		return weight
	else:
		for i in tree[base]:
			weight += getWeights(i,tree,weights,weightList)
		weightList[base] = weight
	return weight
f1 = open('input.txt', 'r')

def getBadWeight(base,tree,weightList):
	checkWeights = {}
	goodWeight = 0
	potentialBad = 0
	for i in tree[base]:
		if weightList[i] in checkWeights:
			checkWeights[weightList[i]] += 1
		else:
			checkWeights[weightList[i]] = 1
	for j in tree[base]:
		if checkWeights[weightList[j]] == 1:
			return j
	return ""

answer = ""
inputs = f1.readlines()
check = inputs[0].split(' (')[0]
weights = {}
tree = {}

for i in inputs:
	base = i.split(' (')[0]
	weights[base] = int(filter(str.isdigit, i))
	if '->' in i:
		# lol
		tree[base] = i.split('-> ')[1][:-1].split(', ')

while answer == "":
	goAgain = ""
	for i in inputs:
		if '->' in i and check in i.split('->')[1]:
			goAgain = i
			check = i.split(' (')[0]
			break
	if goAgain == "":
		answer = check

weightList = {}
getWeights(answer,tree,weights,weightList)
rootBad = answer
bad = getBadWeight(answer,tree,weightList)
lastBad = rootBad

while bad != "":
	rootBad = lastBad
	lastBad = bad
	bad = getBadWeight(bad,tree,weightList)

goodWeight = 0
for i in tree[rootBad]:
	if i != lastBad:
		goodWeight = weightList[i]
	else:
		badWeight = weightList[i]
print weights[lastBad] + goodWeight - badWeight
