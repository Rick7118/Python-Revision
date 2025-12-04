#input()

name = input("Enter your name: ")
age = int(input("Enter your age: "))      # "21" → 21
gpa = float(input("Enter GPA: "))         # "8.4" → 8.4
height = float(input("Enter your height in cms:"))

#print()

print("Name:", name, "Age:", age)

print(f"Hello {name}, you are {age} years old")

print(f"Your height in meters is {height/100}")

#Using input in conditions — the first interactive logic

age_1 = int(input("Enter her age: "))

if age_1 >= 18:
    print("They are an adult")
else:
    print("You are a minor.")
    
#Taking multiple values in a single input

raw = input("Enter three numbers seperated by spaces: ")
parts = raw.split()
print(raw) #Output is in string
numbers = [int(x) for x in parts]

#Input to dict

order = {
    "starter":input("starter: "),
    "quantity":int(input("quantity: ")),
    "price":float(input("price: "))
}


