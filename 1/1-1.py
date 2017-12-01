f1 = open('input.txt', 'r')
input = f1.readline()
i = 0
sum = 0
while i < len(input[:-2]):
	if (input[i] == input[i+1]):
		sum = sum + int(input[i])
	i = i + 1
if (input[i] == input[0]):
	sum = sum + int(input[i])
print sum
