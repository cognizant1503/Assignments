#PF-Prac-38
def build_index_grid(rows, columns):
    
    result_list=[]
    for i in range(0,rows):
        lst=[]
        for j in range(0,columns):
            str1=str(i)+','+str(j)
            lst.append(str1)
        result_list.append(lst)
            
    return result_list

rows=1
columns=1
result=build_index_grid(rows,columns)
print("Rows:",rows,"Columns:",columns)
print("The matrix is:",result)
for i in result:
    print(i)