from datetime import datetime


class Express_trains:
    def __init__(self,exp_user_name,exp_train_start,exp_train_end,exp_train_no,exp_adult,exp_child,exp_train_price_adult,exp_train_price_child,cash_methods,exp_frequently,exp_coach):
        self.name = exp_user_name
        self.start = exp_train_start
        self.end = exp_train_end
        self.train_no = exp_train_no
        self.adult = exp_adult
        self.child = exp_child
        self.adult_total = exp_train_price_adult
        self.child_total = exp_train_price_child
        self.cash = cash_methods
        self.daily = exp_frequently
        self.coach = exp_coach
       

  
    def ticket(self):
        times = datetime.now()
        Current_day = times.strftime("%d-%m-%Y")
        Current_time = times.strftime("%H : %M : %S")
        print("-------------------------WELCOME TO INDIAN RAILWAYS---------------------------")
        print(f"Day : {Current_day}")
        print(f"Time : {Current_time}")
        print(f"Name : {self.name}")
        print(f"Train No : {self.train_no}")
        print(f"Start : {self.start}")
        print(f"Destination : {self.end}")
        print(f"Coach : {self.coach}")
        print(f"Frequently : {self.daily}")
        print(f"Adults : {self.adult}")
        print(f"Childs : {self.child}")
        print(f"Total Price : ₹{self.adult_total * self.adult + self.child_total * self.child}")
        print(f"Mode of Pay : {self.cash}")
        print("Note : You must start your Journey within 3 hours !!!!")
        print("--------------------------------THANK YOU HAPPY JOURNEY----------------------------")
    

    