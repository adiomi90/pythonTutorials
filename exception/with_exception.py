#no need for finally clause 
#auto release resources

try:
    with open("exception.py") as file:
        print("File opened")
    age =  int(input("Enter your age:"))
    age = 10/ age
    print(age) 
except (ValueError,ZeroDivisionError):
    print("Enter a valid number")
else:
    print("no errors")
finally:
    file.close()