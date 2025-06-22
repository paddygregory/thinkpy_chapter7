def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print ('blastoff')

countdown(5)

def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print ('blastoff')
    while n < 0:
        print(n)
        n = n+1
    print ('blastoff')

countdown(-5)

def sequence(n):
    while n != 1:
        print(n)
    if n % 2 == 0: # n is even
       n = n / 2
    else: # n is odd
        n = n*3 + 1

sequence(5)
