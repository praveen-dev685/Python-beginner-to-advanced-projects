
# Train Booking System
import re
import localtrain
from expresstrain import Express_trains
from superfasttrain import Second_coach
from superfasttrain import Ac_coachs



while True:
    print("--------------------------------------WELCOME TO INDIAN RAILWAYS------------------------------------")
    print("1. New user")
    print("2. Already you have an account ?")
    verify = input("Enter your status : ")
    if(verify == "1"):
        print("Welcome......")
        fname = input("Enter your first name : ")
        lname = input("Enter your last name : ")
        phone_no =input("Enter Your phone Number : ")
        if(len(phone_no) == 10):
            password = input("Enter your password : ")
            print("Thank you Your data was stored ....")
            break
        else:
            print("Invalid Phone number ....")
    elif(verify == "2"):
        username=input("Enter your name : ")
        pass_wrd = input("Enter your password : ")
        if(username!="" and pass_wrd !=""):
            print(f"Welcome back {username} .......")
            break
        else:
            print("Invalid text written......")
while True:   
    print("----------------------------------------TRAIN TYPES-------------------------------------------------")
    print("--------> 1. Local Trains")
    print("--------> 2. Express Trains")
    print("--------> 3. Superfast Express Trains")

    check_trains = input("Which type of trains you needed : ").lower()
    if(check_trains == "local trains" or check_trains == "1"):
        print("---------------------------------------------------------------------")
        print(  "Chennai Beach",      "Chennai Fort",       "Chennai Park",)
        print(  "Chennai Egmore",      "Chetpet",           "Nungambakkam",)
        print(  "Kodambakkam",         "Mambalam",          "Saidapet",)
        print(  "Guindy",             "St. Thomas Mount",   "Pazhavanthangal",)
        print(  "Meenambakkam",       "Pallavaram",         "Chromepet",)
        print(  "Tambaram Sanatorium", "Tambaram",          "Perungalathur",)
        print(  "Vandalur",           "Urapakkam",          "Guduvancheri",)
        print(  "Potheri",            "Singaperumal Koil",  "Chengalpattu")
        print("----------------------------------------------------------------------")

        loc_start = input("Enter your currect stop : ").lower()
        loc_end = input("Enter your destination : ").lower()
        adult = int(input("how many adults to Travel : "))
        child = int(input("how many child to Travel : "))
        localtrain.train_price(loc_start,loc_end,adult,child)
        print("Cash Methods :  Gpay , PayTM , Phone Pay , Bharat Pay")
        cash_methods = input("Payments Methods : ").lower()
        if(cash_methods == "gpay"):
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
            localtrain.ticket(adult,child,cash_methods,loc_start,loc_end)
                    
        

        if(cash_methods == "paytm"):
            for i in range(3):
                print("Redirecting your payment Gateway..........")
            pattern = r'^[a-zA-Z0-9._]+@paytm$'

            paytm_id = input("Enter your UPI Id : ")
            if not re.match(pattern, paytm_id):
                print("Invalid UPI ID format. Please enter like name@paytm")
            else:
                paytm_pass= int(input("Enter the UPI pin : "))
                if(paytm_id!="" and paytm_pass!=""):
                    for j in range(3):
                        print("Waiting for Response >>>>>>")
                print("Payment Successfull !!!         Collect Your Ticket  !!!")
                localtrain.ticket(adult,child,cash_methods,loc_start,loc_end)
        
                    

        if(cash_methods == "phone pay"):
            for i in range(3):
                print("Redirecting your payment Gateway..........")
            pattern = r'^[0-9]{10}@ybl$'

            phonepay_id = input("Enter your UPI Id : ")
            if not re.match(pattern, phonepay_id):
                print("Invalid UPI ID format. Please enter like praveen@ybl")
            else:
                phonepay_pass= int(input("Enter the UPI pin : "))
                if(phonepay_id!="" and phonepay_pass!=""):
                    for j in range(3):
                        print("Waiting for Response >>>>>>")
                print("Payment Successfull !!!         Collect Your Ticket  !!!")
                localtrain.ticket(adult,child,cash_methods,loc_start,loc_end)
                    
        

        if(cash_methods == "bharat pay"):
            for i in range(3):
                print("Redirecting your payment Gateway..........")
            pattern = r'^[a-zA-Z0-9._]+@upi$'

            bharatpay_id = input("Enter your UPI Id : ")
            if not re.match(pattern, phonepay_id):
                print("Invalid UPI ID format. Please enter like  praveen@upi")
            else:
                bharatpay_pass= int(input("Enter the UPI pin : "))
                if(bharatpay_id!="" and bharatpay_pass!=""):
                    for j in range(3):
                        print("Waiting for Response >>>>>>")
                print("Payment Successfull !!!         Collect Your Ticket  !!!")
                localtrain.ticket(adult,child,cash_methods,loc_start,loc_end)
                    
        

