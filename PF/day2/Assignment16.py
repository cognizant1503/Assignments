#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    money=0
    
    five=rupees_to_make//5
    if(five>=no_of_five):
        money = no_of_five * 5
        ones = rupees_to_make - money
        if(ones<=no_of_one):
            five_needed = no_of_five
            one_needed = ones
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed) 
        else:
            print("-1")
    elif(five<=no_of_five):
        money=five * 5
        ones=rupees_to_make-money
        if(ones<=no_of_one):
            five_needed = five
            one_needed = ones
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
            print("-1")
    else:
        print('-1')
        
                             
make_amount(105,19,3)




