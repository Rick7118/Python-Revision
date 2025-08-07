for number in range(1,10,2):
    print("attempt",number  ,(number) * "." )
    
succesful = False
for number in range(3):
    print("Attempt")
    if succesful:
        print("Sucessful")
        break;
else:
    print("Attempted 3 times and failed")
