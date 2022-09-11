

# parent class
class School:
    name = "Meghan Gordon"
    grade = "15"
    email = "meghan.gordon@school.com"
    id_number = "1327"
    
    def getSchool(self):
        entry_name = input("Enter your name: ")
        entry_grade = input("Enter your grade level: ")
        entry_email = input("Enter your email: ")
        entry_id_number = input("Enter your ID number: ")
        if (entry_email == self.email and entry_id_number == self.id_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The student ID or email was incorrect.")
                                

# child class instance
class Teacher(School):
    department = "Science"
    teacher_id = "034"
    salary = "55,000"


    def getSchool(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_teacher_id = input("Enter your ID number: ")
        if (entry_email == self.email and entry_teacher_id == self.teacher_id):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The teacher ID or email was incorrect.")
    


student = School()
student.getSchool()

teacher = Teacher()
teacher.getSchool()
    
