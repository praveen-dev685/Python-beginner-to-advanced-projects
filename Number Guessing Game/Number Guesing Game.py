import random

print("----------------Welcome to Number guessing Game--------------")
# it was very funny because of we create a number guessing game without int data type 
while True:
    value = int(input("Enter the Number between (1 - 100) : "))
    value2 = []
    for i in range(1,100):
        value2.append(i)
    data = random.choice(value2)
    if(value == data):
        print("Your Choice : ",value)
        print("Computer    : ",data)
        print("You Won !!!")
    elif(value == ""):
        print("Please Choose any value between 1 to 100")
    elif(value > 100):
        print("Your value is greater than 100 !! ")
    else:
        print("Your Choice : ",value)
        print("Computer    : ",data)
        print("type :",type( data),type(value))
        print("Try Agaiin !!!")
        
