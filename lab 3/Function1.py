
#1
def GramToOunce(x):
    ounce = x * 28.3495231
    return ounce
gram = 20 #int(input)
print(GramToOunce(gram))


#2
def Cel(Ft):
    Ct = (5/9) * (Ft - 32)
    return Ct
t = 370
print(Cel(t))



#3
def solve(numheads, numlegs):
    rabbits = int((numlegs - numheads * 2)/2)
    chickens = int(numheads - rabbits)
    print("rabbits:", rabbits)
    print("chickens:", chickens)
solve(35, 94)


#4
def prime(num):
    caunt = 0
    if num <= 1:
        return False
    for i in range(1, num):
        if num % i == 0:
            caunt += 1
    if caunt != 1:
        return False
    return True


def filter_prime(number):
    prime_number = []
    for num in number:
        if prime(num):
            prime_number.append(num)
    return prime_number



pnumber = input()
number = pnumber.split()
number = [int(num) for num in number]
prime_number = filter_prime(number)
print(prime_number)
    

#5
import itertools
def permutation(stringz):
    perm_set = itertools.permutations(stringz) 
    for val in perm_set: 
        print(val)
word = input()
permutation(word)
        
 

#6
def no(sen):
    sen.reverse()
    for x in sen:
        print(x, end=' ')
sen = input()
sen = sen.split()
no(sen)


#7
def dettector(x):
    for i in x:
        if i == len(x) - 1:
            print(False)
            break
        if x[i] == 3 and x[i + 1] == 3:
            print(True)
            break
    else:
        print(False)

x = input()
x = x.split()
x = [int(y) for y in x]
dettector(x)


#8
def spy_game(x):
    caunt = 0
    caunt2 = 0
    caunt3 = 0
    pos = []
    pos1 = 0
    for i in range(len(x)):
        
        if x[i] == 0:
            pos.append(i) 

            caunt += 1
        if x[i] == 7:
            pos1 = i
            caunt2 += 1
    if caunt >= 2 and caunt2 >= 1:
        for i in pos:
            if i < pos1:
                caunt3 += 1
    if caunt3 >= 2:
        print(True)
    else:
        print(False)

x = input()
x = x.split()
x = [int(y) for y in x]
spy_game(x)


#9
def v(r):
    volume =  r*r*r*3.14*4
    volume =int(volume/3)
    print(volume)
r = int(input())
v(r)


#10
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
input_list = [1, 2, 3, 4, 2, 3, 5]
result_list = unique_elements(input_list)
print(result_list)


#11
def palindrome(word):
    drow = word[::-1]
    if word == drow:
        print("There is palindrome")
        
    else:
        print("No")


word = input()
palindrome(word)


#12
def histogram(x):
    for i in x:
        for j in range(i):
            print("*", end='')
        print(end='\n')        
num = input()
num = num.split()
num = [int(x) for x in num]
histogram(num)


#13
import random
def gtn():
    guess = random.randint(1, 20)
    print('Hello! What is your name?')
    name = input()


    print('Well,',name, ', I am thinking of a number between 1 and 20.\nTake a guess.')
    number = int(input())
    caunt = 1

    while True:
        if number != guess:
            caunt += 1
        if number == guess:
            print('Good job,',name,'! You guessed my number in',caunt,'guesses!')
            break
        if number < guess:
            print('Your guess is too low.\nTake a guess.')
            number = int(input())
        if number > guess:
            print('Your guess is too big.\nTake a guess.')
            number = int(input())



gtn()










