import random

numbers = [7, 13, 42, 88, 99]

while True:
    choice = input("\n1 - Случайное число\n2 - Выход\nВыберите: ")

    if choice == "1":
        print("\nВыпало:", random.choice(numbers))
    elif choice == "2":
        print("\nВыход...")
        break
    else:
        print("\nНеверный выбор")