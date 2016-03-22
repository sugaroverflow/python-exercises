

output = ""
count = 1
diff = 0
while(count <= 6):
    starcount = (count * 2) - 1
    diff = 6 - count
    while (diff > 0):
        output = output + " "
        diff = diff - 1
    while (starcount > 0):
        output = output + "*"
        starcount = starcount - 1
    print output
    output = ""
    count = count + 1
