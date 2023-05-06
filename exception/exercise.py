from pprint import pprint
particles = "This is one of the most commont interview questions"
repeat = {}
for char in particles:
    if char in repeat:
        repeat[char] += 1
    else:
        repeat[char] = 1
        

sorted_char = sorted(repeat.items(), key = lambda kv:kv[1],reverse= True)

pprint(sorted_char)
print("character with the most repeat is : ",sorted_char[1])
   

    

