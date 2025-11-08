def second_price(sup_start,sup_end,sup_coach):
    if((sup_start == "chennai central" and sup_end == "new delhi" ) or (sup_end == "chennai central" and sup_start == "new delhi") ):
        if sup_coach == "sleeper":
            sup_price_adult = 600
            sup_price_child = 350
            

        elif sup_coach == "general":
            sup_price_adult = 350
            sup_price_child = 250
        else:
            print("Invalid coach type for this route.")
        
        
    elif(sup_start == "thiruvananthapuram" and sup_end == "new delhi" or sup_end == "thiruvananthapuram" and sup_start == "new delhi" ):
        if sup_coach == "sleeper":
            sup_price_adult = 800
            sup_price_child = 350

        elif sup_coach == "general":
            sup_price_adult = 550
            sup_price_child = 250

        else:
            print("Invalid coach type for this route.")

    elif(sup_start == "mumbai central" and sup_end == "new delhi" or sup_end == "mumbai central" and sup_start == "new delhi" ):
        if sup_coach == "sleeper":
            sup_price_adult = 500
            sup_price_child = 250

        elif sup_coach == "general":
            sup_price_adult = 250
            sup_price_child = 100

        else:
            print("Invalid coach type for this route.")
    
    elif(sup_start == "howrah junction" and sup_end == "chennai central" or sup_end == "howrah junction" and sup_start == "chennai central" ):
        if sup_coach == "sleeper":
            sup_price_adult = 800
            sup_price_child = 350

        elif sup_coach == "general":
            sup_price_adult = 550
            sup_price_child = 250

        else:
            print("Invalid coach type for this route.")

    elif(sup_start == "bengaluru" and sup_end == "new delhi" or sup_end == "bengaluru" and sup_start == "new delhi" ):
        if sup_coach == "sleeper":
            sup_price_adult = 800
            sup_price_child = 350

        elif sup_coach == "general":
            sup_price_adult = 550
            sup_price_child = 250

        else:
            print("Invalid coach type for this route.")

    elif(sup_start == "mumbai central" and sup_end == "ahmedabad junction" or sup_end == "mumbai central" and sup_start == "ahmedabad Junction" ):
        if sup_coach == "sleeper":
            sup_price_adult = 400
            sup_price_child = 150

        elif sup_coach == "general":
            sup_price_adult = 200
            sup_price_child = 100

        else:
            print("Invalid coach type for this route.")

    elif(sup_start == "tirupathi" and sup_end == "new delhi" or sup_end == "tirupathi" and sup_start == "new delhi" ):
        if sup_coach == "sleeper":
            sup_price_adult = 800
            sup_price_child = 350

        elif sup_coach == "general":
            sup_price_adult = 350
            sup_price_child = 200

        else:
            print("Invalid coach type for this route.")

    elif(sup_start == "coimbatore junction" and sup_end == "chennai central" or sup_end == "coimbatore junction" and sup_start == "chennai central" ):
        if sup_coach == "sleeper":
            sup_price_adult = 500
            sup_price_child = 150

        elif sup_coach == "general":
            sup_price_adult = 350
            sup_price_child = 100

        else:
            print("Invalid coach type for this route.")

    elif(sup_start == "hyderabad" and sup_end == "new delhi" or sup_end == "hyderabad" and sup_start == "new delhi" ):
        if sup_coach == "sleeper":
            sup_price_adult = 600
            sup_price_child = 350

        elif sup_coach == "general":
            sup_price_adult = 250
            sup_price_child = 100

        else:
            print("Invalid coach type for this route.")

    elif(sup_start == "kashmir" and sup_end == "chennai central" or sup_end == "kashmir" and sup_start == "chennai central" ):
        if sup_coach == "sleeper":
            sup_price_adult = 800
            sup_price_child = 450

        elif sup_coach == "general":
            sup_price_adult = 550
            sup_price_child = 200

        else:
            print("Invalid coach type for this route.")
    


    else:
        print()
    return sup_price_adult,sup_price_child

