import math
a=int(input('First leg of the first right triangle: '))
a2=int(input('Second leg of the first right triangle: '))
b=int(input('First leg of the second right triangle: '))
b2=int(input('Second leg of the second right triangle: '))
def hypotenuse():
    c=math.sqrt(math.pow(a,2)+math.pow(a2,2))
    d=math.sqrt(math.pow(b,2)+math.pow(b2,2))
    print('Hypotenuse of the first triangle will be ',c)
    print('Hypotenuse of the second triangle will be ',d)
    if c>d:
        print('First hypotenuse is greater')
    elif c<d:
        print('Second hypotenuse is greater')
    else:
        print('They are equal')
hypotenuse()


