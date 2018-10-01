#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    count=0
    #Write your logic here
    for i in range(0,len(reqd_gems)):
        if (reqd_gems[i] in gems_list) and (reqd_quantity[i]>0):
            count+=1
    if(count==len(reqd_gems)):
        for i in range(0,len(reqd_gems)):
            for j in range(0,len(gems_list)):
                if(reqd_gems[i]==gems_list[j]):
                    bill_amount=bill_amount+reqd_quantity[i]*price_list[j]
        
    else:
        bill_amount=-1
    if(bill_amount>30000):
        discount=bill_amount*5/100
        bill_amount=bill_amount-discount
    return bill_amount

gems_list=["Amber","Aquamarine","Opal","Topaz"]

price_list=[4392,1342,8734,6421]

reqd_gems=["Amber","Opal","Topaz"]

reqd_quantity=[2,1,3]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)