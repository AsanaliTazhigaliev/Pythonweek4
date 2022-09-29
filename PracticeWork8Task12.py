import math
x = 3
print('Начальное значение: ', x)
def pr():
    global x
    x=math.pow(x,10)
    print('Изменённое значение: ',x)
pr()