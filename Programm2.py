price = 0
discount = 10
ticket = input("Введите количество билетов:")
for i in range(int(ticket)):
    age = int(input("Введите возраст посетителей:"))
    if 0 <= int(age) <= 17:
        price += 0
    elif 18 <= int(age) <= 24:
        price += 990
    elif int(age) >= 25:
        price += 1390
if int(ticket) < 3:
    print("Итого", price)
elif int(ticket) > 3:
    price = price - (price * discount / 100)
    print("Итого:", price)
