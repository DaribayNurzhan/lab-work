import re
# #1
def first(word):
    p = re.search("ab+|a$", word)

    if p:
        print("YES")
    else:
        print("Ni")
word = input()
first(word)
# #2
def second(word):
    p = re.search("ab{2,3}", word)
    
    if p:
        print("YES")
    else:
        print("Ni")
word = input()
second(word)
# #3
def third():
    string = input()
    x = re.search('[a-z]+_[a-z]+', string)

    print(x)
third()

# #4
import re
string = input()
pattern = r"[a-z]*[A-Z]{1}[a-z]+"
matches = re.fullmatch(pattern, string)

if matches:
    print('YEs')
else:
    print('N')
# 5
import re
#5
w = input()
p = re.fullmatch('[B-Zb-z]*a[a-zA-Z]*b$', w)
if p:
  print('Yes')
else:
  print('No')
#6
w = input()
p = re.sub('[ ,.]',':', w)
print(p)
#7
import re

def seventh(text):
    words = text.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])
    
print(seventh(input()))

import re
#8
w = input()
p = re.findall('[a-z][A-Z]', r'\1 \2', w)
print(p)

# 9
import re

def ninth(str):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', str)

str = input()
result = ninth(str)
print(result)
#10
import re
def tenth(text):
    p = re.findall('[A-Z]*[a-z]+', text)
    
    return '_'.join(word.lower() for word in p)
print(tenth(input()))