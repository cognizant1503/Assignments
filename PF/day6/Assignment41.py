#PF-Assgn-41
def find_ten_substring(num_str):
    lst=[]
    for i in range(0,len(num_str)):
        lst1=[int(num_str[i])]
        for j in range(i+1,len(num_str)):
            lst1.append(int(num_str[j]))
            if(sum(lst1)==10):
                str1=''.join(str(i) for i in lst1)
                lst.append(str1)
            else:
                continue
                
    return lst            
    
num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
