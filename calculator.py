a = float(input("Первое число: "))
op = input("Действие (+, -, *, /): ")
b = float(input("Второе число: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("На ноль делить нельзя")
else:
    print("Неизвестное действие")