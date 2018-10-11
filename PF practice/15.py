#PF-Prac-15
def check_22(num_list):
    #start writing your code here
    for i in range(0,len(num_list)-1):
        if(num_list[i]==num_list[i+1]):
            return True
    return False   
print(check_22([3,2,5,1,2,1,2,2]))