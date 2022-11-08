

class Student:
    def __init__(self, name: str):
        self.name = name

    def lern(self):
        print(f'{self.name} is learning')
        return True
    
    def get_my_name(self):
        return self.name

students = (Student('Bob'), Student('John'), Student('Tom'))

def GetStudent(student_name: str):
    for student in students:
        if student_name == student.name:
            return student

def GetMultipleStudents():
    ret_val = []
    for name in ['Bob', 'John', 'Tom']:
        ret_val.append(GetStudent(name).get_my_name())
    return ret_val
        

def main() -> None:
    print(f'Hello main from : {__file__}')
    GetStudent('Bob').lern()


if __name__ == '__main__':
    main()

