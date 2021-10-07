class ATM:
    def __init__(self, cardnumber, pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def checkbalance(self):
        print("Your balance is: $"+str(500))
    
    def withdraw(self,amount):
        currentamount=500-amount
        print("You have withdrawn "+str(amount)+"Your remaining balance is:"+str(currentamount))
    
def main():
    cardnumber=input("Enter your card number.")
    pin=input("Enter your pin.")
    newuser=ATM(cardnumber,pin)
    print("Choose your activity: 1. Balance 2. Withdraw")
    activity=int(input("Enter your request."))

    if(activity==1):
        newuser.checkbalance()
    elif(activity==2):
        amount=int(input("Enter amount"))
        newuser.withdraw(amount)
    else:
        print("Enter a valid number")

main()