nums = [10, 20, 30]
fruits = ["apple","banana","mango"]
mixed = [1, "hello" ,3.14 ,True ]

#Indexxing

fruits = ["apple", "banana", "mango"]

fruits[0]   # 'apple'
fruits[1]   # 'banana'
fruits[-1]  # 'mango'

#Slicing

nums = [1,2,3,4,5]

nums[1:4]   # [2,3,4]
nums[:3]    # [1,2,3]
nums[2:]    # [3,4,5]
nums[:]     # full copy

#Lists are mutable

nums = [10, 20, 30]
nums[0] = 99     # [99, 20, 30]

#Adding Elements

nums.append(40)
nums.insert(1, 15)   # insert 15 at index 1


#Removing Elements

nums.pop(2)    # removes index 2
fruits.remove("banana")
nums.clear()

#checking items in list

if ("apple" in fruits):
    print("Yes, we got apples")

#Looping through a list

for item in fruits:
    print(item)

for idx, item in enumerate(fruits):  #use this if you need index + value
    print(idx, item)

#List comprehension

squares = [x*x for x in range(10)]
evens = [x for x in nums if x % 2 == 0]

#Nested Lists

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix[1][2]   # 6


#Useful list functions & methods

len(nums)
nums.sort()
nums.reverse()
min(nums)
max(nums)
sum(nums)




