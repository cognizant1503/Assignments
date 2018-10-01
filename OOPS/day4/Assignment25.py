#OOPR-Assgn-25
#Start writing your code here

class FruitInfo:
    __fruit_name_list=['Apple','Guava','Orange','Grape','Sweet Lime']
    __fruit_price_list=[200,80,70,110,60]
    
    @staticmethod
    def get_fruit_price(fruit_name):
        if(fruit_name in FruitInfo.__fruit_name_list):
            index=FruitInfo.__fruit_name_list.index(fruit_name)
            return FruitInfo. __fruit_price_list[index]
        else:
            return -1
        
    
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list
    
class Purchase(FruitInfo):
    __counter=0
    def __init__(self,customer,fruit_name,quantity):
        self.__purchase_id=None
        self.__customer=customer
        self.__fruit_name=fruit_name
        self.__quantity=quantity
        
       
        self.__purchase_id="P"+str(Purchase.__counter)
        Purchase.__counter+=1

    def get_purchase_id(self):
        return self.__purchase_id
    def get_customer(self):
        return self.__customer
    def get_quantity(self):
        return self.__quantity
    
    def calculate_price(self):
        
       
        if(super().get_fruit_price(self.__fruit_name)==-1):
            return -1
        else:
            price=super().get_fruit_price(self.__fruit_name)
            total_price=price*self.__quantity
            if(price==max(super().get_fruit_price_list()) and 
               self.__quantity>1):
                total_price-=total_price*2/100
            elif(price==min(super().get_fruit_price_list()) and 
                 self.__quantity>=5):
                total_price-=total_price*5/100
            if(self.__customer.get_cust_type()=="wholesale"):
                total_price-=total_price*10/100
            return total_price
            
            
            
            
    
class Customer:
    def __init__(self,customer_name,cust_type):
        self.__customer_name=customer_name
        self.__cust_type=cust_type

    def get_customer_name(self):
        return self.__customer_name
    def get_cust_type(self):
        return self.__cust_type

    

    
        