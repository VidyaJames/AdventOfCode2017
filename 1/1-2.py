f1 = open('input.txt', 'r')
input = f1.readline()
input = input[:-1]
i = 0
sum = 0
half=len(input)/2
while i < len(input):
	compare = i + half
	if (i+1 > half):
		compare = i - half
	if (input[i] == input[compare]):
		sum = sum + int(input[i])
	i = i + 1
print sum
