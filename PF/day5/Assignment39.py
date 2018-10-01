#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,3,0]

def place_order(*item_tuple):
    item_requested=list(item_tuple[::2])
    quantity_req=list(item_tuple[1::2])
    for i in item_requested:
        if i not in menu:
            print (i,"is not available")
            
    for i in range(0,len(item_requested)):
        for j in range(0,len(menu)):
            if item_requested[i]==menu[j]:
                flag=check_quantity_available(j, quantity_req[i])
                if flag:
                    print (item_requested[i],"is available")
                else:
                    print (item_requested[i],"stock is over")


def check_quantity_available(index,quantity_requested):
    if quantity_available[index]>=quantity_requested:
        quantity_available[index]-=quantity_requested
        return True
    


#Provide different values for items ordered and test your program
place_order('Fried Rice',2,'Soup',1)
#place_order("Soup",1,"Veg Roll", 2, "Fried Rice1",1)