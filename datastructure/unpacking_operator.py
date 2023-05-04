numbers = [1, 2, 4]
print(*numbers)


value = list(range(5))
print(value)

value_2 = [*range(5)]
print(value_2)

first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)


#using ** for unpacking dictionary
new_one = {"x": 1}
new_two = {"y": 3, "z": 15}
""" combined = {first** , second**, "j": 1}
print(combined)
 """