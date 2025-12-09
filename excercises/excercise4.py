food = ['fried rice', 'biriyani', 'fish', 'noodles', 'beef']

print(food[0])
print(food[-1])
print(food[1:4])

nums = [3,6,2,9,1]

print(nums.sort())
print(nums.append(10))
print(nums.pop(1))


sum = 0
for x in nums:
    sum +=x
    
print(sum)

numss=[x for x in range (21)]
squares = [x*x for x in range(10)]
evens = [x for x in numss if x % 2 == 0]
divbythree = [x for x in numss if x % 3 == 0]