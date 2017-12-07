f1 = open('input.txt', 'r')

answer = ""
inputs = f1.readlines()
check = inputs[0].split(' (')[0]
while answer == "":
	goAgain = ""
	for i in inputs:
		splits = i.split('->')
		if len(splits) == 2 and check in splits[1]:
			goAgain = i
			check = splits[0].split(' (')[0]
			break
	if goAgain == "":
		answer = check
print answer
