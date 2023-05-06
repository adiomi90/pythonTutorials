#raising exception is not a good practices
def calcualte_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be or o less.")
    return 10 / age 



try:
    calcualte_xfactor(-1)
except ValueError as error:
    print(error)