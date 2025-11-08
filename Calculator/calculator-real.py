while True:
    print("-----------------------Welcome to Calculator------------------------------")
    print("Addition ------------> (+)")
    print("Subraction ----------> (-)")
    print("Multiplication ------> (*)")
    print("Division ------------> (/)")
    
    num1=int(input("Enter the first number : "))
    num2=int(input("Enter the second number : "))
    operator=input("Enter the operation (+,-,*,/): ")
    class Calculate:
        def __init__(self,num1,num2):
            self.num1=num1
            self.num2=num2
        def add(self):
            return(self.num1 + self.num2)
        def sub(self):
            return(self.num1-self.num2)
        def multiply(self):
            return(self.num1*self.num2)
        def div(self):
            try:
                return(self.num1//self.num2)
            except Exception as e:
                return("This number is not divisible")
    obj=Calculate(num1,num2)
    if(operator == '+'):
        print("Total : ",obj.add())
        
    elif(operator=='-'):
        print("Total : ",obj.sub())
        
    elif(operator == "*"):
        print("Total : ",obj.multiply())
        
    elif(operator=="/"):
        print("Total : ",obj.div())
            
    else:
        print("Not a Number")

            
    
    
