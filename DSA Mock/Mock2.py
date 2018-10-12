#OOP-Assgn-202
#Do Not Change any part of the code provided to you
from abc import ABCMeta, abstractmethod
class CustomerDetails:
    customer_points_details = {'R1001':892, 'R1002':956, 'R1003':1352}
    mem_card_types = ['Silver','Gold','Platinum']
    card_type_points = [2,4,5]

    #To Trainee
    @staticmethod
    def get_card_points(card_type):
        type1=['silver','gold','platinum']
        if(card_type.lower() in type1):
            index=type1.index(card_type.lower())
            return CustomerDetails.card_type_points[index]
        return -1
    #To Trainee
    @staticmethod
    def add_point(cust_id,points):
        
        if(cust_id.upper() in CustomerDetails.customer_points_details.keys()):
            CustomerDetails.customer_points_details[cust_id.upper()]+=points
        else:
            CustomerDetails.customer_points_details.update({cust_id.upper():points})
            

    #To Trainee
    @staticmethod
    def redeem_points(cust_id):
        if(cust_id.upper() in CustomerDetails.customer_points_details.keys()):
            val=0
            point=CustomerDetails.customer_points_details[cust_id.upper()]
            if(point>1500):
                val=(point-1500)*75/100
                CustomerDetails.customer_points_details[cust_id.upper()]=1500
            return val   
        return 0
            
            
class Customer(metaclass = ABCMeta):
    def __init__(self,cust_id,cust_name):
        self.__cust_id = cust_id
        self.__cust_name = cust_name

    def get_cust_id(self):
        return self.__cust_id

    def get_cust_name(self):
        return self.__cust_name

    @abstractmethod
    def validate_cust_details(self):
        pass


class RegisteredCustomer(Customer):
    def __init__(self,cust_id,cust_name,mem_card_type):
        super().__init__(cust_id, cust_name)
        self.__mem_card_type = mem_card_type

    def get_mem_card_type(self):
        return self.__mem_card_type

    #To Trainee
    def validate_cust_details(self):
        name=self.get_cust_name()
        type1=self.__mem_card_type
        id1=self.get_cust_id()
        if(name is not None and 
           type1 is not None and 
           id1 is not None):
            return True
        return False

class Bill:
    __counter = 5001
    def __init__(self,customer,redeemption_required):
        self.__customer = customer
        self.__redeemption_required = redeemption_required
        self.__bill_num = None

    def get_customer(self):
        return self.__customer

    def get_redeemption_required(self):
        return self.__redeemption_required

    def get_bill_num(self):
        return self.__bill_num

    #To Trainee
    def generate_bill_num(self):
        self.__bill_num=Bill.__counter
        Bill.__counter+=1

    #To Trainee
    def calculate_points(self,bill_amount):
        type1=self.__customer.get_mem_card_type()
        get_points=CustomerDetails.get_card_points(type1)
        if(get_points==-1):
            return -1
        points=bill_amount*get_points//100
        return points

    #To Trainee
    def calculate_final_bill_amount(self,bill_amount):
        if(bill_amount>100 and self.__customer.validate_cust_details()):
            points=self.calculate_points(bill_amount)
            if(points==-1):
                final_bill_amount=-1
                self.__bill_num=-1
            else:
                id1=self.__customer.get_cust_id()
                CustomerDetails.add_point(id1, points)
                self.generate_bill_num()
                if(self.get_redeemption_required()):
                    val=CustomerDetails.redeem_points(id1)
                    final_bill_amount=bill_amount-val
                else:
                    final_bill_amount=bill_amount
        return final_bill_amount


cust_obj = RegisteredCustomer('r1003', 'John', 'GolD')
bill_obj = Bill(cust_obj, True)
final_bill_amount = bill_obj.calculate_final_bill_amount(10000)
print('Bill Num :',bill_obj.get_bill_num())
print('Final Bill Amount :',final_bill_amount)
print(CustomerDetails.customer_points_details)