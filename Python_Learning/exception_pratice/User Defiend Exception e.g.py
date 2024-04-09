class Atm_balance(Exception):
    pass
class Atm_account(Exception):
    pass

acc=100
atm=1000
w=int(input("Enter the money to withdraw: "))
if w>0:
    if w<acc and w< atm:
        print("Thank You Withdrawl is successful")
    elif w>atm:
        raise Atm_balance('Low balance in ATM')
    elif w>acc:
        raise Atm_account('Low balance in account')
    else:
        print("ATM is not working")

else:
    print('Invalid Input')