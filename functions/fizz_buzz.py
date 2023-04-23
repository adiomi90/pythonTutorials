#solve the fix buzz question 
#return fix if divisible by 5
#return buzz if divisbile by 3
#return fixbuzz if divisible by 3 and 5 or return the number 
def fizz_buzz(input):
    if input % 5 == 0 and input % 3 == 0:
        return "fizz_buzz"
    if input % 5 == 0:
        return "fizz"
    if input % 3 == 0:
        return "buzz"
    return input


print(fizz_buzz(15))