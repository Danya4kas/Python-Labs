num1 =float(input("Введіть перше число:"))
operation =(input("Введіть операцію: (+, -, *, /):"))
num2 = float(input("Введіть друге число:"))

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1+ num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 !=0:
        result = num1 / num2
    else:
        print ("Error: Ділити на 0 неможливо")
        exit() 
else:
    print("Помилка: Невідома операція")
    exit()

print("Результат:", result)


