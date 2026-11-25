balance = 1000

while True:
    choice = input(f"\nБаланс: {balance}\n1. Пополнить баланс\n2. Снять деньги\n3. Выйти\nВыберите: ")

    if choice == "1":
        amount = float(input("Сколько внести? "))
        if amount > 0:
            balance += amount
            print(balance)
        else:
            print("Так нельзя")
    elif choice == "2":
        amount = float(input("Сколько снять? "))
        if 0 < amount <= balance:
            balance -= amount
            print(balance)
        else:
            print("Так нельзя")
    elif choice == "3":
        print("Пока")
        break
    else:
        print("Неверный выбор")