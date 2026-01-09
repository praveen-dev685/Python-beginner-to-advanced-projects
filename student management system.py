students_data = []

print("-------------Students Management System-------------")
while True:
    print("1. --------> Add Students ")
    print("2. --------> Update Students")
    print("3. --------> Delete Students")
    print("4. --------> View All Students")
    print("5.---------> Exit")

    request = input("Enter the choice : ")

    class Students:
        def add(self):
            name = input("Enter The name of Student : ")
            age = int(input("Enter the  Age of that Student :"))
            roll_no = int(input("Enter the Roll no : "))
            class_section = input("Enter the class section : ")
            address=input("Enter the Address : ")
            phone=input("Enter the phone number : ")

            stu_data={
                "name":name,
                "age":age,
                "roll_no":roll_no,
                "class":class_section,
                "address":address,
                "phone":phone,
                },
            students_data.append(stu_data)
            print("Student Record added Successfully")
            print("This is Your Student id :",(len(students_data)-1))
            
        def update(self):
            stu_id = int(input("Enter the Student id : "))
            print(students_data[stu_id])
            name = input("Enter The name of Student : ")
            age = int(input("Enter the  Age of that Student :"))
            roll_no = int(input("Enter the Roll no : "))
            class_section = input("Enter the class section : ")
            address=input("Enter the Address : ")
            phone=input("Enter the phone number : ")

            stu_data1={
                "name":name,
                "age":age,
                "roll_no":roll_no,
                "class":class_section,
                "address":address,
                "phone":phone,
                },
            students_data.pop(stu_id)
            students_data.insert(stu_id,stu_data1)
            print("Student Record Updated Successfully")
            print(students_data)
            
        def view(self):
            print(students_data)
            print("Students Records Viewed Successfully")

        def deleted(self):
            req = input("Are You sureto delete the student name : (yes/no)").strip().lower()
            if(req=="yes"):
                stu_id = int(input("Enter the Student Id : "))
                students_data.pop(stu_id)
                print("Student Data Deleted Successfully")
            else:
                pass
            
    if(request == "1"):
        data = Students()
        data.add()
    elif(request=="2"):
        data = Students()
        data.update()
    elif(request=="3"):
        data=Students()
        data.deleted()
    elif(request=="4"):
        data = Students()
        data.view()
    elif(request=="5"):
        break
    else:
        print("Please choose any option ")
        
    

