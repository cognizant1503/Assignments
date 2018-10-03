#OOPR-Exer-13
#Start writing your code here
from abc import abstractmethod,ABCMeta
class DirectToHomeService(metaclass=ABCMeta):
    __counter=101
    def __init__(self,consumer_name):
        self.__consumer_name=consumer_name
        self.__consumer_number=DirectToHomeService.__counter
        DirectToHomeService.__counter+=1

    def get_consumer_name(self):
        return self.__consumer_name
    def get_consumer_number(self):
        return self.__consumer_number
    
    @abstractmethod
    def calculate_monthly_rent(self):
        pass

class BasePackage(DirectToHomeService):
    def __init__(self,consumer_name,base_pack_name,subscription_period):
        super().__init__(consumer_name)
        self.__base_pack_name=base_pack_name
        self.__subscription_period=subscription_period

    def get_base_pack_name(self):
        return self.__base_pack_name


    def get_subscription_period(self):
        return self.__subscription_period

    def validate_base_pack_name(self):
        list1=['Silver','Gold','Platinum']
        if(self.get_base_pack_name() not in list1):
            self.__base_pack_name='Silver'
            return "Base package name is incorrect, set to Silver"
        else:
            return True

    def calculate_monthly_rent(self):
        a=self.__subscription_period
        list1=['Silver','Gold','Platinum']
        list2=[350,440,560]
        monthly_rent=0
        if(a>=1 and a<=24 and self.validate_base_pack_name()):
            index=list1.index(self.__base_pack_name)
            b=list2[index]
            if(a>12):
                monthly_rent=((b*a)-b)/a
            else:
                monthly_rent=(b*a)/a
            return monthly_rent
        else:
            return -1
            
