#DSA-Assgn-7

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from day2.DataStructures import LinkedList

def remove_duplicates(duplicate_list):
    #write your logic here
    start=duplicate_list.get_head()
    next_node=start.get_next()
    while(next_node!=None):
        if(start.get_data()==next_node.get_data()):
            duplicate_list.delete(start.get_data())
            start=next_node
            next_node=next_node.get_next()
        else:
            start=next_node
            next_node=next_node.get_next()
     
    return duplicate_list

#Add different values to the linked list and test your program
duplicate_list=LinkedList()
duplicate_list.add(30)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)

remove_duplicates(duplicate_list)