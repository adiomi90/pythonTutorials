number = [1, 1, 2, 4]
first = set(number)
second = {1, 5}

#union of the set with |
print(f"The union of set {first | second}") #union of the set 
print(f"The common element of set {first & second}") #common element[]
print(f"not common in both element {first - second}") #not common element
print(f"not in both {first ^ second}") #not in both

#unordered cant be accessed with sequence


if 1 in first:
    print("Yes")
