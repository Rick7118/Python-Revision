def greet():
    print("Hi there")
    print("Welcome aboard")
    
greet()

def greet2(first_name , last_name):
    print(f"Hi {first_name} {last_name}")
    
greet2("Subhayu","Sengupta")

# 1 - Perform a task
# 2 - Return a value

def get_greet(name):
    return f"Hi {name}"

message = get_greet("Ashmi")
file = open("content.txt","w")
file.write(message)