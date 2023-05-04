items  = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 13),
]

print(items)

prices = []
for price in items:
    prices.append(price[1])

print(prices)

print("-------------------------------------")

x = list(map(lambda item:item[0], items))
print(x)

x = list(filter(lambda item:item[1] >= 10, items))
print(x)