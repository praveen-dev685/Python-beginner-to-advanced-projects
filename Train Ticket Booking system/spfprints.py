from datetime import datetime
datas = datetime.now()
Current_day = datas.strftime("%d-%m-%Y")
current_time = datas.strftime("%H : %M : %S")


class Second_data:
    def __init__(self,sup_start,sup_end,sup_coach,sup_user_name,sup_train_start,sup_train_end,sup_frequently,sup_train_no,sup_adult,sup_child,cash_methods,gpay_id,sup_price_adult,sup_price_child):
        self.start = sup_start
        self.end = sup_end
        self.coach = sup_coach
        self.name = sup_user_name
        self.train_start  = sup_train_start
        self.train_end = sup_train_end
        self.daily = sup_frequently
        self.train_no = sup_train_no
        self.adult = sup_adult
        self.child = sup_child
        self.adult_price = sup_price_adult
        self.child_price = sup_price_child
        self.cash = cash_methods
        self.pay_mode = gpay_id

        
    def second_prints(self):
        print("------------------------------WELCOME TO INDIAN RAILWAYS----------------------------")
        print(f"Day : {Current_day}")
        print(f"Time : {current_time}")
        print(f"Name : {self.name}")
        print(f"Start : {self.start}")
        print(f"Destination : {self.end}")
        print(f"Coach : {self.coach}")
        print(f"Frequently : {self.daily}")
        print(f"Adults : {self.adult}")
        print(f"Childs : {self.child}")
        print(f"Total Price : {self.adult * self.adult_price + self.child * self.child_price}")
        print(f"Mode of Pay : {self.cash}")
        print(f"UPI id : {self.pay_mode}")
        print("Note : This ticket only vaild 3 hours after your journey was started !!!!")

        print("------------------------------!!!!!! HAPPY JOURNEY INDIAN RAILWAYS !!!!!--------------------")

class Ac_Coach_data:
    def __init__(self,ac_name,ac_start,ac_end,ac_coach,ac_adult,ac_child,ac_adult_price,ac_child_price,ac_platform,cash_methods,gpay_id,slots):
        self.name = ac_name
        self.start = ac_start
        self.end = ac_end
        self.coach = ac_coach
        self.adult = ac_adult
        self.child = ac_child
        self.adult_price = ac_adult_price
        self.child_price =ac_child_price
        self.platform = ac_platform
        self.cash = cash_methods
        self.payment = gpay_id
        self.slots = slots

    def ac_prints(self):
        print("-------------------------------WELCOME TO INDIAN RAILWAYS--------------------------")
        print(f"Current day : {Current_day}")
        print(f"Current time : {current_time}")
        print(f"Name : {self.name}")
        print(f"Start : {self.start}")
        print(f"Destination : {self.end}")
        print(f"Coach : {self.coach}")
        print(f"Adults : {self.adult}")
        print(f"Childs : {self.child}")
        print(f"Total Price : {self.adult * self.adult_price + self.child * self.child_price}")
        print(f"Platform No : {self.platform}")
        print(f"Mode of Pay : {self.cash}")
        print(f"UPI id : {self.payment}")
        print(f"This is your slots number : {self.slots} in {self.coach} coach !!!")
        print("Note : This ticket only vaild  after your journey was started !!!!")

        print("------------------------------!!!!!! HAPPY JOURNEY INDIAN RAILWAYS !!!!!--------------------")


