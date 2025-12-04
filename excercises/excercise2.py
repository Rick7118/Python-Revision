#Profile generator

profile = {
    "name":input("Enter name:"),
    "age":int(input("Enter age:")),
    "hobbies":input("Enter hobbies:(comma-seperated):")
}

profile["hobbies"] = profile["hobbies"].split(",")
print(profile)

#Simple marks evaluator

maths = 78
english = 88
science = 85

average = (maths + english + science)//3

print(f"Total marks is {maths + english + science}")
print(f"Average marks is {average}")

if (average >= 80):
    print("Grade: A")
elif (average >=70):
    print("Grade: B")
elif (average >=60):
    print("Grade: C")
    
#username creator
first_name = "Ashmi"
last_name = "Sarkar"
birth_year = 2004

print(f"Your auto generated password is : {last_name}@{first_name}{birth_year}")

