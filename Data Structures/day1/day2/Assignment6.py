#DSA-Assgn-6

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from day2.DataStructures import LinkedList

class Child:
    def __init__(self,name,item_to_perform):
        self.__name=name
        self.__item_to_perform=item_to_perform

    def __str__(self):
        return(self.__name+" "+self.__item_to_perform)

    def get_name(self):
        return self.__name

    def get_item_to_perform(self):
        return self.__item_to_perform

class Performance:
    def __init__(self,children_list):
        self.__children_list=children_list

    def get_children_list(self):
        return self.__children_list

    def change_position(self,child):
        '''Finding the length of Linkedlist'''
        temp=self.__children_list.get_head()
        length=0
        while temp!=None:
            length+=1
            temp=temp.get_next()
        
        '''Removing the child and inserting it in the Middle'''   
        temp=self.__children_list.get_head()
        count=0
        while temp!=None:
            if(count==length//2):
                '''Node after which we want to insert the New Node'''
                data1=temp  
                self.__children_list.delete(child)
                break
            count+=1
            temp=temp.get_next()
        
        self.__children_list.insert(child,data1.get_data())
        
          
    def add_new_child(self,child):
        self.__children_list.add(child)
    

#Implement Performance class here
child1=Child("Rahul","solo song")
child2=Child("Sheema","Dance")
child3=Child("Gitu","Plays Flute")
child4=Child("Tarun","Gymnastics")
child5=Child("Tom","MIME")

#Add different values to the list and test the program
children_list=LinkedList()
children_list.add(child1)
children_list.add(child2)
children_list.add(child3)
children_list.add(child4)
children_list.add(child5)
performance=Performance(children_list)
print("The order in which the children would perform:")
performance.get_children_list().display()
print()
print("After Rahul's performance, the schedule would change to:")
performance.change_position(child1)
performance.get_children_list().display()
print()
child6=Child("Swetha","Vote of Thanks")
print("After Swetha has joined, the schedule is:")
performance.add_new_child(child6)
performance.get_children_list().display()