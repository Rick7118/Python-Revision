#conditionals

age = 20

if age >= 18:
    print("Adult")

age = 12

if age >= 18:
    print("Adult")
else:
    print("Minor")

marks = 85

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")


#Comparison

# ==   equal
# !=   not equal
# >    greater
# <    smaller
# >=   greater or equal
# <=   smaller or equal

#Logical

# and   # both must be true
# or    # at least one must be true
# not   # reverses boolean

#Truth and Falsy
#Python treats some values as False automatically

# 0
# "" (empty string)
# [] (empty list)
# {} (empty dict)
# None
# False

#Nested Conditionals

age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID requested")


#One line if

status = "Adult" if age >= 18 else "Minor"
