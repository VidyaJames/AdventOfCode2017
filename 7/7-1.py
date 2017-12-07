f1 = open('input.txt', 'r')

answer = ""
inputs = f1.readlines()
check = inputs[0].split(' (')[0]
while answer == "":
	goAgain = ""
	for i in inputs:
		if '->' in i and check in i.split('->')[1]:
			goAgain = i
			check = i.split(' (')[0]
			break
	if goAgain == "":
		answer = check
print answer
