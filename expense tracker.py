daily_payments = []
user_id = 0



def add_expense(name, amount, category, date):
    global user_id
    user_id += 1
    
    value = {
        "id": user_id,
        "user_name": name,
        "user_amount": float(amount),
        "user_category": category,
        "user_date": date
    }
    daily_payments.append(value)
    print("Expense Added Successfully!!!")



def view_expense():
    if not daily_payments:
        print("No Expenses Found!")
        return

    for i in daily_payments:
        print(i)
    print("Show Expenses Successfully!!!")


def edit_expense(edit_id, name, amount, category, date):
    for item in daily_payments:
        if item["id"] == edit_id:
            item["user_name"] = name
            item["user_amount"] = float(amount)
            item["user_category"] = category
            item["user_date"] = date
            print("Expense Updated Successfully!!!")
            return
    print("Expense ID Not Found!!!")



def delete_expense(exp_id):
    for item in daily_payments:
        if item["id"] == exp_id:
            daily_payments.remove(item)
            print("Deleted Successfully!!!")
            return
    print("Expense ID Not Found!!!")

def total_expense():
    total = sum(item["user_amount"] for item in daily_payments)
    print("Total Expense =", total)




while True:
    print("\n----- Expense Manager -----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Total Expense")
    print("6. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        amount = input("Enter Amount: ")
        category = input("Enter Category: ")
        date = input("Enter Date: ")
        add_expense(name, amount, category, date)

    elif choice == "2":
        view_expense()

    elif choice == "3":
        edit_id = int(input("Enter ID to Edit: "))
        name = input("Enter New Name: ")
        amount = input("Enter New Amount: ")
        category = input("Enter New Category: ")
        date = input("Enter New Date: ")
        edit_expense(edit_id, name, amount, category, date)

    elif choice == "4":
        delete_id = int(input("Enter ID to Delete: "))
        delete_expense(delete_id)

    elif choice == "5":
        total_expense()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")


        



    
    
