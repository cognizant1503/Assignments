#DSA-Exer-19

def swap(num_list, first_index, second_index):
    num_list[first_index],num_list[second_index]=\
    num_list[second_index],num_list[first_index]


def find_next_min(num_list,start_index):
    lst=num_list[start_index:]
    mini=min(lst)
    index=num_list.index(mini)
    return index

def selection_sort(num_list):
    for i in range(0,len(num_list)):
        index=find_next_min(num_list,i)
        swap(num_list,index,i)


#Pass different values to the function and test your program
num_list=[8,2,19,34,23, 67, 91]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)