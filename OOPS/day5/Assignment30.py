#OOPR-Assgn-30
#Start writing your code here

class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity

    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity
 
    def validate_quantity(self):
        if(self.__quantity>=1 and self.__quantity<=5):
            return True
        return False

class Pizzaservice:
    counter=7000
    def __init__(self,customer,pizza_type,additional_topping):
        self.__service_id=None
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=None

    def get_service_id(self):
        return self.__service_id
    def get_customer(self):
        return self.__customer
    def get_pizza_type(self):
        return self.__pizza_type
    def get_additional_topping(self):
        return self.__addtional_topping
    
    def validate_pizza_type(self):
        list1=['small','medium']
        if(self.__pizza_type.lower() in list1):
            return True
        return False
    def calculate_pizza_cost(self):
        cost=0
        if(self.__customer.validate_quantity() and self.validate_pizza_type()):
            type1=self.__pizza_type.lower()
            topping=self.__additional_topping
            quantity=self.__customer.get_quantity()
            Pizzaservice.counter+=1
            if(type1=='small'):
                if(topping):
                    cost=185*quantity
                else:
                    cost=150*quantity
                self.__service_id='S'+str(Pizzaservice.counter)
            elif(type1=="medium"):
                if(topping):
                    cost=250*quantity
                else:
                    cost=200*quantity
                self.__service_id='M'+str(Pizzaservice.counter)
            self.pizza_cost=cost
            
                
        else:
            self.pizza_cost=-1
        
       
                
                

class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        super().__init__(customer, pizza_type, additional_topping)
        self.__delivery_charge=0
        self.__distance_in_kms=distance_in_kms

    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance_in_kms(self):
        return self.__distance_in_kms

    def validate_distance_in_kms(self):
        distance=self.__distance_in_kms
        if(distance>=1 and distance<=10):
            return True
        return False
    def calculate_pizza_cost(self):
        if(self.validate_distance_in_kms()):
            super().calculate_pizza_cost()
            if(self.pizza_cost!=-1):
                for i in range(1,self.__distance_in_kms+1):
                    if(i>=1 and i<=5):
                        self.__delivery_charge+=5
                    if(i>=6 and i<=10):
                        self.__delivery_charge+=7
                self.pizza_cost+=+self.__delivery_charge
            
        else:
            self.__delivery_charge=-1
            self.pizza_cost=-1
            return False
        
c1=Customer('Asha' , 1)
#Customer(customer_name:Asha , quantity:5),
d1=Pizzaservice(c1,"small",True)
d1.calculate_pizza_cost()
