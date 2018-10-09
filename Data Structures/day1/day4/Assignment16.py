#DSA-Assgn-16

from res.DataStructures import Stack,Queue

def separate_boxes(box_stack):
    #Remove pass and write your logic here
    new_queue=Queue(box_stack.get_max_size())
    lst2=[]
    lst=['Red','Green','Blue']
    while not box_stack.is_empty():
        ele=box_stack.pop()
        if(ele not in lst):
            new_queue.enqueue(ele)
        else:
            lst2.append(ele)
    for i in lst2[::-1]:
        box_stack.push(i)
    return new_queue
            


box_stack=Stack(8)
box_stack.push("Red")
box_stack.push("Magenta")
box_stack.push("Yellow")
box_stack.push("Red")
box_stack.push("Orange")
box_stack.push("Green")
box_stack.push("White")
box_stack.push("Purple")
print("Boxes in the stack:")
box_stack.display()
result=separate_boxes(box_stack)
print()
print("Boxes in the stack after modification:")
box_stack.display()
print("Boxes in the queue:")
result.display()