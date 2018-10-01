#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    count=0
    total=0
    for i in list_of_marks:
        total+=i
    average=total/len(list_of_marks)
    for i in list_of_marks:
        if average < i:
            count+=1
    percentage = count*100/len(list_of_marks)
    return percentage
def sort_marks():
    lst=list(list_of_marks)
    lst.sort()
    
    return lst
    
    #Remove pass and write your logic here

def generate_frequency():
    lst=[]
    for i in range(0,26):
        count=list_of_marks.count(i)
        lst.insert(i,count)
    return lst
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
