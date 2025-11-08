def train_price(start,end,adult=0,child=0):
    if(start == "chennai beach" and end=="tambaram" or start == "tambaram" and end == "chennai beach"):
        total =  adult * 10 + child *5
    elif(start == "tambaram" and end == "chengalpattu" or start == "chengalpattu" and end == "tambaram"):
        total = adult * 15 + child *5
    elif(start == "chennai beach" and end == "chengalpattu" or start == "chengalpattu" and end == "chennai beach"):
        total = adult * 20 + child *10
    elif(start == "kodabakkam"  and end == "chengalpattu"):
        total = adult *15 + child *10
    elif(end == "kodabakkam"  and start == "chengalpattu"):
        total = adult * 15 + child *10
    elif(start == "kodabakkam" and end == "tambaram"):
        total = adult *5 + child *5
    elif(end == "kodabakkam" and start == "tambaram"):
        total = adult * 5 + child *5
    elif(start == "guindy" and end=="chengalpattu"  or start=="chengalpattu" and end=="guindy"):
        total = adult * 10 + child * 5 
    elif (start == "perungalathur" and end == "chengalpattu" or start=="chengalpattu" and end=="Perungalathur"):
        total = adult * 5 + child * 5
    elif(start != "" and end !=""  or start !="" and end !=""):
        total = adult * 5 + child  * 2
    else:
        print("Please enter vaild Station name ")
    return total
    

def ticket(adult,child, cash_methods,start,destination):
    total_price = train_price(start,destination,adult,child)
    print("---------------------------WELCOME TO INDIAN RAILWAYS-----------------------------")
    print(f"Adult : {adult}")
    print(f"Child : {child}")
    print(f"Mode Of Pay : {cash_methods}")
    print(f"Start : {start}")
    print(f"Destination : {destination}")
    print(f"Total Price :  ₹{total_price}")
    print("This ticket only Allow to travel within 1 hour .....")
    print("------------------------Thank You Happy Journey !!!!!--------------------------------")
    return ticket

    