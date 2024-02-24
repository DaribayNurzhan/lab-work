#1
n=int(input())
a=[i**2 for i in range(1,n+1)]
print(a)
#2
n=int(input())
g_e=(i for i in range (1,n+1) if i%2==0)
for i in g_e:
    print(i)
#3
def divisible_by_3_and_4(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input())
for num in divisible_by_3_and_4(n):
    print(num)

#4
def squares (a,b):
    for i in range(a, b+1):
        yield i+2

a = int(input())
b = int(input ())
for j in squares (a, b):
    print(j)
#5
def decreasing(n):
    while n>=0:
        yield n
        n-=1
n=int(input())
for i in decreasing(n):
    print(i)