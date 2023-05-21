from sales.ecommerce import sale
import sys


sale.calc_shipping()
print(sys.path)


print(dir(sale))
print(dir(sale.__doc__))
print("___________________________")
print(dir(sale.__file__))
print("_________________________________")
print(dir(sale.__name__))
print("_____________________________________")
print(sale.__package__)