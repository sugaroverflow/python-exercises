# word = str(raw_input(">>>"))
word="racecar"
length = len(word)

num = 0

# print(word[1])
# print(word[-1])


isPal = True

while(num < length/2 + 1):
    print("---->num is " + str(num))
    if(num == 0): #special case
        print(word[num] + "," + word[-1])
        if(word[num] == word[-1]):
            isPal = True
        else:
            isPal = False
        print isPal
    else:
        print(word[num:num+1] + "," + word[-num-1])
        if(word[num:num+1] == word[-num-1]):
            isPal = True
        else:
            isPal = False
        print isPal
    if(isPal == False):
        break;
    num = num + 1

if(isPal == False):
    print "Not a palindrome. Please try again."
    num = num + 1
if(isPal == True):
    print "Yes a palindrome!"
    num = num + 1
