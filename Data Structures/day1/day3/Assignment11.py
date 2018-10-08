#DSA-Assgn-11

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from res.DataStructures import Queue

def merge_queue(queue1,queue2):
    #write your logic here
    a=queue1.get_max_size()
    b=queue2.get_max_size()
    merged_queue=Queue(a+b)
    lst1=[]
    lst2=[]
    while not queue1.is_empty():
        lst1.append(queue1.dequeue())
    while not queue2.is_empty():
        lst2.append(queue2.dequeue())
    merged=[]
    if(a<b):
        for i in range(0,a):
            merged.append(lst1[i])
            merged.append(lst2[i])
        for i in range(a,b):
            merged.append(lst2[i])
    else:
        for i in range(0,b):
            merged.append(lst1[i])
            merged.append(lst2[i])
        for i in range(b,a):
            merged.append(lst1[i])
    for i in merged:
        merged_queue.enqueue(i)
    
    
    return merged_queue

#Enqueue different values to both the queues and test your program

queue1=Queue(3)
queue2=Queue(6)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')

merged_queue=merge_queue(queue1, queue2)
print("The elements in the merged queue are:")
merged_queue.display()