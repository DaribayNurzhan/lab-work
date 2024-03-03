#1
def multip(list):
    one = 1
    for num in list:
        one *= num
    return one
list = (4, 4, 4, 5, 7)
print(multip(list))
#2
def opredelitel(str):
    low = 0
    upper = 0
    for x in str:
        if x >= 'a' and x <= 'z':
            low += 1
        if x >= 'A' and x <= 'Z':
            upper += 1
    return low, upper
str = input()
print(opredelitel(str))
#3
def polwoker(str):
        
    if str == str[::-1]:
        print("yes")
    else:
        print("Try again")
str = input()
polwoker(str)
#4
import time, math
def sleeep(x, s):
    time.sleep(s/1000)
    return math.sqrt(x)
x = int(input("enter number:"))
s = int(input("enter time:"))
print(f"Output:\nSquare root of {x} after {s} miliseconds is {sleeep(x, s)}")
#5
tuple = (True, True, True, False)
print(all(tuple))
