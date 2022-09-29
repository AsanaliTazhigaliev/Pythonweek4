import math
def s(x,y,z):
    p=(x+y+z)/2
    s=math.sqrt(p*(p-x)*(p-y)*(p-z))
    return s
A=[]
for i in range(3):
    print('enter the sides of the',i,' triangle: ')
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    A.append(s(a,b,c))
for i in range(3):
    print('Area of',i,' triangle 1{:.2f}'.format(A[i]))
if A[0]==A[1]:
    if A[0]==A[2]:
        print('Triangles are the same')
else: print('Triangles are not the same')
