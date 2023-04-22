""" successful = true
for number in range(1, 4):
    print("Attempt", number, number * "*")
 """

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print ("Attempt failed")
