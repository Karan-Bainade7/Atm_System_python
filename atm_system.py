def main():
    pinCode = ["1234", "1122", "2323", "1985", "5555"]
    accountHoldersName = ["karan", "prajwal", "sanket", "kiran", "sachin"]
    accountNumber = ['1353', '199281', "182838", "185597", "667432"]
    balance = [567000, 21873, 2341871, 275638, 91820]

    flag = False
    for i in range (0,999999999): 
        print("""
    \t\t=== Welcome to ATM System ===
""")
        inputName = input("Enter Your Name: ")
        inputName = inputName.lower()
        inputPin = 0000 
        index = 0 
        for name in accountHoldersName:
            count = 0
            if name == inputName:
                index = count 
                inputPin = input("\nEnter Pin Number: ")
            count += 1

        if inputPin == pinCode[index]:
            flag = True
        else:
            print("Invalid data.")
            flag = False
            continue
        if flag == True:
            print("\nYour account number is: ",accountNumber[index])
            print("Your account balance is: Rs.", balance[index])
            drawOrDeposite = input("\nDo you want to draw or deposit cash (draw/deposite/no): ")
            if drawOrDeposite == "draw":
                amount = input("\nEnter the amount you want to draw: ")
                try: 
                    amount = int(amount)
                    if amount > balance[index]:
                        raise
                except:
                    print("invalid amount.")
                    continue
                remainingBalalnce = balance[index] - amount 
                balance.remove(balance[index])  
                balance.insert(index,remainingBalalnce)
                availableBalance = print("\nYour available balance is: ",remainingBalalnce)
            elif drawOrDeposite == "deposite":
                amount = input("Enter the amount you want to deposite: ")
                try:
                    amount = int(amount)
                    if amount > balance[index]:
                        raise
                except:
                    print("invalid amount.")
                    continue
                remainingBalalnce = balance[index] + amount 
                balance.remove(balance[index])
                balance.insert(index,remainingBalalnce)
                availableBalance = print("Your available balance is: ",remainingBalalnce)
            print("\n\nThank you for using this ATM System. \n  Brought To You By karan bainade")

main()




