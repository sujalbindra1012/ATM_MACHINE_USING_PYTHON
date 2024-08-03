import time

print("WELCOME TO THE BANK")

print("Please Insert Your Card ")

time.sleep(3)

password = 1234
chances = 3
transaction_history = []
balance = 1000
while (chances != 0):
    pin = int(input("Enter Your Four Digit Pin : "))
    if pin != password:
        chances -= 1
        print("*********************************")
        print("Wrong Pin Number")
        print(f"You Have {chances} chances left")
        print("*********************************")
    else:
        if pin == password:
            print("""
          1 == TRANSACTION HISTORY
          2 == WITHDRAW BALANCE
          3 == DEPOSIT BALANCE
          4 == TRANSFER
          5 == exit
          """
                  )
        try:
            option = int(input("Please Enter Your Choice : "))
        except:
            print("Please Enter Valid Option")

        if option == 1:
            print('-------------------------------------')
            print(f"Your Current Balance is : {balance}")
            print('-----------------------------')
            print("Transaction History :")
            for transaction in transaction_history:
                if transaction['type'] == 'Transfer':
                    print(
                        f"Type: {transaction['type']}, Amount: {transaction['amount']}, Recipient Account: {transaction['recipient_account']}, Date and Time: {transaction['date_time']}")
                else:
                    print(
                        f"Type :{transaction['type']},Amount : {transaction['amount']}, Date and Time: {transaction['date_time']}")
            print("---------------------------------")

        if option == 2:

            withdraw = int(input("Enter Your Withdraw Amount : "))
            print('-----------------------------')
            if balance < withdraw:
                print("Insufficient Balance ....")
                print('-----------------------------')

            else:
                balance = balance - withdraw
                transaction_history.append(
                    {"type": "Withdraw", "amount": withdraw, "date_time": time.strftime("%Y-%m-%d %H:%M:%S")})
                print(f'{withdraw} is debited from your account ')
                print(f"Your Current Balance is : {balance}")
                print('-----------------------------')

        if option == 3:
            deposit = int(input("Enter Your Deposited Amount : "))
            print('-----------------------------')
            balance = balance + deposit
            transaction_history.append(
                {"type": "Deposit", "amount": deposit, "date_time": time.strftime("%Y-%m-%d %H:%M:%S")})
            print(f'{deposit} is credited to your account ')
            print(f"Your Current Balance is : {balance}")
            print('-----------------------------')

        if option == 4:
            transfer = int(input("Enter amount to transfer : "))
            if balance < transfer:
                print("Insufficient Balance ...")
                print("------------------------------------")
            else:
                recipient = input("Enter Recipient Account Number : ")
                balance -= transfer
                transaction_history.append({"type": "Transfer", "amount": transfer,"recipient_account": recipient, "date_time": time.strftime("%Y-%m-%d %H:%M:%S")})
                print(f'{transfer} has been transferred to account {recipient}')
                print(f"Your Current Balance is : {balance}")
                print('-----------------------------')

        if option == 5:

            print("****************************************")
            print("----------------------------------------")
            print("Thank You For Visiting Our Bank ... ")
            print("SEE YOU SOON")
            print("----------------------------------------")
            print("****************************************")

            break
