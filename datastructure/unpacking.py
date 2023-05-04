numbers = [1, 2, 3,4,5,6]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]


# one , two , three = numbers
# print(one, two , three)

# print(first)
# print(second)
# print(third)


first, second , *other = numbers

#unpacking in other

print(f"{first},{second},{other}")