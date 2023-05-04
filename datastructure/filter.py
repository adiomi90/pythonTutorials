items = [
    ("Product1", 10),
    ("Product2", 300),
    ("Product3", 400),
    ("Product3", 2),
]

x = list(filter(lambda item: item[1] > 40, items))

print(x)

# comprehension
filterd = [item[1] for item in items ] 
filter30 = [item for item in items if item[1] > 30]
print(filterd)
print(filter30)
