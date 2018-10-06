#DSA-Assgn-9

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from day2.DataStructures import LinkedList

def reverse_linkedlist(reverse_list):
    
    temp=reverse_list.get_head()
    list1=[]
    while temp!=None:
        list1.append(temp.get_data())
        temp=temp.get_next()
    list1=list1[::-1]
    lld=LinkedList()
    for i in list1:
        lld.add(i)
    reverse_list=lld
        
    #write your logic here
    
    return reverse_list

#Add different values to the linked list and test your program
reverse_list=LinkedList()
reverse_list.add(10)
reverse_list.add(15)
reverse_list.add(14)
reverse_list.add(28)
reverse_list.add(30)
reversed_linkedlist=reverse_linkedlist(reverse_list)
reversed_linkedlist.display()