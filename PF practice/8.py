#PF-Prac-8
def calculate_net_amount(trans_list):
    #start writing your code here
    deposit,withdraw=0,0
    for i in trans_list:
        if(i[0]=='D'):
            mon=int(i[2:])
            deposit+=mon
        elif(i[0]=='W'):
            mon1=int(i[2:])
            withdraw+=mon1
    net_amount=deposit-withdraw
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))