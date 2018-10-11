#DSA-Exer-21

def merge_sort(num_list):
    # Remove pass and write the logic here to return the sorted list
    start_index=0
    last_index=len(num_list)-1
    if(start_index==last_index):
        return num_list
    else:
        mid=len(num_list)//2
        left_list=merge_sort(num_list[:mid])
        right_list=merge_sort(num_list[mid:])
        new_list=merge(left_list,right_list)
    return new_list

def merge(left_list,right_list):
    # Remove pass and write the logic to merge the elements in the left_list and right_list and return the sorted list
    i,j=0,0
    empty_list=[]
    while(i<len(left_list) and j<len(right_list)):
        if(left_list[i]<=right_list[j]):
            empty_list.append(left_list[i])
            i+=1
        else:
            empty_list.append(right_list[j])
            j+=1
    for i in left_list:
        if(i not in empty_list):
            empty_list.append(i)
    for i in right_list:
        if(i not in empty_list):
            empty_list.append(i)
    return empty_list
    
num_list=[34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:",num_list)
sorted_list = merge_sort(num_list)
print("After sorting:",sorted_list)
