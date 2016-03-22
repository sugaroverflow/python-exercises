#python
#to find all the prime #s between 2 and 1000




n = 2000
p = 2
i = 2
while p <= n:
    while i < n:
        if n%i == 0:
            return False
        i += 1
        print p,
    p=p+1

print "Here are all the primes between 2 - 2000"
