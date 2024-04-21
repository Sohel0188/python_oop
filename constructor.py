class Phone:
    manufectured  = "china"
    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

my_phone = Phone("ami","samsung",5) 
print(my_phone.brand,my_phone.owner,my_phone.price)