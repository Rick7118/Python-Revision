#Strings
'''
p   y   t   h   o   n
0   1   2   3   4   5
-6 -5  -4  -3  -2  -1

'''

s = 'python'
s[0]
s[3]
s[-1]

#Slicing

s[1:4] #yth
s[:3] #pyt
s[3:] #hon
s[:]

#Strings are immutable

s = "m" + s[1:]
print(s)

#String Methods

s = s.upper()
s = s.lower()

s.replace("my","java")

#split->list
"apple,banana,mango".split(",")

#join->string
"-".join(["A","B","C"]) 

#find
"python".find("th") #2
"python".find("z") #-1

s.startswith("py")
s.endswith("on")

name = 'Subhayu'
age = 21
print(f"My name is {name} and I am {age} years old")
print(f"In 5 years you will be {age + 5}")

#length
len("python")

#looping through a string
for char in "relationship":
    print(char)

#creating modified versions of strings

s = "python"
s = s[0].upper() + s[1:] #Capitalizing the first letter

result = ""
for char in s:
    if char not in "aeiou":
        result +=char 



