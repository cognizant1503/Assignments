#OOPR-Assgn-9
#Implement Student class here
class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
        self.__course_id=[1001,1002]
        self.__fees=[25575.0,15500.0]
        
    def set_student_id(self,student_id):
        self.__student_id=student_id
    def set_marks(self,marks):
        self.__marks=marks
    def set_age(self,age):
        self.__age=age
        
    def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    def get_course_id(self):
        return self.__course_id
    def get_fees(self):
        return self.__fees
        
    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return True
        else:
            return False
    def validate_age(self):
        if(self.__age>20):
            return True
        else:
            return False
    
    def check_qualification(self):
        if(self.validate_age() and self.validate_marks() and self.__marks>=65):
            return True
        else:
            return False
    def choose_course(self,course_id):
        if((course_id in self.__course_id) and self.check_qualification()):
            if(self.__marks>85):
                self.__fees=0.75*self.__fees[self.__course_id.index(course_id)]
            else:
                self.__fees=self.__fees[self.__course_id.index(course_id)]
            self.__course_id=course_id
            return True
        else:
            self.__fees=None
            self.__course_id=None
            return False        
         
