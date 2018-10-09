#DSA-Assgn-19

def last_instance( num_list,  start,  end,  key):
    index=None
    #Remove pass and write your logic here
    for i in range(start,end+1):
        if num_list[i]==key:
            index=i
    if(index is None):
        return -1
    return index

num_list=[1,1,2,2,3,4,5,5,5,5]
start=0
end=len(num_list)-1
key=5 #Number to be searched
#Pass different values for num_list, start,end and key and test your program
result=last_instance(num_list, start,end,key)

if(result!=-1):
    print("The index position of the last occurrence of the number:",result)
else:
    print("Number not found")