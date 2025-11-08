import re
from spfprints import Second_data
from spfprints import Ac_Coach_data
import spfdata

class Second_coach:
    def second_class(self):
        sup_start = input("Enter the Current Stop : ").lower().strip()
        sup_end =   input("Enter the Destination : ").lower().strip()
        sup_coach = input("Enter the coach (Sleeper / general) : ").strip()
        print("Wait !!!  We can check  Availability.......")
        print("Availability is here .......")
        if(sup_coach == "sleeper" or sup_coach == "general"):
            sup_user_name = input("Enter your name : ").lower()
            sup_train_start = input("Enter the Current stop : ").lower()
            sup_train_end =  input("Enter the  destination : ").lower()
            sup_frequently = "Weekly Once"
            sup_train_no = int(input("Enter the Train Number Properly : "))
            if(sup_train_no != ""):
                sup_adult = int(input("How Many Adults : "))
                sup_child = int(input("How Many Childs : "))
                sup_price_adult = 0
                sup_price_child = 0
                print("Cash Methods :  Gpay , PayTM , Phone Pay , Bharat Pay")
                cash_methods = input("Payments Methods : ").lower()
                if(cash_methods == "gpay" or cash_methods == "paytm" or cash_methods == "phone pay" or cash_methods=="bharat pay"):
                    for i in range(3):
                        print("Redirecting your payment Gateway..........")
                pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+$"

                gpay_id = input("Enter your UPI Id : ")
                if not re.match(pattern, gpay_id):
                    print("Invalid UPI ID format. Please enter like name@bank")
                else:
                    gpay_pass= int(input("Enter the UPI pin : "))
                    if(gpay_id!="" and gpay_pass!=""):
                        for j in range(3):
                            print("Waiting for Response >>>>>>")
                    print("Payment Successfull !!!         Collect Your Ticket  !!!")
                    sup_price_adult,sup_price_child = spfdata.second_price(sup_start,sup_end,sup_coach)
                    data = Second_data(sup_start,sup_end ,sup_coach,sup_user_name,sup_train_start,sup_train_end,sup_frequently,sup_train_no,sup_adult,sup_child,cash_methods,gpay_id,sup_price_adult,sup_price_child)
                   
                    data.second_prints()
        else:
            print("Please Select vaild payment gateway")

class Ac_coachs:
    def ac_class(self):
        print("-----------------PLEASE FILL THE RESERVATION FORM--------------------")
        ac_name = input("Enter your name : ")
        ac_start = input("Enter the Current Stop : ").lower().strip()
        ac_end =   input("Enter the Destination : ").lower().strip()
        ac_coach = input("Enter the coach  : ").strip().lower()
        print("Wait !!!  We can check  Availability.......")
        print("Available Slots...................")
        odd=[]
        even=[]
        five=[]
        seven = []
        for a in range(1,21):
            if(a%2==1):
                odd.append(a)
        for b in range(30,51):
            if(b%2==0):
                even.append(b)
        for c in range(50,101):
            if(c%5==0):
                five.append(c)
        for d in range(101,171):
            if(d%7==0):
                seven.append(d)
        print(odd)
        print(even)
        print(five)
        print(seven)
        slots = input("Enter your slots : ").split()
        slots = list(slots)
        ac_adult = int(input("How many Adults : "))
        ac_child = int(input("How many Childs : "))
        ac_adult_price = 0
        ac_child_price = 0
        ac_platform = 0
        print("Cash Methods :  Gpay , PayTM , Phone Pay , Bharat Pay")
        cash_methods = input("Payments Methods : ").lower()
        if(cash_methods == "gpay" or cash_methods == "paytm" or cash_methods == "phone pay" or cash_methods=="bharat pay"):
            for i in range(3):
                print("Redirecting your payment Gateway..........")
            pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+$"

            gpay_id = input("Enter your UPI Id : ")
            if not re.match(pattern, gpay_id):
                print("Invalid UPI ID format. Please enter like name@bank")
            else:
                gpay_pass= int(input("Enter the UPI pin : "))
                if(gpay_id!="" and gpay_pass!=""):
                    for j in range(3):
                        print("Waiting for Response >>>>>>")
                    print("Payment Successfull !!!         Collect Your Ticket  !!!")
                    ac_adult_price,ac_child_price,ac_platform = spfdata.ac_price(ac_start,ac_end,ac_coach)
                    data1 = Ac_Coach_data(ac_name,ac_start,ac_end,ac_coach,ac_adult,ac_child,ac_adult_price,ac_child_price,ac_platform,cash_methods,gpay_id,slots)
                    data1.ac_prints()
        else:
            print("Please Select vaild payment gateway")        



           
                    


