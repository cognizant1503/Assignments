#PF-Assgn-44

def find_duplicates(list_of_numbers):
    #start writing your code here
    lst=[]
    for i in list_of_numbers:
        count=list_of_numbers.count(i)
        if count>1 and i not in lst:
            lst.append(i)
    return lst
list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
