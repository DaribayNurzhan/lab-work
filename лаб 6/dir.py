import os
#1
import os
path = os.getcwd()
print("only directories:", [dire for dire in os.listdir(path) if os.path.isdir(dire)])
print("only files:", [file for file in os.listdir(path) if os.path.isfile(file)])
print("all dir and files:", os.listdir(path))
# #2
import os
path = os.getcwd()
print(f"Check for accessibility:\nExistence: {os.access(path, os.F_OK)} \nReadability: {os.access(path, os.R_OK)} \nWritability: {os.access(path, os.W_OK)} \nExecutability: {os.access(path, os.X_OK)}")
#3
import os
path = os.getcwd()
def checkForExistence(some_path):
    if os.access(some_path, os.F_OK):
        print(os.listdir(path))
    else:
        print("Given path doesn't exist")
checkForExistence(path)
#4
import os
with open('text.txt','r') as f:
    cnt = 0
    for i in f:
        cnt += 1
    print(cnt)
# 5
import os
lst = list(input().split())       
with open('text.txt', 'w') as f:
    for i in lst:
        f.write(str(i)+'\n')
#6
import string

for l in string.ascii_uppercase:
    f = l + '.txt'
    with open(f, 'w') as file:
        file.write(f"This is file {f}\n")   
# for removing
import string

for letter in string.ascii_uppercase:
    file_name = letter + '.txt'
    if os.path.exists(file_name):
        os.remove(file_name)
#7
import os
f = open('text.txt', 'r')
with open('capy.txt', 'w') as file:
    for x in f:
        file.write(x)

f.close()
#8
import os
if os.path.exists('copy_file.txt'):
    os.remove('copy_file.txt')