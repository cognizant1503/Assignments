#DSA-Assgn-8

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from day2.DataStructures import LinkedList


class BakeHouse:
    def __init__(self):
        self.__occupied_table_list=LinkedList()
    def get_occupied_table_list(self):
        return self.__occupied_table_list
    def allocate_table(self):
        pass
    
    def deallocate_table(self,table_number):
        pass
    #Implement other methods here

bakehouse=BakeHouse()
bakehouse.deallocate_table(8)