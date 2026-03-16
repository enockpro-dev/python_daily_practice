print("==== Welcome to  ATM ====")

balance = 1000

while True:
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        deposit = float(input("Enter amount to deposit: "))
        balance = balance + deposit
        print("Money deposited successfully")

    elif choice == "3":
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw > balance:
            print("Insufficient balance")
        else:
            receipt_choice = input("Do you want a receipt? (y/n): ")
            balance = balance - withdraw
            print("Please take your money")
            if receipt_choice.lower() == 'y':
                print("Receipt:")
                print(".......................")
                print(f"Transaction: Withdrawal of ${withdraw}")
                print(f"New balance: ${balance}")
                print("THANK YOU FOR USING OUR ATM")
                print("Please take your card")
                break
            else:
                print("Thank you for using our ATM")
                print("\nPlease take your card")
                break

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid option")