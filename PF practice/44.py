#PF-Prac-44

def check_correct_depth(input_list, depth=0):
    #start writing your code here
    brac=0
    for i in input_list:
        if(i=='('):
            brac+=1
        elif(i==')'):
            brac-=1
        elif(i.isdigit()):
            if(brac!=int(i)):
                return False
    if(brac!=0):
        return False
    return True
                
        

input_list1=list('(1)')
input_list2=list('(2)') 
input_list3=list('((2)((3)))') 
input_list4=list('((2)(3))') 
input_list5=list('((3)(2))') 
input_list6=list('(((3)((4))(3))(2)((3)))')
output=check_correct_depth(input_list6) 
print("Input list:",input_list6)
print(output)