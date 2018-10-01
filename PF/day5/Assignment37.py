#PF-Assgn-37

#Global variables
child_id=(101, 201, 301, 401, 501)
chocolates_received=[10, 5, 3, 2, 4]

def calculate_total_chocolates():
    total=0
    for i in chocolates_received:
        total+=i
    return total

def reward_child(child_id_rewarded,extra_chocolates):
    if(child_id_rewarded not in child_id):
        print('Child id is invalid')
    elif(extra_chocolates<1):
        print('Extra chocolates is less than 1')
    else:
        for i in range(0,len(child_id)):
            if child_id[i]==child_id_rewarded:
                chocolates_received[i]+=extra_chocolates
        print(chocolates_received)


print(calculate_total_chocolates())

reward_child(21,2)
