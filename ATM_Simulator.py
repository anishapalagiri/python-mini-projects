balance=1000
while True:
    print("\n1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Balance:",balance)
    elif choice==2:
        amount=int(input("Enter deposit amount:"))
        balance+=amount
        print("Amount Deposited Successfully!")
    elif choice==3:
        amount=int(input("Enter withdraw amount:"))
        if amount<=balance:
            balance-=amount
            print("Amount Withdraw Successfully!")
        else:print("Insufficient Balance!")
    elif choice==4:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")

        






