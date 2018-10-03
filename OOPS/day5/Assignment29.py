#OOPR-Assgn-29
#Start writing your code here
from abc import ABCMeta, abstractmethod

class Customer(metaclass=ABCMeta):
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.bill_amount=None
        self.bill_id=None

    def get_customer_name(self):
        return self.__customer_name

    @abstractmethod
    def calculate_bill_amount(self):
        pass
    
class OccasionalCustomer(Customer):
    __counter=1000
    def __init__(self,customer_name,distance_in_kms):
        super().__init__(customer_name)
        OccasionalCustomer.__counter+=1
        self.bill_id='O'+str(OccasionalCustomer.__counter)
        self.__distance_in_kms=distance_in_kms
        Customer.__customer_name=customer_name
        

    def get_distance_in_kms(self):
        return self.__distance_in_kms

    
    def validate_distance_in_kms(self):
        a=self.__distance_in_kms
        if(a>=1 and a<=5):
            return True
        else:
            return False
    def calculate_bill_amount(self):
        self.bill_amount=0
        delivery_charges=0
        distance=self.__distance_in_kms
        if(self.validate_distance_in_kms()):
            if(distance>=1 and distance<=2):
                delivery_charges=5*distance
            elif(distance>2 and distance<=5):
                delivery_charges=7.5*distance
            self.bill_amount=50+delivery_charges
        else:
            self.bill_amount=-1
        return self.bill_amount

class RegularCustomer(Customer):
    __counter=100
    def __init__(self,customer_name,no_of_tiffin):
        super().__init__(customer_name)
        RegularCustomer.__counter+=1
        self.bill_id='R'+str(RegularCustomer.__counter)
        self.__no_of_tiffin=no_of_tiffin
        
    def get_no_of_tiffin(self):
        return self.__no_of_tiffin

    
    def validate_no_of_tiffin(self):
        a=self.get_no_of_tiffin()
        if(a>=1 and a<=7):
            return True
        return False 
    
    def calculate_bill_amount(self):
        if(self.validate_no_of_tiffin()):
            self.bill_amount=self.get_no_of_tiffin()*50*7
        else:
            self.bill_amount=-1
        return self.bill_amount
 
    