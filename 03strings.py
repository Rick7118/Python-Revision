course = "Python Programming"

print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:5])
print(course[:])

goal = "good \" pay" #backslash is an escape character
print(goal)

# \"
# \'
# \\
# \n  this is basically a new line

first = "Subhayu"
last = "Sengupta"
full = f"{first} {last}" #you can put any valid expression in between curly braces
print(full)

#string methods
print(course.upper()) #returns a new string, original string is not affected
print(course.lower())
print(course.title())
print(course.strip())

print(course.find("tho")) #if it returns -1 that means it was not found in the string
print(course.replace("P","x"))

print("Pro" in course) #returns boolean
print("doggy" not in course)