Balance = 5000

def check_balance():
    print(f"current balance :{Balance}")
    return Balance


def deposite_amount():
    global Balance
    deposite = int(input("Enter a Number :"))
    Balance += deposite
    print(f"current balance after deposite :{Balance}")
    return Balance


def withdrawal_amount():
    global Balance
    withdrawal = int(input("Enter a Number :"))
    if withdrawal > Balance:
        print("Insufficient Funds")
    else:
        Balance -= withdrawal
    print(f"current balance after withdraw :{Balance}")
    return Balance


pin = int(input("Enter a Pin :"))

if pin == 1234:
    while True:
        choice = int(input(
            "Enter a choice \n"
            "1. Check Balance \n"
            "2. Amount_deposite \n"
            "3. Withdrawal \n"
            "4. Exit\n"
        ))

        if choice == 1:
            check_balance()
        elif choice == 2:
            deposite_amount()
        elif choice == 3:
            withdrawal_amount()
        elif choice == 4:
            break
        else:
            print("Invalid choice")
else:
    print("Invalid Pin")