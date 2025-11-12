import random #Choose Random Values

print("----------------------------- Welcome to Rock Paper Scissor Game --------------------------")
while True:
    human_data = input("Enter Your Choice (Rock,Paper,Scissor) : ").lower().strip()
    computer = ["rock",'paper','scissor']
    comp_val = random.choice(computer) # random.choice is helps to choose anything in the list
    if(human_data == comp_val):
        print("Result : Draw !!! ")
        print("Your Choice : ",human_data)
        print("Computer : ", comp_val)
    elif(human_data == "paper" and comp_val == "scissor"):
        print("Your Choice : ",human_data)
        print("Computer : ",comp_val)
        print("Result : Computer Won !!! Try Again !!!")
    elif(human_data == "scissor" and comp_val=="rock"):
        print("Your Choice : ",human_data)
        print("Computer : ",comp_val)
        print("Result : Computer Won !!! Try Again !!!")
    elif(human_data=="rock" and comp_val=="paper"):
        print("Your Choice : ",human_data)
        print("Computer : ",comp_val)
        print("Result : Computer Won !!! Try Again !!!")
    elif(human_data == "" ):
        print("Please Select Anyone !!!")
    else:
        print("Your Choice : ",human_data)
        print("Computer : ",comp_val)
        print("Result : You Won !!! Play Again !!!")
