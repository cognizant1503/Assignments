#PF-Assgn-19
def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    delivery_charge = 0
    for i in range(1, distance_in_kms+1):
        if(i>=1 and i<=3):
            delivery_charge=0
        elif(i>=4 and i<=6):
            delivery_charge+=3
        elif(i>=7):
            delivery_charge+=6
    if(quantity_ordered>=1 and distance_in_kms>0):
        if(food_type=="V"):
            bill_amount = 120*quantity_ordered+delivery_charge
        elif(food_type=="N"):
            bill_amount = 150*quantity_ordered+delivery_charge  
        else:
            bill_amount=-1
    else:
        bill_amount=-1
    return bill_amount


bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)