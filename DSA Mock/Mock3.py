#DSA-Assgn-303
#This assignment needs DataStructures.py file in your package, you can get it from resources page
from res.DataStructures import LinkedList,Queue,Stack
def regenerate_stack(input_stack):
    output_stack = Stack(input_stack.get_max_size())#Do Not Change the size of the ouput_stack
    count=0
    lst=[]
    while not input_stack.is_empty():
        val=input_stack.pop()
        if(val=='@'):
            count+=1
        if(count==1):
            if(val=='@'):
                val='.'
            val=val.upper()
            lst.append(val)
        else:
            if(val=='@'):
                val='.'
            lst.append(val)
    for i in lst[::-1]:
        output_stack.push(i)

    return output_stack
#You can modify the input to test your code
input_stack = Stack(10)
input_stack.push('Hello')
input_stack.push('How')
input_stack.push('are')
input_stack.push('@')
input_stack.push('@')
input_stack.push('you')
# input_stack.push('you')
# input_stack.push('@')
# input_stack.push('WelCome')
# input_stack.push('hi')
output_stack = regenerate_stack(input_stack)
output_stack.display()



