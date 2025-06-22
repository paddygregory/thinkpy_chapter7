def squareroot(a,x):
    while True:
        y = (x+a/x) /2
        print(y)
        if y == x:
            break
        x = y

squareroot(25,7)

squareroot(100,21)

def exactsquareroot(a,x):
    while True:
        y = (x+a/x) /2
        print(y)
        if abs(y - x) < 0.00001:
            break
        x=y

exactsquareroot(25,7)

exactsquareroot(100,21) 