balance = 1000
choice = input("1.пополнить баланс\n 2. снять деньги\n 3.выйти")

if choice == 1:
  amount = float(input("сколько внести?"))
  if amount > 0:
      balance += amount
      print(balance)
   else:
      print("так нельзя")
elif choice == "2":
    amount = float(input("сколько снять?"))
   if amount > 0:
       balance -= amount
       print("balance")
   else:
       print("так нельзя")
elif choice == "3"
       print("пока")
