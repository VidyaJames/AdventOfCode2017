f1 = open('input.txt', 'r')

valid = 0
for passphrase in f1.readlines():
	words = passphrase[:-1].split(' ')
	i = 0
	invalid = 0
	while i < len(words):
		check = sorted(words[i])
		for j in words[i+1:]:
			if check == sorted(j):
				invalid = 1
		i += 1
	if invalid == 0:
		valid +=1
print valid

