#int

score = 95
year = 2025

wins = 10 + 3
losses = 20 - 7
ratio = 7 // 3   # floor division → 2
ratio_2 = 7/3    #2.33
rem = 7 % 3      # remainder → 1

#float

price = 19.99
cgpa = 8.7
height = 175.5

speed_of_light = 3e8   # 3 × 10^8

#str

name = 'Subhayu'

s = "python"

s[0]        # 'p'
s[1:4]      # 'yth'
s.upper()   # 'PYTHON'
len(s)      # 6

#bool

is_adult = True
is_coder = True

'''
True == 1     
False == 0

'''

#list

scores = [ 10, 20, 30]
names = ["Ram", "Shyam", "Rahul"]
mixed = [1, "apple", 3.14 ,True]

#you can mutate lists

scores.append(40)
scores[0] = 99

#you can slice them

scores[1:3] #10 20

#tuples

point = (10, 20)
colors = ("red", "green", "blue")

#dictionary

student = {
    "name": "Subhayu",
    "age": 21,
    "skills": ["python", "ai"]
}

student["name"] #access
student["age"] = 22 #update

#set

nums = {1, 2, 3, 3}
print(nums)  # {1, 2, 3}

#None

data = None

#Casting -- converting between types

int("10")        # 10
float("2.5")     # 2.5
str(123)         # "123"
list("hello")    # ['h','e','l','l','o']

age = int(input("Enter age: ")) #input is always a string










