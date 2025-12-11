def greet():
    print("hello")

greet()

def greeet(name):
    print(f"Hello {name} tu chutiya he")

greeet("Rick")

def add(a,b):
    return a + b

result = add(7,8)
print(result)

def welcome(name="guest"):
    print(f"Welcome, {name}!")

def stats(nums):
    return max(nums), min(nums), sum(nums)

def outer():
    def inner():
        print("inside inner")
    inner()

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
print(double(5))   # 10
