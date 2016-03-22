#!/usr/bin/python

#get the user input
print ("Welcome to the palindrome checker")
string = raw_input("Give me a line of text: ")
reversestr = ""


# split the string
# and put it into an array
# ex: 'hello' --> ['h', 'e', 'l', 'l', 'o']
array = []
x = 0
while (x <= len(string) - 1):
    array.append(string[x])
    x += 1
# print "regular array: ", array #testcode

# split the string
# and put it into an array in reverse
# ex: 'hello' --> ['o', 'l', 'l', 'e', 'h']
reverse_array = []
y = len(string) - 1
while (y >= 0):
    reverse_array.append(string[y])
    y -= 1

# print "reverse array: ", reverse_array #testcode

# check the two arrays against each other
# if all the values are the same
# we have a palindrome
i = 0
flag = True
while( i <= len(string) - 1):
    if(array[i] == reverse_array[i]):
        flag = True
    else:
        flag = False
    i += 1

if (flag == True):
    print "------>YES! " + string + " is a palindrome!"
else:
    print "------>NO! " + string + " is not a palindrome"
