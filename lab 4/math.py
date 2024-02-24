import math

#1 degree to radians
import math
def toRadian(degree):
    radian = math.radians(degree) 
    return radian
degree = int(input("введи градус:\n"))
print(toRadian(degree))

#2
def areaoftrap(height, firstside, secondside):
    area = height * (firstside + secondside)/ 2
    return area
height = int(input("введи высоту:\n"))
firstside = int(input("введи первую сторону:\n"))
secondside = int(input("введи вторую сторону:\n"))
print(areaoftrap(height, firstside, secondside))

#3
def toRadian(degree):
    radian = math.radians(degree) 
    return radian

def arearight(n, l):
    
    p = n * l
    radian = toRadian(180/n)
    a = (2 * math.tan(radian))

    print(a)
    a = l / a
    area = (a * p)/2
    return int(area)
n = int(input("введи количество сторон:\n"))
l = int(input("введи длину:\n"))
print(arearight(n, l))

#4
def areaparealel(l, h):
    area = l * h
    return area
h = int(input("введи высоту:\n"))
l = int(input("введи длину:\n"))
print(areaparealel(l, h))