#------------------Local Trains Ended------------------------------------------- 

    elif(check_trains == "express trains" or check_trains == "2"):
        print("-----------------------------------AVAILABLITY TRAINS-------------------------------------------------------")
        exp_routes = {
            "Madurai Express"    :    "Train No : 16160 / 16159  Chennai Egmore - Madurai",
            "Coimbatore Express" :    "Train No : 16128 / 16127  Chennai Egmore - Coimbatore",
            "Tirunelveli Express" :   "Train No : 16184 / 16183  Chennai Egmore - Tirunelveli",
            "Nagercoil Express " :    "Train No: 16182 / 16181   Chennai Egmore - Nagercoil",
            "Karaikkudi Express" :    "Train No: 16160 / 16159   Chennai Egmore - Karaikkudi",
            "Rameswaram Express" :    "Train No: 16128 / 16127   Chennai Egmore - Rameswaram",
            "Tiruchirappalli Express":"Train No: 16160 / 16159   Chennai Egmore - Tiruchirappalli",
            "Thoothukudi Express":    "Train No: 16128 / 16127   Chennai Egmore - Thoothukudi",
            "Villupuram Express" :    "Train No: 16160 / 16159   Chennai Egmore - Villupuram",
            "Salem Express"      :    "Train No: 16128 / 16127   Chennai Egmore - Salem", 
           

        }
        for routes in exp_routes.items():
            print(routes)
        

        print("-------------------------------------------------------------------------------------------------------")

        exp_start = input("Enter the Current Stop : ").lower()
        exp_end =   input("Enter the Destination : ").lower()
        exp_coach = input("Enter the coach (Sleeper / general) : ")
        print("Wait !!!  We can check  Availability.......")
        print("Availability is here .......")
        if(exp_coach == "sleeper" or exp_coach == "general"):
            exp_user_name = input("Enter your name : ").lower()
            exp_train_start = input("Enter the Current stop : ").lower()
            exp_train_end =  input("Enter the  destination : ").lower()
            exp_frequently = "Daily"
            exp_train_no = int(input("Enter the Train Number Properly : "))
            if(exp_train_no != ""):
                exp_adult = int(input("How Many Adults : "))
                exp_child = int(input("How Many Childs : "))
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

                #Ticket Process and Price  

                if(exp_start == "madurai" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "madurai" and exp_coach=="sleeper"):
                    exp_train_price_adult= 500
                    exp_train_price_child = 250
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "madurai" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "madurai" and exp_coach=="general"):
                    exp_train_price_adult= 250
                    exp_train_price_child = 100
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "coimbatore" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "coimbatore" and exp_coach=="sleeper"):
                    exp_train_price_adult= 600
                    exp_train_price_child = 300
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "coimbatore" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "coimbatore" and exp_coach=="general"):
                    exp_train_price_adult= 300
                    exp_train_price_child = 150
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "tirunelveli" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "tirunelveli" and exp_coach=="sleeper"):
                    exp_train_price_adult= 650
                    exp_train_price_child = 350
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "tirunelveli" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "tirunelveli" and exp_coach=="general"):
                    exp_train_price_adult= 350
                    exp_train_price_child = 200
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()
                elif(exp_start == "nagercoil" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "nagercoil" and exp_coach=="sleeper"):
                    exp_train_price_adult= 300
                    exp_train_price_child = 150
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "nagercoil" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "nagercoil" and exp_coach=="general"):
                    exp_train_price_adult= 150
                    exp_train_price_child = 100
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()
                    
                elif(exp_start == "karaikkudi" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "karaikkudi" and exp_coach=="sleeper"):
                    exp_train_price_adult= 350
                    exp_train_price_child = 250
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "karaikkudi" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "karaikkudi" and exp_coach=="general"):
                    exp_train_price_adult= 120
                    exp_train_price_child = 80
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "rameswaram" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "rameswaram" and exp_coach=="sleeper"):
                    exp_train_price_adult= 800
                    exp_train_price_child = 650
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "rameswaram" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "rameswaram" and exp_coach=="general"):
                    exp_train_price_adult= 350
                    exp_train_price_child = 200
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()
                elif(exp_start == "tiruchirappalli" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "tiruchirappalli" and exp_coach=="sleeper"):
                    exp_train_price_adult= 550
                    exp_train_price_child = 250
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "tiruchirappalli" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "tiruchirappalli" and exp_coach=="general"):
                    exp_train_price_adult= 200
                    exp_train_price_child = 100
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "thoothukudi" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "thoothukudi" and exp_coach=="sleeper"):
                    exp_train_price_adult= 700
                    exp_train_price_child = 450
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "thoothukudi" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "thoothukudi" and exp_coach=="general"):
                    exp_train_price_adult= 300
                    exp_train_price_child = 150
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "villupuram" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "villupuram" and exp_coach=="sleeper"):
                    exp_train_price_adult= 350
                    exp_train_price_child = 150
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "villupuram" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "villupuram" and exp_coach=="general"):
                    exp_train_price_adult= 70
                    exp_train_price_child = 40
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "salem" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "salem" and exp_coach=="sleeper"):
                    exp_train_price_adult= 400
                    exp_train_price_child = 200
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                elif(exp_start == "salem" and exp_end == "chennai egmore" or exp_start == "chennai egmore" and exp_end == "salem" and exp_coach=="general"):
                    exp_train_price_adult= 200
                    exp_train_price_child = 100
                    trains = Express_trains(exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach)
                    trains.ticket()

                
                
                else:
                    print("Sorry , Your Train is not available at the moment !!!" )
               
            else:
                print("Invaild Train Number Please Check it given above !!!")
        else:
            print("Invalid Coach Please re-check it !!!")

        #----------------------Express trains ended---------------------------  

    elif(check_trains == "superfast trains" or check_trains == "3"):
        print("----------------------------------------------------------------------------------------")
        sup_trains_lists = {
            "Tamil Nadu Express" : "Train No: 12621 / 12622  Chennai Central - New Delhi",
            "Kerala Express" :     "Train No: 12625 / 12626  Thiruvananthapuram - New Delhi",
            "Mumbai Rajdhani Express": "Train No: 12951 / 12952 Mumbai Central - New Delhi",
            "Howrah Mail" : "Train No: 12839 / 12840  Chennai Central- Howrah Junction",
            "Gujarat Superfast Express" : "Train No: 22953 / 22954  Mumbai Central - Ahmedabad Junction",
            "Karnataka Express" : "Train No: 12627 / 12628  Bengaluru - New Delhi",
            "Andhra Pradesh Express" : "Train No: 12723 / 12724  Tirupathi - New Delhi",
            "Shatabdi Express" : "Train No: 12243 / 12244  Chennai Central - Coimbatore Junction",
            "Telangana Express" : "Train No: 12723 / 12724  Hyderabad - New Delhi",
            "Ganga Kaveri Express" : "Train No: 12669 / 12670  Chennai Central - kashmir "

        }
        for superfast in sup_trains_lists.items():
            print(superfast)
        print("----------------------------------------------------------------------------------------")



        print("------------------------SUPERFAST EXPRESS TRAINS TYPES----------------------------------")
        print("1. General Coach           2. Sleeper Coach")  
        print("3. AC TIER - 1             4. AC TIER - 2  ")
        print("              5. AC TIER - 3               ")
        print("-----------------------------------------------------------------------------")
        sup_coach = input("Enter the Coach What you like (1 - 5) : ")
        if(sup_coach == "1" or sup_coach == "2"):
            coachs =Second_coach()
            coachs.second_class() 
        elif(sup_coach == "3" or sup_coach == "4" or sup_coach == "5" or sup_coach == 6):
            accoachs = Ac_coachs()
            accoachs.ac_class()
        else:
            print("Please Enter vaild Number !!!!")




    else:
        print("Ivalid data entered. Please Re-check .......")

   
        
        

    



