class Famaly:
    def __init__(self,address) -> None:
        self.address = address
class School:
    def __init__(self,id,r_class) -> None:
        self.id = id
        self.r_class = r_class

class Sports:
    def __init__(self,game) -> None:
        self.game = game

class Student(Famaly,School,Sports):
    def __init__(self, address,id,level,game) -> None:
        School.__init__(self,id,level)
        Sports.__init__(self,game)
        Famaly.__init__(self.address)

Student1 = Student("no",32132,"one","game_name")
print(Student1.address)