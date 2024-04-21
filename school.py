class Student:
    def __init__(self,name,current_class,id) -> None:
        self.name = name
        self.current_class = current_class
        self.student_id = id
    def __repr__(self)->str:
        return f'Student with name: {self.name},{self.current_class},{self.student_id}'
class Teacher:
    def __init__(self,name,subject,id) -> None:
        self.name = name
        self.subject = subject
        self.teacher_id = id
    def __repr__(self) -> str:
        return f'Teacher : {self.name},{self.subject},{self.teacher_id}'
    
class School:
    def __init__(self,name,) -> None:
        self.name = name
        self.teachers = []
        self.students = []
    def add_teacher(self,name,subject):
        id = len(self.teachers)+101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)
    
    def enroll(self,name,fee):
        if fee < 6500:
            return 'You Donnot Have Enough Money'
        else:
            id = len(self.students)+1
            student = Student(name,'C',id)
            self.students.append(student)
            return f'{name} is enrolled with id {id}'
    def __repr__(self) -> str:
        print("Welcome To",self.name)

        print('-----------Our Teachers -----------')
        for teacher in self.teachers:
            print(teacher)
        print ("----------Student ----------")
        for student in self.students:
            print(student)
        return 'All Done'

rahim = Student('Abdul rahim', 9, 1)
karim = Teacher('Abdul Karim', 'Algorithm', 101)
print(rahim)
print(karim)  

phitron = School('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('aishwaraiya', 7000)
phitron.enroll('vaijaan', 90000)

phitron.add_teacher('Tom Cruise', 'Algo')
phitron.add_teacher('Decap', 'DS')
phitron.add_teacher('AJ', 'Database')

print(phitron)