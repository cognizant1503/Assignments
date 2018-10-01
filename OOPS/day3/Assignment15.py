#OOPR-Assgn-15
#Start writing your code here
class Parrot:
    __counter=0
    def __init__(self,name,color):
        self.__color=color
        self.__name=name
        Parrot.__counter+=1
        self.__unique_number=Parrot.__counter
        
        
                    
    def get_unique_number(self):
        return self.__unique_number   
    def get_color(self):
        return self.__color
    def get_name(self):
        return self.__name
    