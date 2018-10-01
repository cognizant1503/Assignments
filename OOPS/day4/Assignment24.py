#OOPR-Assgn-24
#Start writing your code here

class Apparel:
    counter=100
    def __init__(self,price,item_type):
        self.__price=price
        self.__item_type=item_type
        self.__item_id=''
        Apparel.counter+=1
        if(self.__item_type=="Cotton"):
            self.__item_id='C'+str(Apparel.counter)
        elif(self.__item_type=="Silk"):
            self.__item_id='S'+str(Apparel.counter)
            
    def get_price(self):
        return self.__price
    def get_item_type(self):
        return self.__item_type
    def get_item_id(self):
        return self.__item_id
    
    def set_price(self, price):
        self.__price = price
    def calculate_price(self):
        a=self.get_price()+self.get_price()*5/100
        self.set_price(a)
class Cotton(Apparel):
    def __init__(self,price,discount):
        self.__discount=discount
        super().__init__(price, "Cotton")

    def get_discount(self):
        return self.__discount

    def calculate_price(self):
        super().calculate_price()
        total_price=super().get_price()
        total_price-=total_price*self.__discount/100
        total_price+=total_price*5/100
        super().set_price(total_price)
        
        

class Silk(Apparel):
    def __init__(self,price):
        super().__init__(price, "Silk")
        self.__points=None
    
    def calculate_price(self):
        self.__points=0
        silk_price=super().get_price()
        if(silk_price>10000):
            self.__points+=10
        else:
            self.__points+=3
        super().calculate_price()
        total_price=super().get_price()   
        total_price+=total_price*10/100
        super().set_price(total_price)
    
    def get_points(self):
        return self.__points
    
    
    