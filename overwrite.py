class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print('vat mangso polau korma')
    
    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):

    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):
        print('Heath maintaing korte hove')

    def exercise(self):
        print('Regular gym korte hobe')
    
    def __add__(self,other):
        return self.age + other.age
    def __mul__(self,other):
        return self.height * other.height

mas = Cricketer('masrifi',38,5.10,70,"banglasesh")
tamim = Cricketer('Tamim',40,5.10,80,"banglasesh")
mas.eat()
mas.exercise()

#oprator overload
print(40 + 60)
print('sakik' + " rakib")
print([10,30,15]+[50,84,54,45])
print(mas + tamim)
print(mas * tamim)