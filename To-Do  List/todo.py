task = []


def addtask(data):
    task.append(data)
    print("Task Added Successfully !!!")
    print("This is your task id : ",(len(task)-1))
def updatetask(data,change):
    task[data] = change
    print("Task Updated Successfully !!!")
def removetask(data):
    try:
        task.pop(data)
        print("Task Deleted Successfully !!!")
    except Exception as e:
        print("Please Fisrt Add Task !!!")
    
def showtask():
    print(task)
    print("Showed Task Successfully !!!")

while True:
    print("====> 1. Add Task ")
    print("====> 2. Update Task ")
    print("====> 3. Delete Task ")
    print("====> 4. Show Task ")
    print("====> 5. Exit ")
    print("-----------------------------------")

    value = int(input("Enter your tasks (1 - 5) : "))
    if(value == 1):
        tasks = input("Enter your tasks : ")
        addtask(tasks)
    elif(value == 2):
        task1 = int(input("Enter your  task id  : "))
        uptask =input("Enter your updated Task : ")
        if((len(task)-1) >= 0 ):
            updatetask(task1,uptask)
        else:
            print("Please First Add Tasks !!!")
    elif(value == 3):
        task2 = int(input("Enter your  task id  : "))
        if(task2 >= 0):
            removetask(task2)
    elif(value == 4):
        print(task)
    else:
        print("Exit Successfully !!!!");
        break
    
           
       
