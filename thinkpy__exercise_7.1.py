import math

def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < 0.00001:
            break
        x = y
    return y  # ✅ This is crucial!

def test_square_root():
    print('a  mysqrt(a) math.sqrt(a)  diff')
    print ('-------------------------------')
    for a in range(1,10):
        print( 'a', mysqrt(a), math.sqrt(a), abs(mysqrt(a)) - math.sqrt(a))

test_square_root()
def test_square_root():
    print('a  mysqrt(a) math.sqrt(a)  diff')
    print ('-------------------------------')
    for a in range(1,10):
        print( a, mysqrt(a), math.sqrt(a), abs(mysqrt(a)) - math.sqrt(a))
test_square_root()


