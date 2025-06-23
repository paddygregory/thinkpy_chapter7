def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a / x) / 2          # y is the estimate square root of a
        print(y)
        if abs(y - x) < 0.00001:
            break
        x = y

mysqrt(25)
mysqrt(67)

def test_square_root():
    print('a  mysqrt(a) math.sqrt(a)  diff')
    print ('-------------------------------')

test_square_root()

import math

def test_square_root():
    print('a  mysqrt(a) math.sqrt(a)  diff')
    print ('-------------------------------')
    for a in range(1,10):
        print( 'a', mysqrt(a), math.sqrt(a), abs(mysqrt(a) - math.sqrt(a)))

test_square_root()

def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a / x) / 2          # y is the estimate square root of a
        print(y)
        if abs(y - x) < 0.00001:
            break
        x = y
        return y
    
def test_square_root():
    print('a  mysqrt(a) math.sqrt(a)  diff')
    print ('-------------------------------')
    for a in range(1,10):
        print( 'a', mysqrt(a), math.sqrt(a), abs(mysqrt(a) - math.sqrt(a)))

test_square_root()

def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a / x) / 2          # y is the estimate square root of a
        print(y)
        if abs(y - x) < 0.00001:
            break
        x = y
    return y

def test_square_root():
    print('a  mysqrt(a) math.sqrt(a)  diff')
    print ('-------------------------------')
    for a in range(1,10):
        print( 'a', mysqrt(a), math.sqrt(a), abs(mysqrt(a) - math.sqrt(a)))

def test_square_root():
    print('a  mysqrt(a) math.sqrt(a)  diff')
    print ('-------------------------------')
    for a in range(1,10):
        print( 'a', mysqrt(a), math.sqrt(a), abs(print(mysqrt(a)) - math.sqrt(a)))

test_square_root()

def test_square_root():
    print('a  mysqrt(a) math.sqrt(a)  diff')
    print ('-------------------------------')
    for a in range(1,10):
        print( 'a', mysqrt(a), math.sqrt(a), abs(mysqrt(a)) - math.sqrt(a))

test_square_root()

def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a / x) / 2          # y is the estimate square root of a
        print(y)
        if abs(y - x) < 0.00001:
            break
            return y 
        x = y

def test_square_root():
    print('a  mysqrt(a) math.sqrt(a)  diff')
    print ('-------------------------------')
    for a in range(1,10):
        print( 'a', mysqrt(a), math.sqrt(a), abs(mysqrt(a)) - math.sqrt(a))

test_square_root()
test_square_root()

def test_square_root():
    print('a  mysqrt(a) math.sqrt(a)  diff')
    print ('-------------------------------')
    while 10>a:
        a = 1
        print( 'a', mysqrt(a), math.sqrt(a), abs(mysqrt(a)) - math.sqrt(a))
        a = a +1

test_square_root()
