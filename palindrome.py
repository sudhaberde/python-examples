def reverse(word):
	x = ''
	for i in range(len(word)-1,-1,-1):
		x += word[i]
	return x

word = input('give me a word:\n')
x = reverse(word)
print(word)
print(x)
if x == word:
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')

