f1 = open('input.txt', 'r')

valid = 0
for passphrase in f1.readlines():
	words = passphrase[:-1].split(' ')
	if len(words) == len(set(words)):
		valid += 1
print valid
