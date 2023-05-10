from math import sqrt

def solve (a, b, c):
    print(f'Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0')
    D = b * b - 4 * a * c
    sqrtval = sqrt(abs(D)) 
    if D > 0:
        x1 = (-b + sqrtval) / (2 * a)
        x2 = (-b - sqrtval) / (2 * a)
        print(f'There are 2 roots:\nx1 = {x1}\nx2 = {x2}')
    elif D == 0:
        x = -b / (2 * a)
        print(f'There is one root: x = {x}')
    else:
        print('There are no roots in area of real numbers')