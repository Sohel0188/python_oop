class Pen:
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price
    def exam(self,num1,num2):
        sum = num1 + num2
        return sum
    

my_pen = Pen('marator','balck',10)
print(my_pen.brand,my_pen.color,my_pen.price)

my_pen2 = Pen("Hi school",'Red',5)
print(my_pen2.brand,my_pen2.color,my_pen2.price)

my_pen3 = Pen('Good Luck','Black',10)
print(my_pen3.brand,my_pen3.color,my_pen3.price)