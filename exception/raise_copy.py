from timeit import timeit

code1 = """ 
def calcualte_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be or o less.")
    return 10 / age 



try:
    calcualte_xfactor(-1)
except ValueError as error:
    print(error) """

code2 = """ 
def calcualte_xfactor(age):
    if age <= 0:
        return None
    return 10 / age 




  xfactor =   calcualte_xfactor(-1)
  if xfactor == None:
  pass
"""
    
    
print("first code ", timeit(code1 , number =10000))