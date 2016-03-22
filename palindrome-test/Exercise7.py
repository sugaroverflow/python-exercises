#7 strings
print "Reading Palindromes"
print "Please enter a word."
word = str(raw_input(">>>"))

length = len(word)

num = 0

isPal = True


while(num < length/2 + 1):
	if(word[num:num+1] == word[-num-1]):
		isPal = True
		num = num + 1
	else:
		isPal = False
		num = num + 1

if(isPal == True):
	print "Yes, a palindrome!"

elif(isPal == False):
	print "Not a palindrome. Please try again."
