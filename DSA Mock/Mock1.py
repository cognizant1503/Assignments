#PF-Assgn-103

def fun(input_list):
    output_list=[]
    #Write your logic here
    for i in input_list:
        lst=i.split(':')
        left=''
        right=''
        for j in range(len(lst[0])):
            if(lst[0][j].isalpha()):
                left+=str(j)
        for k in range(len(lst[1])):
            if(lst[1][k].isdigit()):
                right+=str(k)
        if(len(left)==0):
            left='X'
        if(len(right)==0):
            right='Y'
        output_list.append(left+':'+right)
                
                
        
        
        
    return output_list

input_list = ['A12z3:xy9z1','12345:fg12x']
output_list = fun(input_list)
print(output_list)