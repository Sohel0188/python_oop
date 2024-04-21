class Vehicle : 
    def __init__(self,name,model,price) -> None:
        self.name = name
        self.model = model
        self.price = price
    def move(self):
        pass
    def __repr__(self) -> str:
        return f"{self.name},{self.model},{self.price}"
class Bus(Vehicle):
    def __init__(self, name, model, price,seat) -> None:
        self.seat = seat
        super().__init__(name, model, price)

    def __repr__(self) -> str:
        print(self.seat)
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self, name, model, price,weidgh) -> None:
        self.weight = weidgh
        super().__init__(name, model, price)

class ACBus(Bus):
    def __init__(self, name, model, price, seat,temperature) -> None:
        self.temperature = temperature
        super().__init__(name, model, price, seat)
    
    def __repr__(self) -> str:
        print(f"{self.temperature}")
        return super().__repr__()

new_bus = ACBus("new AC bus","ae55",200000,20,22)
print(new_bus)