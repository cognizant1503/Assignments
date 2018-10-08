#DSA-Assgn-13

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from res.DataStructures import Stack

def change_smallest_value(number_stack):
    #write your logic here
    lst=[]
    
    while not number_stack.is_empty():
        lst.append(number_stack.pop())
    least=min(lst)
    count1=lst.count(least)
    for i in range(0,count1):
        number_stack.push(least)
        lst.remove(least)
        
    for i in lst[::-1]:
        number_stack.push(i)

    return number_stack

#Add different values to the stack and test your program
number_stack=Stack(8)
number_stack.push(7)
number_stack.push(8)
number_stack.push(5)
number_stack.push(66)
number_stack.push(5)
print("Initial Stack:")
number_stack.display()
change_smallest_value(number_stack)
print("After the change:")
number_stack.display()