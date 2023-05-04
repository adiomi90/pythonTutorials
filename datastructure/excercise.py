from pprint import pprint

sentence = "This is a very common interview question"

repeat = {}
for char in sentence:
    if char in repeat:
        repeat[char] += 1
    else:
        repeat[char] = 1
sorted_repeat=sorted(repeat.items(),key = lambda  kv:kv[1],reverse = True)
pprint(sorted_repeat)
print("The letter with most repeat",sorted_repeat[1])
