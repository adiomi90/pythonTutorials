# numbers = [1, 2]
# print(numbers[1])
# particles 
try:
    open("exception.py")
    age = int(input("Enter your age: "))
    age = 10 / age    
    print(age)
   
except (ValueError,ZeroDivisionError)  as ex:
    print("You didnt enter a value age")
    print(ex)
    print(type(ex))
else:
    print("No errors")
finally:
    file.close()
print("no errors")