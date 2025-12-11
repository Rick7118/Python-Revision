#1
num = int(input("Enter a number: "))

if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("its zero")

#2
user_age = int(input("Enter your age: "))

if(user_age < 13):
    print("Child")
elif(user_age < 19):
    print("Teenager")
else:
    print("Adult")

#3
even_no = int(input("Enter a number(preferably evil hehe):"))

if(even_no % 2 == 0 and even_no > 10):
    print("All conditions are met")

#4
strr = input("Enter a string:")

if(strr):
    if(len(strr) < 5):
        print("Too short")
    else:
        print("Valid username")
else:
    print("invalid username")

#5
correct_username = "admin"
correct_password = "1234"

given_username = input("Enter your username")
given_password = input("Enter your password")

if(correct_password == given_password and correct_username == given_username):
    print("Login successful")
else:
    print("Access denied")

    