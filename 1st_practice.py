class Shopping:
    def __init__(self,name) -> None:
        self.name = name
        self.cart = []
    def add_to_cart(self,item,price,quantiry):
       product = {'item':item,'price':price,'quantity':quantiry}
       self.cart.append(product)
        
    def remove_item (self,item):
        
         for value in self.cart:
            i=0
            if value['item'] == item:
                self.cart.remove(value)
            # print(value['item'])
           # print(value['item'])
            
    
    def checkout(self,amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print('Total price',total) 
        if amount<total:
            print(f'Sorry ! Provide {total-amount} Taka More')
        else:
            extra = amount - total
            print(f"Thank You for buying {self.name}\nHere is your change {extra}")
parson = Shopping('Sohel')
parson.add_to_cart('alu',50,5)
parson.add_to_cart('piyaj',50,5)
print(parson.cart)
parson.remove_item('alu')
parson.checkout(1000)
print(parson.cart)