def ac_price(ac_start,ac_end,ac_coach):
    if((ac_start == "chennai central" and ac_end == "new delhi" ) or (ac_end == "chennai central" and ac_start == "new delhi") ):
        if ac_coach == "ac-tier-1":
            ac_price_adult = 1200
            ac_price_child = 600
            ac_platform = 1

        elif ac_coach == "ac-tier-2":
            ac_price_adult = 1000
            ac_price_child = 500
            ac_platform = 1

        elif ac_coach == "ac-tier-3":
            ac_price_adult = 900
            ac_price_child = 500
            ac_platform = 1

        else:
            print("Invalid coach type for this route.")
        
        
    elif(ac_start == "thiruvananthapuram" and ac_end == "new delhi" or ac_end == "thiruvananthapuram" and ac_start == "new delhi" ):
        if ac_coach == "ac-tier-1":
            ac_price_adult = 1300
            ac_price_child = 600
            ac_platform = 2
            

        elif ac_coach == "ac-tier-2":
            ac_price_adult = 1100
            ac_price_child = 500
            ac_platform = 2

        elif ac_coach == "ac-tier-3":
            ac_price_adult = 1000
            ac_price_child = 500
            ac_platform = 2
        else:
            print("Invalid coach type for this route.")

    elif(ac_start == "mumbai central" and ac_end == "new delhi" or ac_end == "mumbai central" and ac_start == "new delhi" ):
        if ac_coach == "ac-tier-1":
            ac_price_adult = 1000
            ac_price_child = 600
            ac_platform = 3
            

        elif ac_coach == "ac-tier-2":
            ac_price_adult = 800
            ac_price_child = 500
            ac_platform = 3

        elif ac_coach == "ac-tier-3":
            ac_price_adult = 700
            ac_price_child = 500
            ac_platform = 3
        else:
            print("Invalid coach type for this route.")

    
    elif(ac_start == "howrah junction" and ac_end == "chennai central" or ac_end == "howrah junction" and ac_start == "chennai central" ):
        if ac_coach == "ac-tier-1":
            ac_price_adult = 1200
            ac_price_child = 600
            ac_platform = 4
            
            

        elif ac_coach == "ac-tier-2":
            ac_price_adult = 1000
            ac_price_child = 500
            ac_platform = 4

        elif ac_coach == "ac-tier-3":
            ac_price_adult = 900
            ac_price_child = 500
            ac_platform = 4
        else:
            print("Invalid coach type for this route.")


    elif(ac_start == "bengaluru" and ac_end == "new delhi" or ac_end == "bengaluru" and ac_start == "new delhi" ):
        if ac_coach == "ac-tier-1":
            ac_price_adult = 1300
            ac_price_child = 600
            ac_platform = 5
            

        elif ac_coach == "ac-tier-2":
            ac_price_adult = 1200
            ac_price_child = 500
            ac_platform = 5

        elif ac_coach == "ac-tier-3":
            ac_price_adult = 900
            ac_price_child = 500
            ac_platform = 5
        else:
            print("Invalid coach type for this route.")


    elif(ac_start == "mumbai central" and ac_end == "ahmedabad junction" or ac_end == "mumbai central" and ac_start == "ahmedabad Junction" ):
        if ac_coach == "ac-tier-1":
            ac_price_adult = 1200
            ac_price_child = 800
            ac_platform = 6
            

        elif ac_coach == "ac-tier-2":
            ac_price_adult = 1100
            ac_price_child = 500
            ac_platform = 6

        elif ac_coach == "ac-tier-3":
            ac_price_adult = 1000
            ac_price_child = 500
            ac_platform = 6
        else:
            print("Invalid coach type for this route.")


    elif(ac_start == "tirupathi" and ac_end == "new delhi" or ac_end == "tirupathi" and ac_start == "new delhi" ):
        if ac_coach == "ac-tier-1":
            ac_price_adult = 1500
            ac_price_child = 1000
            ac_platform = 7
            

        elif ac_coach == "ac-tier-2":
            ac_price_adult = 1300
            ac_price_child = 800
            ac_platform = 7

        elif ac_coach == "ac-tier-3":
            ac_price_adult = 1200
            ac_price_child = 700
            ac_platform = 7
        else:
            print("Invalid coach type for this route.")


    elif(ac_start == "coimbatore junction" and ac_end == "chennai central" or ac_end == "coimbatore junction" and ac_start == "chennai central" ):
        if ac_coach == "ac-tier-1":
            ac_price_adult = 1200
            ac_price_child = 700
            ac_platform = 8
            

        elif ac_coach == "ac-tier-2":
            ac_price_adult = 1100
            ac_price_child = 600
            ac_platform = 8

        elif ac_coach == "ac-tier-3":
            ac_price_adult = 1000
            ac_price_child = 500
            ac_platform = 8
        else:
            print("Invalid coach type for this route.")


    elif(ac_start == "hyderabad" and ac_end == "new delhi" or ac_end == "hyderabad" and ac_start == "new delhi" ):
        if ac_coach == "ac-tier-1":
            ac_price_adult = 1700
            ac_price_child = 1000
            ac_platform = 9
            

        elif ac_coach == "ac-tier-2":
            ac_price_adult = 1600
            ac_price_child = 900
            ac_platform = 9

        elif ac_coach == "ac-tier-3":
            ac_price_adult = 1300
            ac_price_child = 800
            ac_platform = 9
        else:
            print("Invalid coach type for this route.")


    elif(ac_start == "kashmir" and ac_end == "chennai central" or ac_end == "kashmir" and ac_start == "chennai central" ):
        if ac_coach == "ac-tier-1":
            ac_price_adult = 2500
            ac_price_child = 1300
            ac_platform = 10
            

        elif ac_coach == "ac-tier-2":
            ac_price_adult = 2000
            ac_price_child = 1200
            ac_platform = 10

        elif ac_coach == "ac-tier-3":
            ac_price_adult = 1500
            ac_price_child = 1000
            ac_platform = 10
        else:
            print("Invalid coach type for this route.")

    


    else:
        print()
    return ac_price_adult,ac_price_child,ac_platform

    
        
    