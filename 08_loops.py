#for loops

for x in [10,20,30]:
    print(x)

for char in "python":
    print (char)

for i in range(5):
    print(i)

for j in range(2,10,2): #start,stop,step
    print(j)

nums =[5,10,5]

for n in nums:
    print(n)

#looping with index using enumerate()

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

#looping through a dictionary

# for key in student:
#     print(key)

# for value in student.values():
#     print(value)

# for k, v in student.items():
#     print(k, v)

#while loop

i = 1

while i <= 5:
    print(i)
    i += 1

#break and continue

for x in range(10):
    if x == 5:
        break
    print(x)

#nested loops

# for row in grid:
#     for item in row:
#         print(item)

for x in range(20):
    if x % 2 == 0:
        print(x)
