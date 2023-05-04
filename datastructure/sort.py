numbers = [3, 34, 233, 55, 43, 54]
# numbers.sort(reverse=True)
print(numbers)

#returns a new list
print(sorted(numbers, reverse=True))

items = [
    ("product10", 100),
    ("product20", 120),
    ("product30", 7),
]

# def sort_item(item):
#     return item[1]


items.sort(key = lambda item:item[1])
print(items)
