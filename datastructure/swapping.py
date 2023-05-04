x = 10
y = 11

tem = x
x = y
y = tem

print(x)
print(y)

x, y = y, x
print(x)
print(y)
