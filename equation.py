from math import *
n='ax+bx+c=0'
print(n)


a = float(input('entre le valeur de a : '))
b = float(input('entre le valeur de b : '))
c = float(input('entre le valeur de c : '))

def resoud(a,b,c):
    delt = pow(b, 2)-4*a*b
    print(delt)
    if delt > 0:
        x1 = (-b+sqrt(delt))/2*a
        x = (-b-sqrt(delt))/2*a
        solu = f"x1 = {x1} ; x = {x}"
        return solu
    elif delt < 0:
        n="cette equation admet pas de solution "
        return n
test = resoud(a, b, c)
print(test)
# delt = pow(b, 2)-(4*a*b)

# print(delt)
    

