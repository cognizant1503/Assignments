#DSA-Assgn-302
from res.DataStructures import *

def queue_ordering(input_queue,input_stack):
    #Do not modify the size of output_queue
    output_queue=Queue(input_queue.get_max_size())
    alph=[]
    #Write your code here
    while not input_queue.is_empty():
        ele=input_queue.dequeue()
        alph.append(ele)
    
    while not input_stack.is_empty():
        pop1=input_stack.pop()
        if(pop1==1):
            alph=list(alph[1:])+list(alph[0])
        if(pop1==2):
            alph=list(alph[-1])+list(alph[:-1])
       
    for i in alph:
        output_queue.enqueue(i)    
    
    return output_queue

#You may modify the below code for testing
input_stack=Stack(5)
input_stack.push(1)
# input_stack.push(2)
input_stack.push(1)
input_stack.push(1)
# input_stack.push(1)

input_queue=Queue(5)
input_queue.enqueue('x')
input_queue.enqueue('y')
input_queue.enqueue('z')
input_queue.enqueue('o')
input_queue.enqueue('t')
output_queue=queue_ordering(input_queue, input_stack)
output_queue.display()