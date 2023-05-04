letters = ["a", "b", "c", "d"]
#Add 
letters.append("e")
print(letters)
letters.insert(3, "d")


#remove
letters.remove("a")
print(letters)

letters.pop()
print(letters)

# remove from a range

# del letters[0:3]
# print(letters)

letters.insert(0,"-")
print(letters)

#using range
#del letters[0:3]
#clear
letters.clear()