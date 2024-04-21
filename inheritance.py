#base Class / Parent class
class Person:
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
    def __repr__(self) -> str:
        return f"{self.name},{self.email},{self.phone}"
        
class Employee(Person):
    def __init__(self, name, email, phone,working_tech,num_of_project,salary,join_date):
        self.working_tech = working_tech
        self.num_of_project = num_of_project
        self.salary = salary
        self.join_date = join_date
        super().__init__(name, email, phone)

    def __repr__(self) -> str:
        print(self.salary)
        return super().__repr__()

    def web_dev(self,use_theme,plugin_name):
        print(f"using theme : {use_theme} & using plugin : {plugin_name}")

    def sof_engi(self,using_theme):
        print (f"using theme : {using_theme}")


class Customer(Person):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)

    def __repr__(self) -> str:
        return super().__repr__()
    
    def project(self):
       print("hello")


customer1 = Customer("A",'deom@gmail.com','001201')
# print(customer1.name,customer1.email,customer1.phone)
# customer1.project()

employee1 = Employee("Sohel","employee@gmail.com","01453431","Python",10,200000,'10 Dec')

# print(employee1.name,employee1.email,employee1.phone,employee1.working_tech,employee1.num_of_project,employee1.salary,employee1.join_date)

# employee1.sof_engi("some one")

print(customer1)
print(employee1)