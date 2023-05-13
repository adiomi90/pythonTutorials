class Product:
    def __init__(self,price):
        self.price = price 
        
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Value cannot be less than 0")
        self.__price = value
        
product = Product(-30)