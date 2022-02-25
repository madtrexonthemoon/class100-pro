class atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def check_balance(self):
        print("your balance is 5000000")
    def withdrawl(self,amount):
        new_amount  = 5000000-amount
def main():
    card_number=input("insert your card number:-")
    pin_number=input("enter your pin number:-")
    new_user=atm(card_number,pin_number)
    print("choose your activty")
    print("1.balance enquriy 2.withdrawl")
    activty= int(input("enter activty number:-"))
    if(activty==1):
        new_user.check_balance()
    elif (activty==2):
        amount= int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valide number")
if __name__=="__main__":
    main()