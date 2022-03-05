per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
deposit = []
print (per_cent['TKB'])
money = int(input("Введите сумму взноса"))
for key in per_cent:
    per_cent[key] = money * per_cent[key]/100
    deposit.append(per_cent[key])
print (deposit)
print (max(deposit))