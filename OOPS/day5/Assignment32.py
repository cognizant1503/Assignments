#OOPR-Assgn-32
#Start writing your code here
from abc import abstractmethod,ABCMeta

class Employee(metaclass=ABCMeta):
    def __init__(self,job_band,employee_name,basic_salary,qualification):
        self.__job_band=job_band
        self.__employee_name=employee_name
        self.__basic_salary=basic_salary
        self.__qualification=qualification

    def get_job_band(self):
        return self.__job_band
    def get_employee_name(self):
        return self.__employee_name
    def get_basic_salary(self):
        return self.__basic_salary
    def get_qualification(self):
        return self.__qualification
    
    def validate_basic_salary(self):
        if(self.__basic_salary>3000):
            return True
        return False
    
    def validate_qualification(self):
        if(self.__qualification in ["Bachelors","Masters"]):
            return True
        return False
    
    @abstractmethod
    def validate_job_band(self):
        pass
    @abstractmethod
    def calculate_gross_salary(self):
        pass

class Graduate(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,cgpa):
        super().__init__(job_band, employee_name, basic_salary, qualification)
        self.__cgpa=cgpa

    def get_cgpa(self):
        return self.__cgpa
    
    def validate_job_band(self):
        if(self.get_job_band() in ["A", "B" ,"C"]):
            return True
        return False
    
    def calculate_gross_salary(self):
        job=["A", "B" ,"C"]
        incentive=[4,6,10]
        if(self.validate_basic_salary() and
           self.validate_qualification() and
           self.validate_job_band()):
            
            if(self.__cgpa>=4 and self.__cgpa<=4.25):
                tpi=1000
            elif(self.__cgpa>=4.26 and self.__cgpa<=4.5):
                tpi=1700
            elif(self.__cgpa>=4.51 and self.__cgpa<=4.75):
                tpi=3200
            elif(self.__cgpa>=4.76 and self.__cgpa<=5):
                tpi=5000
            index=job.index(self.get_job_band())
            incent=incentive[index]
            pf=self.get_basic_salary()*0.12
            
            gross_salary=pf+tpi+(self.get_basic_salary()*incent/100)+self.get_basic_salary()
            return gross_salary
        else:
            return -1   
            
    
class Lateral(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,skill_set):
        super().__init__(job_band, employee_name, basic_salary, qualification)
        self.__skill_set=skill_set
    
    def get_skill_set(self):
        return self.__skill_set
    
    def validate_job_band(self):
        if(self.get_job_band() in ["D", "E" ,"F"]):
            return True
        return False
    def calculate_gross_salary(self):
        job=["D", "E" ,"F"]
        incentive=[13,16,20]
        if(self.validate_basic_salary() and
           self.validate_qualification() and
           self.validate_job_band()):
            pf=self.get_basic_salary()*0.12
            
            if(self.__skill_set=='AGP'):
                sme=6500   
            elif(self.__skill_set=='AGPT'):
                sme=8200
            elif(self.__skill_set=='AGDEV'):
                sme=11500
                
            index=job.index(self.get_job_band())
            incent=incentive[index]
            
            gross_salary=pf+sme+(self.get_basic_salary()*incent/100)+self.get_basic_salary()
            
            return gross_salary
        else:
            return -1
    
    

    