drinks = [["Pepsi", 3], ["Coca-Cola", 2], ["Mineral Water", 1], ["Gatorade", 5]]
notes = [100, 50, 20, 10, 5, 1]

for index, drink in enumerate(drinks):
    print(f"[{index}] {drink[0]} (RM {drink[1]})")
print(f"Choose your drink based on code (0 for {drinks[0][0]}, etc.): ")

while True:
    try:
        input_drink = int(input())
    except ValueError:
        print(f"Enter only the code (1 for {drinks[1][0]}, etc.):")
        continue
    else:
        if input_drink >= 0 and input_drink < len(drinks):
            break
        else:
            print(f"No drinks for the provided code. Enter the correct one:")
            continue

while True:
    try:
        input_money = int(input("Insert your money(RM): "))
    except ValueError:
        print(f"Enter only the amount (100, 50, 3, 2):")
        continue
    else:
        price = drinks[input_drink][1]
        if input_money >= price:
            balance = input_money - price

            change = {}
            for note in notes:
                if balance >= note:
                    change[note] = balance//note # Getting number of notes by dividing the balance
                    balance = balance % note # Update balance 

            print("Your balance:")
            for key in change.keys():
                print(f"RM {key} x {change[key]}")
        else:
            print("Sorry you don't have enough money.")
        break