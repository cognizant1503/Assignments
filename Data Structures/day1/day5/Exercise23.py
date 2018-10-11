#DSA-Exer-23

def arrange_tickets(tickets_list):
    new_list=[]
    for i in range(1,21):
        a='T'+str(i)
        new_list.append(a)
    for i in range(0,len(new_list)):
        if(new_list[i] not in tickets_list):
            new_list[i]='V'
    group1=new_list[:10]
    group2=new_list[10:]
    
    while 'V' in group2:
        group2.remove('V')
    j=0
    while 'V' in group1:
        index=group1.index('V')
        group1.remove('V')
        group1.insert(index,group2[j])
        j+=1
    return group1
tickets_list = ['T5','T7','T1','T2','T8','T15','T17','T19','T6','T12','T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result=arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)
