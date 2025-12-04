a = 10
b = 3

#Arithmetic Operators
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#Comparison Operators

'''
==     equal
!=     not equal
>      greater
<      smaller
>=     greater or equal
<=     smaller or equal

'''

print(a==10)
print(a > 5)
print(a < 3)
print(a >= b)

#Logical Operators

'''
and
or
not

'''

age = 21

print(age >18 and age < 60)
print(age < 18 or age > 60)
print(not(age < 18))

#Assignment Operators

'''
+=     add and assign
-=     subtract and assign
*=     multiply and assign
/=     divide and assign
//=    floor divide and assign
%=     remainder and assign

'''

#Using Operators in Real Code

age = int(input("Enter age: "))

if age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("Not an adult.")

