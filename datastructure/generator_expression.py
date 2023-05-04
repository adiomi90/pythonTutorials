from sys import getsizeof

values = [x * 2 for x in range(10)]
for x in values:
    print(x)

values_1 = (x * 2 for x in range(10000))
print("list:", getsizeof(values_1))
